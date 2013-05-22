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
    _decoding_table['\x80'] = '\uFFFE' # UNDEFINED
    _decoding_table['\x81'] = '\uFFFE' # UNDEFINED
    _decoding_table['\x82'] = '\xC6' # CAPITAL AE
    _decoding_table['\x83'] = '\u0192' # SMALL F WITH HOOK
    _decoding_table['\x84'] = '\xE6' # SMALL AE
    _decoding_table['\x85'] = '\u2026' # HORIZONTAL ELLIPSIS
    _decoding_table['\x86'] = '\u2020' # DAGGER
    _decoding_table['\x87'] = '\u2021' # DOUBLE DAGGER
    _decoding_table['\x88'] = '\uFFFE' # FIXME: UNKNOWN
    _decoding_table['\x89'] = '\u2030' # PER MILLE SIGN
    _decoding_table['\x8A'] = '\uFFFE' # FIXME: DIAERESIS ABOVE FOR CAPITAL
    _decoding_table['\x8B'] = '\u2039' # SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    _decoding_table['\x8C'] = '\uFFFE' # FIXME: HOOK ABOVE FOR CAPITAL (also \xDB)
    _decoding_table['\x8D'] = '\uFFFE' # UNDEFINED
    _decoding_table['\x8E'] = '\uFFFE' # FIXME: UNKNOWN
    _decoding_table['\x8F'] = '\uFFFE' # UNDEFINED
    _decoding_table['\x90'] = '\uFFFE' # UNDEFINED
    _decoding_table['\x91'] = '\u2018' # LEFT SINGLE QUOTATION MARK
    _decoding_table['\x92'] = '\u2019' # RIGHT SINGLE QUOTATION MARK
    _decoding_table['\x93'] = '\u201C' # LEFT DOUBLE QUOTATION MARK
    _decoding_table['\x94'] = '\u201D' # RIGHT DOUBLE QUOTATION MARK
    _decoding_table['\x95'] = '\uFFFE' # FIXME: UNKNOWN
    _decoding_table['\x96'] = '\u2013' # EN DASH
    _decoding_table['\x97'] = '\u2014' # EM DASH
    _decoding_table['\x98'] = '\uFFFE' # FIXME: UNKNOWN
    _decoding_table['\x99'] = '\u2122' # TRADE MARK SIGN
    _decoding_table['\x9A'] = '\uFFFE' # FIXME: DIAERESIS ABOVE FOR SMALL
    _decoding_table['\x9B'] = '\u203A' # SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    _decoding_table['\x9C'] = '\uFFFE' # FIXME: HOOK ABOVE FOR SMALL (also \xFB)
    _decoding_table['\x9D'] = '\uFFFE' # UNDEFINED
    _decoding_table['\x9E'] = '\uFFFE' # FIXME: UNKNOWN
    _decoding_table['\x9F'] = '\u1EF4' # CAPITAL Y WITH DOT BELOW (also \xCE)
    _decoding_table['\xA0'] = '\xA0' # UNICODE
    _decoding_table['\xA1'] = '\xA1' # UNICODE
    _decoding_table['\xA2'] = '\xA2' # UNICODE
    _decoding_table['\xA3'] = '\xA3' # UNICODE
    _decoding_table['\xA4'] = '\xA4' # UNICODE
    _decoding_table['\xA5'] = '\xA5' # UNICODE
    _decoding_table['\xA6'] = '\xA6' # UNICODE
    _decoding_table['\xA7'] = '\xA7' # UNICODE
    _decoding_table['\xA8'] = '\uFFFE' # FIXME: RING ABOVE FOR CAPITAL
    _decoding_table['\xA9'] = '\xA9' # UNICODE
    _decoding_table['\xAA'] = '\uFFFE' # FIXME: PLAIN SQUARE
    _decoding_table['\xAB'] = '\xAB' # UNICODE
    _decoding_table['\xAC'] = '\u0152' # CAPITAL LIGATURE OE
    _decoding_table['\xAD'] = '\xAD' # UNICODE
    _decoding_table['\xAE'] = '\xAE' # UNICODE
    _decoding_table['\xAF'] = '\xAF' # UNICODE
    _decoding_table['\xB0'] = '\uFFFE' # FIXME: PLAIN CIRCLE
    _decoding_table['\xB1'] = '\xB1' # UNICODE
    _decoding_table['\xB2'] = '\xB2' # UNICODE
    _decoding_table['\xB3'] = '\xB3' # UNICODE
    _decoding_table['\xB4'] = '\uFFFE' # FIXME: CARON ABOVE FOR CAPITAL
    _decoding_table['\xB5'] = '\xB5' # UNICODE
    _decoding_table['\xB6'] = '\xB6' # UNICODE
    _decoding_table['\xB7'] = '\uFFFE' # FIXME: RING ABOVE FOR SMALL
    _decoding_table['\xB8'] = '\uFFFE' # FIXME: CARON ABOVE FOR SMALL
    _decoding_table['\xB9'] = '\xB9' # UNICODE
    _decoding_table['\xBA'] = '\uFFFE' # FIXME: EMPTY SQUARE
    _decoding_table['\xBB'] = '\xBB' # UNICODE
    _decoding_table['\xBC'] = '\xBC' # UNICODE
    _decoding_table['\xBD'] = '\xBD' # UNICODE
    _decoding_table['\xBE'] = '\xBE' # UNICODE
    _decoding_table['\xBF'] = '\xBF' # UNICODE
    ### CAPITAL LETTERS
    _decoding_table['\xC0'] = {
        'A':    '\u1EA6', # CAPITAL A WITH CIRCUMFLEX AND GRAVE
        'E':    '\u1EC0', # CAPITAL E WITH CIRCUMFLEX AND GRAVE
        'O':    '\u1ED2', # CAPITAL O WITH CIRCUMFLEX AND GRAVE
    }
    _decoding_table['\xC1'] = {
        'A':    '\u1EA4', # CAPITAL A WITH CIRCUMFLEX AND ACUTE
        'E':    '\u1EBE', # CAPITAL E WITH CIRCUMFLEX AND ACUTE
        'O':    '\u1ED0', # CAPITAL O WITH CIRCUMFLEX AND ACUTE
    }
    _decoding_table['\xC2'] = {
        'A':    '\u00C2', # CAPITAL A WITH CIRCUMFLEX
        'E':    '\u00CA', # CAPITAL E WITH CIRCUMFLEX
        'I':    '\u00CE', # CAPITAL I WITH CIRCUMFLEX # XXX: unused because of \xDD ?
        'O':    '\u00D4', # CAPITAL O WITH CIRCUMFLEX
    }
    _decoding_table['\xC3'] = {
        'A':    '\u1EAA', # CAPITAL A WITH CIRCUMFLEX AND TILDE
        'E':    '\u1EC4', # CAPITAL E WITH CIRCUMFLEX AND TILDE
        'O':    '\u1ED6', # CAPITAL O WITH CIRCUMFLEX AND TILDE
    }
    _decoding_table['\xC4'] = {
        'A':    '\u1EAC', # CAPITAL A WITH CIRCUMFLEX AND DOT BELOW
        'E':    '\u1EC6', # CAPITAL E WITH CIRCUMFLEX AND DOT BELOW
        'O':    '\u1ED8', # CAPITAL O WITH CIRCUMFLEX AND DOT BELOW
    }
    _decoding_table['\xC5'] = {
        'A':    '\u1EA8', # CAPITAL A WITH CIRCUMFLEX AND HOOK
        'E':    '\u1EC2', # CAPITAL E WITH CIRCUMFLEX AND HOOK
        'O':    '\u1ED4', # CAPITAL O WITH CIRCUMFLEX AND HOOK
    }
    _decoding_table['\xC6'] = '\u1EC8' # CAPITAL I WITH HOOK
    _decoding_table['\xC7'] = '\xC7' # UNICODE
    _decoding_table['\xC8'] = {
        'A':    '\u1EB0', # CAPITAL A WITH BREVE AND GRAVE
    }
    _decoding_table['\xC9'] = {
        'A':    '\u1EAE', # CAPITAL A WITH BREVE AND ACUTE
    }
    _decoding_table['\xCA'] = {
        'A':    '\u0102', # CAPITAL A WITH BREVE
    }
    _decoding_table['\xCB'] = {
        'A':    '\u1EB6', # CAPITAL A WITH BREVE AND DOT BELOW
    }
    _decoding_table['\xCC'] = '\u00CC' # CAPITAL I WITH GRAVE
    _decoding_table['\xCD'] = '\u00CD' # CAPITAL I WITH ACUTE
    _decoding_table['\xCE'] = '\u1EF4' # CAPITAL Y WITH DOT BELOW
    _decoding_table['\xCF'] = {
        'A':    '\u1EA0', # CAPITAL A WITH DOT BELOW
        'E':    '\u1EB8', # CAPITAL E WITH DOT BELOW
        'I':    '\u1ECA', # CAPITAL I WITH DOT BELOW # XXX: unused because of \xD2 ?
        'O':    '\u1ECC', # CAPITAL O WITH DOT BELOW
        '\xD4': '\u1EE2', # CAPITAL O WITH DOT BELOW AND HORN
        'U':    '\u1EE4', # CAPITAL U WITH DOT BELOW
        '\xD6': '\u1EF0', # CAPITAL U WITH DOT BELOW AND HORN
        'Y':    '\u1EF4', # CAPITAL Y WITH DOT BELOW # XXX: unused because of \xCE ?
    }
    _decoding_table['\xD0'] = '\u00CF' # CAPITAL I WITH DIAERESIS
    _decoding_table['\xD1'] = '\u0110' # CAPITAL D WITH STROKE
    _decoding_table['\xD2'] = '\u1ECA' # CAPITAL I WITH DOT BELOW
    _decoding_table['\xD3'] = '\u0128' # CAPITAL I WITH TILDE
    _decoding_table['\xD4'] = '\u01A0' # CAPITAL O WITH HORN
    _decoding_table['\xD5'] = {
        'A':    '\u00C3', # CAPITAL A WITH TILDE
        'E':    '\u1EBC', # CAPITAL E WITH TILDE
        'I':    '\u0128', # CAPITAL I WITH TILDE # XXX: unused because of \xD3 ?
        'O':    '\u00D5', # CAPITAL O WITH TILDE
        '\xD4': '\u1EE0', # CAPITAL O WITH TILDE AND HORN
        'U':    '\u0168', # CAPITAL U WITH TILDE
        '\xD6': '\u1EEE', # CAPITAL U WITH TILDE AND HORN
        'Y':    '\u1EF8', # CAPITAL Y WITH TILDE
    }
    _decoding_table['\xD6'] = '\u01AF' # CAPITAL U WITH HORN
    _decoding_table['\xD7'] = '\xD7' # UNICODE
    _decoding_table['\xD8'] = {
        'A':    '\u00C0', # CAPITAL A WITH GRAVE
        'E':    '\u00C8', # CAPITAL E WITH GRAVE
        'I':    '\u00CC', # CAPITAL I WITH GRAVE # XXX: unused because of \xCC ?
        'O':    '\u00D2', # CAPITAL O WITH GRAVE
        '\xD4': '\u1EDC', # CAPITAL O WITH GRAVE AND HORN
        'U':    '\u00D9', # CAPITAL U WITH GRAVE
        '\xD6': '\u1EEA', # CAPITAL U WITH GRAVE AND HORN
        'Y':    '\u1EF2', # CAPITAL Y WITH GRAVE
    }
    _decoding_table['\xD9'] = {
        'A':    '\u00C1', # CAPITAL A WITH ACUTE
        'E':    '\u00C9', # CAPITAL E WITH ACUTE
        'I':    '\u00CD', # CAPITAL I WITH ACUTE # XXX: unused because of \xCD ?
        'O':    '\u00D3', # CAPITAL O WITH ACUTE
        '\xD4': '\u1EDA', # CAPITAL O WITH ACUTE AND HORN
        'U':    '\u00DA', # CAPITAL U WITH ACUTE
        '\xD6': '\u1EE8', # CAPITAL U WITH ACUTE AND HORN
        'Y':    '\u00DD', # CAPITAL Y WITH ACUTE
    }
    _decoding_table['\xDA'] = {
        'A':    '\u1EB2', # CAPITAL A WITH BREVE AND HOOK
    }
    _decoding_table['\xDB'] = {
        'A':    '\u1EA2', # CAPITAL A WITH HOOK
        'E':    '\u1EBA', # CAPITAL E WITH HOOK
        'I':    '\u1EC8', # CAPITAL I WITH HOOK # XXX: unused because of \xC6 ?
        'O':    '\u1ECE', # CAPITAL O WITH HOOK
        '\xD4': '\u1EDE', # CAPITAL O WITH HOOK AND HORN
        'U':    '\u1EE6', # CAPITAL U WITH HOOK
        '\xD6': '\u1EEC', # CAPITAL U WITH HOOK AND HORN
        'Y':    '\u1EF6', # CAPITAL Y WITH HOOK
    }
    _decoding_table['\xDC'] = {
        'A':    '\u1EB4', # CAPITAL A WITH BREVE AND TILDE
    }
    _decoding_table['\xDD'] = '\u00CE' # CAPITAL I WITH CIRCUMFLEX
    _decoding_table['\xDE'] = '\xDE' # UNICODE
    _decoding_table['\xDF'] = '\xDF' # UNICODE
    ### SMALL LETTERS
    _decoding_table['\xE0'] = {
        'a':    '\u1EA7', # SMALL A WITH CIRCUMFLEX AND GRAVE
        'e':    '\u1EC1', # SMALL E WITH CIRCUMFLEX AND GRAVE
        'o':    '\u1ED3', # SMALL O WITH CIRCUMFLEX AND GRAVE
    }
    _decoding_table['\xE1'] = {
        'a':    '\u1EA5', # SMALL A WITH CIRCUMFLEX AND ACUTE
        'e':    '\u1EBF', # SMALL E WITH CIRCUMFLEX AND ACUTE
        'o':    '\u1ED1', # SMALL O WITH CIRCUMFLEX AND ACUTE
    }
    _decoding_table['\xE2'] = {
        'a':    '\u00E2', # SMALL A WITH CIRCUMFLEX
        'e':    '\u00EA', # SMALL E WITH CIRCUMFLEX
        'i':    '\u00EE', # SMALL I WITH CIRCUMFLEX # XXX: unused because of \xFD ?
        'o':    '\u00F4', # SMALL O WITH CIRCUMFLEX
    }
    _decoding_table['\xE3'] = {
        'a':    '\u1EAB', # SMALL A WITH CIRCUMFLEX AND TILDE
        'e':    '\u1EC5', # SMALL E WITH CIRCUMFLEX AND TILDE
        'o':    '\u1ED7', # SMALL O WITH CIRCUMFLEX AND TILDE
    }
    _decoding_table['\xE4'] = {
        'a':    '\u1EAD', # SMALL A WITH CIRCUMFLEX AND DOT BELOW
        'e':    '\u1EC7', # SMALL E WITH CIRCUMFLEX AND DOT BELOW
        'o':    '\u1ED9', # SMALL O WITH CIRCUMFLEX AND DOT BELOW
    }
    _decoding_table['\xE5'] = {
        'a':    '\u1EA9', # SMALL A WITH CIRCUMFLEX AND HOOK
        'e':    '\u1EC3', # SMALL E WITH CIRCUMFLEX AND HOOK
        'o':    '\u1ED5', # SMALL O WITH CIRCUMFLEX AND HOOK
    }
    _decoding_table['\xE6'] = '\u1EC9' # SMALL I WITH HOOK
    _decoding_table['\xE7'] = '\xE7' # UNICODE
    _decoding_table['\xE8'] = {
        'a':    '\u1EB1', # SMALL A WITH BREVE AND GRAVE
    }
    _decoding_table['\xE9'] = {
        'a':    '\u1EAF', # SMALL A WITH BREVE AND ACUTE
    }
    _decoding_table['\xEA'] = {
        'a':    '\u0103', # SMALL A WITH BREVE
    }
    _decoding_table['\xEB'] = {
        'a':    '\u1EB7', # SMALL A WITH BREVE AND DOT BELOW
    }
    _decoding_table['\xEC'] = '\u00EC' # SMALL I WITH GRAVE
    _decoding_table['\xED'] = '\u00ED' # SMALL I WITH ACUTE
    _decoding_table['\xEE'] = '\u1EF5' # SMALL Y WITH DOT BELOW
    _decoding_table['\xEF'] = {
        'a':    '\u1EA1', # SMALL A WITH DOT BELOW
        'e':    '\u1EB9', # SMALL E WITH DOT BELOW
        'i':    '\u1ECB', # SMALL I WITH DOT BELOW # XXX: unused because of \xF2 ?
        'o':    '\u1ECD', # SMALL O WITH DOT BELOW
        '\xF4': '\u1EE3', # SMALL O WITH DOT BELOW AND HORN
        'u':    '\u1EE5', # SMALL U WITH DOT BELOW
        '\xF6': '\u1EF1', # SMALL U WITH DOT BELOW AND HORN
        'y':    '\u1EF5', # SMALL Y WITH DOT BELOW # XXX: unused because of \xEE ?
    }
    _decoding_table['\xF0'] = '\u00EF' # SMALL I WITH DIAERESIS
    _decoding_table['\xF1'] = '\u0111' # SMALL D WITH STROKE
    _decoding_table['\xF2'] = '\u1ECB' # SMALL I WITH DOT BELOW
    _decoding_table['\xF3'] = '\u0129' # SMALL I WITH TILDE
    _decoding_table['\xF4'] = '\u01A1' # SMALL O WITH HORN
    _decoding_table['\xF5'] = {
        'a':    '\u00E3', # SMALL A WITH TILDE
        'e':    '\u1EBD', # SMALL E WITH TILDE
        'i':    '\u0129', # SMALL I WITH TILDE # XXX: unused because of \xF3 ?
        'o':    '\u00F5', # SMALL O WITH TILDE
        '\xF4': '\u1EE1', # SMALL O WITH TILDE AND HORN
        'u':    '\u0169', # SMALL U WITH TILDE
        '\xF6': '\u1EEF', # SMALL U WITH TILDE AND HORN
        'y':    '\u1EF9', # SMALL Y WITH TILDE
    }
    _decoding_table['\xF6'] = '\u01B0' # SMALL U WITH HORN
    _decoding_table['\xF7'] = '\xF7' # UNICODE
    _decoding_table['\xF8'] = {
        'a':    '\u00E0', # SMALL A WITH GRAVE
        'e':    '\u00E8', # SMALL E WITH GRAVE
        'i':    '\u00EC', # SMALL I WITH GRAVE # XXX: unused because of \xEC ?
        'o':    '\u00F2', # SMALL O WITH GRAVE
        '\xF4': '\u1EDD', # SMALL O WITH GRAVE AND HORN
        'u':    '\u00F9', # SMALL U WITH GRAVE
        '\xF6': '\u1EEB', # SMALL U WITH GRAVE AND HORN
        'y':    '\u1EF3', # SMALL Y WITH GRAVE
    }
    _decoding_table['\xF9'] = {
        'a':    '\u00E1', # SMALL A WITH ACUTE
        'e':    '\u00E9', # SMALL E WITH ACUTE
        'i':    '\u00ED', # SMALL I WITH ACUTE # XXX: unused because of \xED ?
        'o':    '\u00F3', # SMALL O WITH ACUTE
        '\xF4': '\u1EDB', # SMALL O WITH ACUTE AND HORN
        'u':    '\u00FA', # SMALL U WITH ACUTE
        '\xF6': '\u1EE9', # SMALL U WITH ACUTE AND HORN
        'y':    '\u00FD', # SMALL Y WITH ACUTE
    }
    _decoding_table['\xFA'] = {
        'a':    '\u1EB3', # SMALL A WITH BREVE AND HOOK
    }
    _decoding_table['\xFB'] = {
        'a':    '\u1EA3', # SMALL A WITH HOOK
        'e':    '\u1EBB', # SMALL E WITH HOOK
        'i':    '\u1EC9', # SMALL I WITH HOOK # XXX: unused because of \xE6 ?
        'o':    '\u1ECF', # SMALL O WITH HOOK
        '\xF4': '\u1EDF', # SMALL O WITH HOOK AND HORN
        'u':    '\u1EE7', # SMALL U WITH HOOK
        '\xF6': '\u1EED', # SMALL U WITH HOOK AND HORN
        'y':    '\u1EF7', # SMALL Y WITH HOOK
    }
    _decoding_table['\xFC'] = {
        'a':    '\u1EB5', # SMALL A WITH BREVE AND TILDE
    }
    _decoding_table['\xFD'] = '\u00EE' # SMALL I WITH CIRCUMFLEX
    _decoding_table['\xFE'] = '\xFE' # UNICODE
    _decoding_table['\xFF'] = '\u1EF5' # SMALL Y WITH DOT BELOW
    ### SMALL LETTERS ACCENTS APPLIED ON CAPITALS LETTERS (!?) # seen in use...
    for i in range(0xE0, 0xFF):
        if type(_decoding_table[chr(i)]) == dict:
            _decoding_table[chr(i)].update(_decoding_table[chr(i-0x20)])
    ###
    return _decoding_table

_vni_secondhalf_decoding_table = _create_vni_secondhalf_decoding_table()

def vni_decode(input, errors='strict'):
    assert errors == 'strict'
    output = ''
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
    _encoding_table['\u00C0'] = 'A\xD8'
    # FIXME: to continue...
    output = ''
    for c in input:
        if c in _encoding_table:
            output += _encoding_table[c]
        else:
            output += c
    return (output, len(input))

