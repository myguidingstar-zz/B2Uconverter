"""
B2UConverter — UNO extension for OpenOffice.org
File: include/vietnamese_recoding.py

Copyright ©2009  Ministry of Science and Technology of Vietnam
License: GNU Lesser General Public License version 2.1
Authors: Jean Christophe André <jcandre@hanoilug.org>
         Lê Quốc Thái <lqthai@hanoilug.org>
         Võ Đức Phương <vdphuong@hanoilug.org>
"""

class VietnameseTextConverter(object):

    _diacritics = (
        #'âÂăĂđĐêÊôÔơƠưƯ'
        u'\xe2\xc2\u0103\u0102\u0111\u0110\xea\xca\xf4\xd4\u01a1\u01a0\u01b0\u01af'
        #'áÁàÀảẢãÃạẠấẤầẦẩẨẫẪậẬắẮằẰẳẲẵẴặẶ'
        u'\xe1\xc1\xe0\xc0\u1ea3\u1ea2\xe3\xc3\u1ea1\u1ea0\u1ea5\u1ea4\u1ea7\u1ea6\u1ea9\u1ea8\u1eab\u1eaa\u1ead\u1eac\u1eaf\u1eae\u1eb1\u1eb0\u1eb3\u1eb2\u1eb5\u1eb4\u1eb7\u1eb6'
        #'éÉèÈẻẺẽẼẹẸếẾềỀểỂễỄệỆíÍìÌỉỈĩĨịỊ'
        u'\xe9\xc9\xe8\xc8\u1ebb\u1eba\u1ebd\u1ebc\u1eb9\u1eb8\u1ebf\u1ebe\u1ec1\u1ec0\u1ec3\u1ec2\u1ec5\u1ec4\u1ec7\u1ec6\xed\xcd\xec\xcc\u1ec9\u1ec8\u0129\u0128\u1ecb\u1eca'
        #'óÓòÒỏỎõÕọỌốỐồỒổỔỗỖộỘớỚờỜởỞỡỠợỢ'
        u'\xf3\xd3\xf2\xd2\u1ecf\u1ece\xf5\xd5\u1ecd\u1ecc\u1ed1\u1ed0\u1ed3\u1ed2\u1ed5\u1ed4\u1ed7\u1ed6\u1ed9\u1ed8\u1edb\u1eda\u1edd\u1edc\u1edf\u1ede\u1ee1\u1ee0\u1ee3\u1ee2'
        #'úÚùÙủỦũŨụỤứỨừỪửỬữỮựỰỳỲỷỶỹỸỵỴýÝ'
        u'\xfa\xda\xf9\xd9\u1ee7\u1ee6\u0169\u0168\u1ee5\u1ee4\u1ee9\u1ee8\u1eeb\u1eea\u1eed\u1eec\u1eef\u1eee\u1ef1\u1ef0\u1ef3\u1ef2\u1ef7\u1ef6\u1ef9\u1ef8\u1ef5\u1ef4\xfd\xdd'
    )
    _diacritics_removed = (
        u'aAaAdDeEoOoOuU'
        u'aAaAaAaAaAaAaAaAaAaAaAaAaAaAaA'
        u'eEeEeEeEeEeEeEeEeEeEiIiIiIiIiI'
        u'oOoOoOoOoOoOoOoOoOoOoOoOoOoOoO'
        u'uUuUuUuUuUuUuUuUuUuUyYyYyYyYyY'
    )

    def __init__(self, decoderPrefix=None,
                                removeDiacritics=False, vniHacks=False):
        self.decoderPrefix = decoderPrefix and decoderPrefix or ''
        self.removeDiacriticsFlag = removeDiacritics
        self.vniHacksFlag = vniHacks

    def removeDiacritics(self, str):
        result = u''
        for c in str:
            idx = self._diacritics.find(c)
            if idx >= 0:
                c = self._diacritics_removed[idx]
            result += c
        return result

    def convertString(self, str, real, upper=False):
        if not str: return u''
        result = u''
        prefixed_real = self.decoderPrefix + real

        logging.debug("convertString('%s')", str)
        # compensate for (supposedly) some VNI encoder's bug(s)
        if self.vniHacksFlag and real == 'vni':
            # two consecutive 'Â', 'â', 'å', 'ï', 'ù', 'õ'
            for c in [u'\xC2', u'\xE2', u'\xE5', u'\xEF', u'\xF5', u'\xF9']:
                while (str.find(c * 2) >= 0):
                    str = str.replace(c * 2, c)
            # 'âê' -> 'â'
            while (str.find(u'\xE2\xEA') >= 0):
                str = str.replace(u'\xE2\xEA', u'\xE2')
            # 'ÀÂ' -> 'À'
            while (str.find(u'\xC0\xC2') >= 0):
                str = str.replace(u'\xC0\xC2', u'\xC0')
            # 'àø' -> 'à'
            while (str.find(u'\xE0\xF8') >= 0):
                str = str.replace(u'\xE0\xF8', u'\xE0')
        # Vietnamese case: mix of byte & Unicode chars
        i = 0
        while (i < len(str)):
            # find cp1252 content and convert it
            j = i
            while (j < len(str) and str[j] in cp1252_decoding_table): j += 1
            segment = str[i:j].encode('cp1252').decode(prefixed_real)
            if self.removeDiacriticsFlag:
                segment = self.removeDiacritics(segment)
            if upper: segment = segment.upper()
            result += segment
            # find Unicode content and keep it
            # XXX: could use this information to detect text already converted!
            k = j
            while (k < len(str) and ord(str[k]) >= 256): k += 1
            result += str[j:k]
            i = k

        # compensate for OOo's bug on MS-Office's soft hyphen importation
        if real == 'vntime_tcvn':
            # luckily there is no Vietnamese word with two consecutive 'ư'
            while (result.find(u'\u01B0\u01B0') >= 0):
                result = result.replace(u'\u01B0\u01B0', u'\u01B0')

        logging.debug("convertString -> '%s'", result)
        return result

