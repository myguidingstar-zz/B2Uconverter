""" Python Character Mapping Codec vni (VNI Software Company - Vietnamese)
    Copyright (c) 2008-2009  Jean Christophe André <jcandre@hanoilug.org>
    License: GNU Lesser General Public License version 2.1
    To enable this encoding, move this file into /usr/lib/python2.5/encodings/

    Created from information found at http://vnisoft.com/english/vnichar.htm

    WARNING: THE ENCODING IS UNFINISHED YET !!! (READ *NOT* WORKING)
"""

def _create_vni_secondhalf_decoding_table():
    _decoding_table = {}
    ### MISC
    _decoding_table['\x80'] = u'\uFFFE' # UNDEFINED
    _decoding_table['\x81'] = u'\uFFFE' # UNDEFINED
    _decoding_table['\x82'] = u'\xC6' # CAPITAL AE
    _decoding_table['\x83'] = u'\u0192' # SMALL F WITH HOOK
    _decoding_table['\x84'] = u'\xE6' # SMALL AE
    _decoding_table['\x85'] = u'\u2026' # HORIZONTAL ELLIPSIS
    _decoding_table['\x86'] = u'\u2020' # DAGGER
    _decoding_table['\x87'] = u'\u2021' # DOUBLE DAGGER
    _decoding_table['\x88'] = u'\uFFFE' # FIXME: UNKNOWN
    _decoding_table['\x89'] = u'\u2030' # PER MILLE SIGN
    _decoding_table['\x8A'] = u'\uFFFE' # FIXME: DIAERESIS ABOVE FOR CAPITAL
    _decoding_table['\x8B'] = u'\u2039' # SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    _decoding_table['\x8C'] = u'\uFFFE' # FIXME: HOOK ABOVE FOR CAPITAL (also \xDB)
    _decoding_table['\x8D'] = u'\uFFFE' # UNDEFINED
    _decoding_table['\x8E'] = u'\uFFFE' # FIXME: UNKNOWN
    _decoding_table['\x8F'] = u'\uFFFE' # UNDEFINED
    _decoding_table['\x90'] = u'\uFFFE' # UNDEFINED
    _decoding_table['\x91'] = u'\u2018' # LEFT SINGLE QUOTATION MARK
    _decoding_table['\x92'] = u'\u2019' # RIGHT SINGLE QUOTATION MARK
    _decoding_table['\x93'] = u'\u201C' # LEFT DOUBLE QUOTATION MARK
    _decoding_table['\x94'] = u'\u201D' # RIGHT DOUBLE QUOTATION MARK
    _decoding_table['\x95'] = u'\uFFFE' # FIXME: UNKNOWN
    _decoding_table['\x96'] = u'\u2013' # EN DASH
    _decoding_table['\x97'] = u'\u2014' # EM DASH
    _decoding_table['\x98'] = u'\uFFFE' # FIXME: UNKNOWN
    _decoding_table['\x99'] = u'\u2122' # TRADE MARK SIGN
    _decoding_table['\x9A'] = u'\uFFFE' # FIXME: DIAERESIS ABOVE FOR SMALL
    _decoding_table['\x9B'] = u'\u203A' # SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    _decoding_table['\x9C'] = u'\uFFFE' # FIXME: HOOK ABOVE FOR SMALL (also \xFB)
    _decoding_table['\x9D'] = u'\uFFFE' # UNDEFINED
    _decoding_table['\x9E'] = u'\uFFFE' # FIXME: UNKNOWN
    _decoding_table['\x9F'] = u'\u1EF4' # CAPITAL Y WITH DOT BELOW (also \xCE)
    _decoding_table['\xA0'] = u'\xA0' # UNICODE
    _decoding_table['\xA1'] = u'\xA1' # UNICODE
    _decoding_table['\xA2'] = u'\xA2' # UNICODE
    _decoding_table['\xA3'] = u'\xA3' # UNICODE
    _decoding_table['\xA4'] = u'\xA4' # UNICODE
    _decoding_table['\xA5'] = u'\xA5' # UNICODE
    _decoding_table['\xA6'] = u'\xA6' # UNICODE
    _decoding_table['\xA7'] = u'\xA7' # UNICODE
    _decoding_table['\xA8'] = u'\uFFFE' # FIXME: RING ABOVE FOR CAPITAL
    _decoding_table['\xA9'] = u'\xA9' # UNICODE
    _decoding_table['\xAA'] = u'\uFFFE' # FIXME: PLAIN SQUARE
    _decoding_table['\xAB'] = u'\xAB' # UNICODE
    _decoding_table['\xAC'] = u'\u0152' # CAPITAL LIGATURE OE
    _decoding_table['\xAD'] = u'\xAD' # UNICODE
    _decoding_table['\xAE'] = u'\xAE' # UNICODE
    _decoding_table['\xAF'] = u'\xAF' # UNICODE
    _decoding_table['\xB0'] = u'\uFFFE' # FIXME: PLAIN CIRCLE
    _decoding_table['\xB1'] = u'\xB1' # UNICODE
    _decoding_table['\xB2'] = u'\xB2' # UNICODE
    _decoding_table['\xB3'] = u'\xB3' # UNICODE
    _decoding_table['\xB4'] = u'\uFFFE' # FIXME: CARON ABOVE FOR CAPITAL
    _decoding_table['\xB5'] = u'\xB5' # UNICODE
    _decoding_table['\xB6'] = u'\xB6' # UNICODE
    _decoding_table['\xB7'] = u'\uFFFE' # FIXME: RING ABOVE FOR SMALL
    _decoding_table['\xB8'] = u'\uFFFE' # FIXME: CARON ABOVE FOR SMALL
    _decoding_table['\xB9'] = u'\xB9' # UNICODE
    _decoding_table['\xBA'] = u'\uFFFE' # FIXME: EMPTY SQUARE
    _decoding_table['\xBB'] = u'\xBB' # UNICODE
    _decoding_table['\xBC'] = u'\xBC' # UNICODE
    _decoding_table['\xBD'] = u'\xBD' # UNICODE
    _decoding_table['\xBE'] = u'\xBE' # UNICODE
    _decoding_table['\xBF'] = u'\xBF' # UNICODE
    ### CAPITAL LETTERS
    _decoding_table['\xC0'] = {
        'A':    u'\u1EA6', # CAPITAL A WITH CIRCUMFLEX AND GRAVE
        'E':    u'\u1EC0', # CAPITAL E WITH CIRCUMFLEX AND GRAVE
        'O':    u'\u1ED2', # CAPITAL O WITH CIRCUMFLEX AND GRAVE
    }
    _decoding_table['\xC1'] = {
        'A':    u'\u1EA4', # CAPITAL A WITH CIRCUMFLEX AND ACUTE
        'E':    u'\u1EBE', # CAPITAL E WITH CIRCUMFLEX AND ACUTE
        'O':    u'\u1ED0', # CAPITAL O WITH CIRCUMFLEX AND ACUTE
    }
    _decoding_table['\xC2'] = {
        'A':    u'\u00C2', # CAPITAL A WITH CIRCUMFLEX
        'E':    u'\u00CA', # CAPITAL E WITH CIRCUMFLEX
        'I':    u'\u00CE', # CAPITAL I WITH CIRCUMFLEX # XXX: unused because of \xDD ?
        'O':    u'\u00D4', # CAPITAL O WITH CIRCUMFLEX
    }
    _decoding_table['\xC3'] = {
        'A':    u'\u1EAA', # CAPITAL A WITH CIRCUMFLEX AND TILDE
        'E':    u'\u1EC4', # CAPITAL E WITH CIRCUMFLEX AND TILDE
        'O':    u'\u1ED6', # CAPITAL O WITH CIRCUMFLEX AND TILDE
    }
    _decoding_table['\xC4'] = {
        'A':    u'\u1EAC', # CAPITAL A WITH CIRCUMFLEX AND DOT BELOW
        'E':    u'\u1EC6', # CAPITAL E WITH CIRCUMFLEX AND DOT BELOW
        'O':    u'\u1ED8', # CAPITAL O WITH CIRCUMFLEX AND DOT BELOW
    }
    _decoding_table['\xC5'] = {
        'A':    u'\u1EA8', # CAPITAL A WITH CIRCUMFLEX AND HOOK
        'E':    u'\u1EC2', # CAPITAL E WITH CIRCUMFLEX AND HOOK
        'O':    u'\u1ED4', # CAPITAL O WITH CIRCUMFLEX AND HOOK
    }
    _decoding_table['\xC6'] = u'\u1EC8' # CAPITAL I WITH HOOK
    _decoding_table['\xC7'] = u'\xC7' # UNICODE
    _decoding_table['\xC8'] = {
        'A':    u'\u1EB0', # CAPITAL A WITH BREVE AND GRAVE
    }
    _decoding_table['\xC9'] = {
        'A':    u'\u1EAE', # CAPITAL A WITH BREVE AND ACUTE
    }
    _decoding_table['\xCA'] = {
        'A':    u'\u0102', # CAPITAL A WITH BREVE
    }
    _decoding_table['\xCB'] = {
        'A':    u'\u1EB6', # CAPITAL A WITH BREVE AND DOT BELOW
    }
    _decoding_table['\xCC'] = u'\u00CC' # CAPITAL I WITH GRAVE
    _decoding_table['\xCD'] = u'\u00CD' # CAPITAL I WITH ACUTE
    _decoding_table['\xCE'] = u'\u1EF4' # CAPITAL Y WITH DOT BELOW
    _decoding_table['\xCF'] = {
        'A':    u'\u1EA0', # CAPITAL A WITH DOT BELOW
        'E':    u'\u1EB8', # CAPITAL E WITH DOT BELOW
        'I':    u'\u1ECA', # CAPITAL I WITH DOT BELOW # XXX: unused because of \xD2 ?
        'O':    u'\u1ECC', # CAPITAL O WITH DOT BELOW
        '\xD4': u'\u1EE2', # CAPITAL O WITH DOT BELOW AND HORN
        'U':    u'\u1EE4', # CAPITAL U WITH DOT BELOW
        '\xD6': u'\u1EF0', # CAPITAL U WITH DOT BELOW AND HORN
        'Y':    u'\u1EF4', # CAPITAL Y WITH DOT BELOW # XXX: unused because of \xCE ?
    }
    _decoding_table['\xD0'] = u'\u00CF' # CAPITAL I WITH DIAERESIS
    _decoding_table['\xD1'] = u'\u0110' # CAPITAL D WITH STROKE
    _decoding_table['\xD2'] = u'\u1ECA' # CAPITAL I WITH DOT BELOW
    _decoding_table['\xD3'] = u'\u0128' # CAPITAL I WITH TILDE
    _decoding_table['\xD4'] = u'\u01A0' # CAPITAL O WITH HORN
    _decoding_table['\xD5'] = {
        'A':    u'\u00C3', # CAPITAL A WITH TILDE
        'E':    u'\u1EBC', # CAPITAL E WITH TILDE
        'I':    u'\u0128', # CAPITAL I WITH TILDE # XXX: unused because of \xD3 ?
        'O':    u'\u00D5', # CAPITAL O WITH TILDE
        '\xD4': u'\u1EE0', # CAPITAL O WITH TILDE AND HORN
        'U':    u'\u0168', # CAPITAL U WITH TILDE
        '\xD6': u'\u1EEE', # CAPITAL U WITH TILDE AND HORN
        'Y':    u'\u1EF8', # CAPITAL Y WITH TILDE
    }
    _decoding_table['\xD6'] = u'\u01AF' # CAPITAL U WITH HORN
    _decoding_table['\xD7'] = u'\xD7' # UNICODE
    _decoding_table['\xD8'] = {
        'A':    u'\u00C0', # CAPITAL A WITH GRAVE
        'E':    u'\u00C8', # CAPITAL E WITH GRAVE
        'I':    u'\u00CC', # CAPITAL I WITH GRAVE # XXX: unused because of \xCC ?
        'O':    u'\u00D2', # CAPITAL O WITH GRAVE
        '\xD4': u'\u1EDC', # CAPITAL O WITH GRAVE AND HORN
        'U':    u'\u00D9', # CAPITAL U WITH GRAVE
        '\xD6': u'\u1EEA', # CAPITAL U WITH GRAVE AND HORN
        'Y':    u'\u1EF2', # CAPITAL Y WITH GRAVE
    }
    _decoding_table['\xD9'] = {
        'A':    u'\u00C1', # CAPITAL A WITH ACUTE
        'E':    u'\u00C9', # CAPITAL E WITH ACUTE
        'I':    u'\u00CD', # CAPITAL I WITH ACUTE # XXX: unused because of \xCD ?
        'O':    u'\u00D3', # CAPITAL O WITH ACUTE
        '\xD4': u'\u1EDA', # CAPITAL O WITH ACUTE AND HORN
        'U':    u'\u00DA', # CAPITAL U WITH ACUTE
        '\xD6': u'\u1EE8', # CAPITAL U WITH ACUTE AND HORN
        'Y':    u'\u00DD', # CAPITAL Y WITH ACUTE
    }
    _decoding_table['\xDA'] = {
        'A':    u'\u1EB2', # CAPITAL A WITH BREVE AND HOOK
    }
    _decoding_table['\xDB'] = {
        'A':    u'\u1EA2', # CAPITAL A WITH HOOK
        'E':    u'\u1EBA', # CAPITAL E WITH HOOK
        'I':    u'\u1EC8', # CAPITAL I WITH HOOK # XXX: unused because of \xC6 ?
        'O':    u'\u1ECE', # CAPITAL O WITH HOOK
        '\xD4': u'\u1EDE', # CAPITAL O WITH HOOK AND HORN
        'U':    u'\u1EE6', # CAPITAL U WITH HOOK
        '\xD6': u'\u1EEC', # CAPITAL U WITH HOOK AND HORN
        'Y':    u'\u1EF6', # CAPITAL Y WITH HOOK
    }
    _decoding_table['\xDC'] = {
        'A':    u'\u1EB4', # CAPITAL A WITH BREVE AND TILDE
    }
    _decoding_table['\xDD'] = u'\u00CE' # CAPITAL I WITH CIRCUMFLEX
    _decoding_table['\xDE'] = u'\xDE' # UNICODE
    _decoding_table['\xDF'] = u'\xDF' # UNICODE
    ### SMALL LETTERS
    _decoding_table['\xE0'] = {
        'a':    u'\u1EA7', # SMALL A WITH CIRCUMFLEX AND GRAVE
        'e':    u'\u1EC1', # SMALL E WITH CIRCUMFLEX AND GRAVE
        'o':    u'\u1ED3', # SMALL O WITH CIRCUMFLEX AND GRAVE
    }
    _decoding_table['\xE1'] = {
        'a':    u'\u1EA5', # SMALL A WITH CIRCUMFLEX AND ACUTE
        'e':    u'\u1EBF', # SMALL E WITH CIRCUMFLEX AND ACUTE
        'o':    u'\u1ED1', # SMALL O WITH CIRCUMFLEX AND ACUTE
    }
    _decoding_table['\xE2'] = {
        'a':    u'\u00E2', # SMALL A WITH CIRCUMFLEX
        'e':    u'\u00EA', # SMALL E WITH CIRCUMFLEX
        'i':    u'\u00EE', # SMALL I WITH CIRCUMFLEX # XXX: unused because of \xFD ?
        'o':    u'\u00F4', # SMALL O WITH CIRCUMFLEX
    }
    _decoding_table['\xE3'] = {
        'a':    u'\u1EAB', # SMALL A WITH CIRCUMFLEX AND TILDE
        'e':    u'\u1EC5', # SMALL E WITH CIRCUMFLEX AND TILDE
        'o':    u'\u1ED7', # SMALL O WITH CIRCUMFLEX AND TILDE
    }
    _decoding_table['\xE4'] = {
        'a':    u'\u1EAD', # SMALL A WITH CIRCUMFLEX AND DOT BELOW
        'e':    u'\u1EC7', # SMALL E WITH CIRCUMFLEX AND DOT BELOW
        'o':    u'\u1ED9', # SMALL O WITH CIRCUMFLEX AND DOT BELOW
    }
    _decoding_table['\xE5'] = {
        'a':    u'\u1EA9', # SMALL A WITH CIRCUMFLEX AND HOOK
        'e':    u'\u1EC3', # SMALL E WITH CIRCUMFLEX AND HOOK
        'o':    u'\u1ED5', # SMALL O WITH CIRCUMFLEX AND HOOK
    }
    _decoding_table['\xE6'] = u'\u1EC9' # SMALL I WITH HOOK
    _decoding_table['\xE7'] = u'\xE7' # UNICODE
    _decoding_table['\xE8'] = {
        'a':    u'\u1EB1', # SMALL A WITH BREVE AND GRAVE
    }
    _decoding_table['\xE9'] = {
        'a':    u'\u1EAF', # SMALL A WITH BREVE AND ACUTE
    }
    _decoding_table['\xEA'] = {
        'a':    u'\u0103', # SMALL A WITH BREVE
    }
    _decoding_table['\xEB'] = {
        'a':    u'\u1EB7', # SMALL A WITH BREVE AND DOT BELOW
    }
    _decoding_table['\xEC'] = u'\u00EC' # SMALL I WITH GRAVE
    _decoding_table['\xED'] = u'\u00ED' # SMALL I WITH ACUTE
    _decoding_table['\xEE'] = u'\u1EF5' # SMALL Y WITH DOT BELOW
    _decoding_table['\xEF'] = {
        'a':    u'\u1EA1', # SMALL A WITH DOT BELOW
        'e':    u'\u1EB9', # SMALL E WITH DOT BELOW
        'i':    u'\u1ECB', # SMALL I WITH DOT BELOW # XXX: unused because of \xF2 ?
        'o':    u'\u1ECD', # SMALL O WITH DOT BELOW
        '\xF4': u'\u1EE3', # SMALL O WITH DOT BELOW AND HORN
        'u':    u'\u1EE5', # SMALL U WITH DOT BELOW
        '\xF6': u'\u1EF1', # SMALL U WITH DOT BELOW AND HORN
        'y':    u'\u1EF5', # SMALL Y WITH DOT BELOW # XXX: unused because of \xEE ?
    }
    _decoding_table['\xF0'] = u'\u00EF' # SMALL I WITH DIAERESIS
    _decoding_table['\xF1'] = u'\u0111' # SMALL D WITH STROKE
    _decoding_table['\xF2'] = u'\u1ECB' # SMALL I WITH DOT BELOW
    _decoding_table['\xF3'] = u'\u0129' # SMALL I WITH TILDE
    _decoding_table['\xF4'] = u'\u01A1' # SMALL O WITH HORN
    _decoding_table['\xF5'] = {
        'a':    u'\u00E3', # SMALL A WITH TILDE
        'e':    u'\u1EBD', # SMALL E WITH TILDE
        'i':    u'\u0129', # SMALL I WITH TILDE # XXX: unused because of \xF3 ?
        'o':    u'\u00F5', # SMALL O WITH TILDE
        '\xF4': u'\u1EE1', # SMALL O WITH TILDE AND HORN
        'u':    u'\u0169', # SMALL U WITH TILDE
        '\xF6': u'\u1EEF', # SMALL U WITH TILDE AND HORN
        'y':    u'\u1EF9', # SMALL Y WITH TILDE
    }
    _decoding_table['\xF6'] = u'\u01B0' # SMALL U WITH HORN
    _decoding_table['\xF7'] = u'\xF7' # UNICODE
    _decoding_table['\xF8'] = {
        'a':    u'\u00E0', # SMALL A WITH GRAVE
        'e':    u'\u00E8', # SMALL E WITH GRAVE
        'i':    u'\u00EC', # SMALL I WITH GRAVE # XXX: unused because of \xEC ?
        'o':    u'\u00F2', # SMALL O WITH GRAVE
        '\xF4': u'\u1EDD', # SMALL O WITH GRAVE AND HORN
        'u':    u'\u00F9', # SMALL U WITH GRAVE
        '\xF6': u'\u1EEB', # SMALL U WITH GRAVE AND HORN
        'y':    u'\u1EF3', # SMALL Y WITH GRAVE
    }
    _decoding_table['\xF9'] = {
        'a':    u'\u00E1', # SMALL A WITH ACUTE
        'e':    u'\u00E9', # SMALL E WITH ACUTE
        'i':    u'\u00ED', # SMALL I WITH ACUTE # XXX: unused because of \xED ?
        'o':    u'\u00F3', # SMALL O WITH ACUTE
        '\xF4': u'\u1EDB', # SMALL O WITH ACUTE AND HORN
        'u':    u'\u00FA', # SMALL U WITH ACUTE
        '\xF6': u'\u1EE9', # SMALL U WITH ACUTE AND HORN
        'y':    u'\u00FD', # SMALL Y WITH ACUTE
    }
    _decoding_table['\xFA'] = {
        'a':    u'\u1EB3', # SMALL A WITH BREVE AND HOOK
    }
    _decoding_table['\xFB'] = {
        'a':    u'\u1EA3', # SMALL A WITH HOOK
        'e':    u'\u1EBB', # SMALL E WITH HOOK
        'i':    u'\u1EC9', # SMALL I WITH HOOK # XXX: unused because of \xE6 ?
        'o':    u'\u1ECF', # SMALL O WITH HOOK
        '\xF4': u'\u1EDF', # SMALL O WITH HOOK AND HORN
        'u':    u'\u1EE7', # SMALL U WITH HOOK
        '\xF6': u'\u1EED', # SMALL U WITH HOOK AND HORN
        'y':    u'\u1EF7', # SMALL Y WITH HOOK
    }
    _decoding_table['\xFC'] = {
        'a':    u'\u1EB5', # SMALL A WITH BREVE AND TILDE
    }
    _decoding_table['\xFD'] = u'\u00EE' # SMALL I WITH CIRCUMFLEX
    _decoding_table['\xFE'] = u'\xFE' # UNICODE
    _decoding_table['\xFF'] = u'\u1EF5' # SMALL Y WITH DOT BELOW
    ### SMALL LETTERS ACCENTS APPLIED ON CAPITALS LETTERS (!?) # seen in use...
    for i in range(0xE0, 0xFF):
        if type(_decoding_table[chr(i)]) == dict:
            _decoding_table[chr(i)].update(_decoding_table[chr(i-0x20)])
    ###
    return _decoding_table

_vni_secondhalf_decoding_table = _create_vni_secondhalf_decoding_table()

def vni_decode(input, errors='strict'):
    assert errors == 'strict'
    output = u''
    _decoding_table = _vni_secondhalf_decoding_table
    for i,c in enumerate(input):
        if ord(c) < 0x80:
            output += c
        elif type(_decoding_table[c]) == dict:
            try:
                output = output[:-1] + _decoding_table[c][input[i-1]]
            except KeyError:
                # TODO: return more informative values? (error,position)
                raise ValueError("bad encoded data at position %d" % i)
        else:
            output += _decoding_table[c]
    return (output, len(input))

def vni_encode(input,errors='strict'):
    assert errors == 'strict'
    _encoding_table = {}
    _encoding_table[u'\u00C0'] = 'A\xD8'
    # FIXME: to continue...
    output = ''
    for c in input:
        if c in _encoding_table:
            output += _encoding_table[c]
        else:
            output += c
    return (output, len(input))

