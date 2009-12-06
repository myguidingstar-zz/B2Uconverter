# -*- coding: utf-8 -*-
"""
This is the UNO extension for OpenOffice.org from the B2UConverter project.
Copyright ©2009  Ministry of Science and Technology of Vietnam
License: GNU Lesser General Public License version 2.1
Authors: Jean Christophe André, Lê Quốc Thái, Võ Đức Phương
"""

import sys
import logging
import traceback

_settings = {
  "Debug": False,
  "RemoveDiacritics": False,
  "VNIHacks": False,
}

#############################################################################
# PART 1 : codecs registration
#############################################################################

import codecs

# codecs.charmap_build lacks in the Python 2.3.4 bundled with Windows's OOo
if not 'charmap_build' in codecs.__dict__:
    # this code has been "stolen" from Python 2.5 codecs.py
    def _encoding_map_from_decoding_table(table):
        m = {}
        for k,v in table.items():
            if not v in m:
                m[v] = k
            else:
                m[v] = None
        return m

    codecs.charmap_build = _encoding_map_from_decoding_table

#============================================================================
# codec 'vntime_tcvn': kind of TCVN 5712:1993 VN3 (with CP1252 additions)
#============================================================================

_VnTime_TCVN_decoding_table = (
    u'\x00'	#  0x00 -> NULL (NUL)
    u'\x01'	#  0x01
    u'\x02'	#  0x02
    u'\x03'	#  0x03 -> END OF TEXT
    u'\x04'	#  0x04
    u'\x05'	#  0x05
    u'\x06'	#  0x06
    u'\x07'	#  0x07 -> BELL (BEL)
    u'\x08'	#  0x08 -> BACKSPACE (BS)
    u'\x09'	#  0x09 -> CHARACTER TABULATION (HT)
    u'\x0A'	#  0x0a -> LINE FEED (LF)
    u'\x0B'	#  0x0b -> LINE TABULATION (VT)
    u'\x0C'	#  0x0c -> FORM FEED (FF)
    u'\x0D'	#  0x0d -> CARRIAGE RETURN (CR)
    u'\x0E'	#  0x0e -> SHIFT OUT (SO)
    u'\x0F'	#  0x0f -> SHIFT IN (SI)
    u'\x10'	#  0x10 -> DATA LINK ESCAPE (DLE)
    u'\x11'	#  0x11
    u'\x12'	#  0x12
    u'\x13'	#  0x13
    u'\x14'	#  0x14
    u'\x15'	#  0x15
    u'\x16'	#  0x16
    u'\x17'	#  0x17
    u'\x18'	#  0x18 -> CANCEL (CAN)
    u'\x19'	#  0x19 -> END OF MEDIUM (EM)
    u'\x1A'	#  0x1a -> SUBSTITUTE (SUB)
    u'\x1B'	#  0x1b -> ESCAPE (ESC)
    u'\x1C'	#  0x1c -> FILE SEPARATOR (IS4)
    u'\x1D'	#  0x1d -> GROUP SEPARATOR (IS3)
    u'\x1E'	#  0x1e -> RECORD SEPARATOR (IS2)
    u'\x1F'	#  0x1f -> UNIT SEPARATOR (IS1)
    u' '	#  0x20 -> SPACE
    u'!'	#  0x21 -> EXCLAMATION MARK
    u'"'	#  0x22 -> QUOTATION MARK
    u'#'	#  0x23 -> NUMBER SIGN
    u'$'	#  0x24 -> DOLLAR SIGN
    u'%'	#  0x25 -> PERCENT SIGN
    u'&'	#  0x26 -> AMPERSAND
    u"'"        #  0x27 -> APOSTROPHE
    u'('	#  0x28 -> LEFT PARENTHESIS
    u')'	#  0x29 -> RIGHT PARENTHESIS
    u'*'	#  0x2A -> ASTERISK
    u'+'	#  0x2B -> PLUS SIGN
    u','	#  0x2C -> COMMA
    u'-'	#  0x2D -> HYPHEN-MINUS
    u'.'	#  0x2E -> FULL STOP
    u'/'	#  0x2F -> SOLIDUS
    u'0'	#  0x30 -> DIGIT ZERO
    u'1'	#  0x31 -> DIGIT ONE
    u'2'	#  0x32 -> DIGIT TWO
    u'3'	#  0x33 -> DIGIT THREE
    u'4'	#  0x34 -> DIGIT FOUR
    u'5'	#  0x35 -> DIGIT FIVE
    u'6'	#  0x36 -> DIGIT SIX
    u'7'	#  0x37 -> DIGIT SEVEN
    u'8'	#  0x38 -> DIGIT EIGHT
    u'9'	#  0x39 -> DIGIT NINE
    u':'	#  0x3A -> COLON
    u';'	#  0x3B -> SEMICOLON
    u'<'	#  0x3C -> LESS-THAN SIGN
    u'='	#  0x3D -> EQUALS SIGN
    u'>'	#  0x3E -> GREATER-THAN SIGN
    u'?'	#  0x3F -> QUESTION MARK
    u'@'	#  0x40 -> COMMERCIAL AT
    u'A'	#  0x41 -> LATIN CAPITAL LETTER A
    u'B'	#  0x42 -> LATIN CAPITAL LETTER B
    u'C'	#  0x43 -> LATIN CAPITAL LETTER C
    u'D'	#  0x44 -> LATIN CAPITAL LETTER D
    u'E'	#  0x45 -> LATIN CAPITAL LETTER E
    u'F'	#  0x46 -> LATIN CAPITAL LETTER F
    u'G'	#  0x47 -> LATIN CAPITAL LETTER G
    u'H'	#  0x48 -> LATIN CAPITAL LETTER H
    u'I'	#  0x49 -> LATIN CAPITAL LETTER I
    u'J'	#  0x4A -> LATIN CAPITAL LETTER J
    u'K'	#  0x4B -> LATIN CAPITAL LETTER K
    u'L'	#  0x4C -> LATIN CAPITAL LETTER L
    u'M'	#  0x4D -> LATIN CAPITAL LETTER M
    u'N'	#  0x4E -> LATIN CAPITAL LETTER N
    u'O'	#  0x4F -> LATIN CAPITAL LETTER O
    u'P'	#  0x50 -> LATIN CAPITAL LETTER P
    u'Q'	#  0x51 -> LATIN CAPITAL LETTER Q
    u'R'	#  0x52 -> LATIN CAPITAL LETTER R
    u'S'	#  0x53 -> LATIN CAPITAL LETTER S
    u'T'	#  0x54 -> LATIN CAPITAL LETTER T
    u'U'	#  0x55 -> LATIN CAPITAL LETTER U
    u'V'	#  0x56 -> LATIN CAPITAL LETTER V
    u'W'	#  0x57 -> LATIN CAPITAL LETTER W
    u'X'	#  0x58 -> LATIN CAPITAL LETTER X
    u'Y'	#  0x59 -> LATIN CAPITAL LETTER Y
    u'Z'	#  0x5A -> LATIN CAPITAL LETTER Z
    u'['	#  0x5B -> LEFT SQUARE BRACKET
    u'\\'	#  0x5C -> REVERSE SOLIDUS
    u']'	#  0x5D -> RIGHT SQUARE BRACKET
    u'^'	#  0x5E -> CIRCUMFLEX ACCENT
    u'_'	#  0x5F -> LOW LINE
    u'`'	#  0x60 -> GRAVE ACCENT
    u'a'	#  0x61 -> LATIN SMALL LETTER A
    u'b'	#  0x62 -> LATIN SMALL LETTER B
    u'c'	#  0x63 -> LATIN SMALL LETTER C
    u'd'	#  0x64 -> LATIN SMALL LETTER D
    u'e'	#  0x65 -> LATIN SMALL LETTER E
    u'f'	#  0x66 -> LATIN SMALL LETTER F
    u'g'	#  0x67 -> LATIN SMALL LETTER G
    u'h'	#  0x68 -> LATIN SMALL LETTER H
    u'i'	#  0x69 -> LATIN SMALL LETTER I
    u'j'	#  0x6A -> LATIN SMALL LETTER J
    u'k'	#  0x6B -> LATIN SMALL LETTER K
    u'l'	#  0x6C -> LATIN SMALL LETTER L
    u'm'	#  0x6D -> LATIN SMALL LETTER M
    u'n'	#  0x6E -> LATIN SMALL LETTER N
    u'o'	#  0x6F -> LATIN SMALL LETTER O
    u'p'	#  0x70 -> LATIN SMALL LETTER P
    u'q'	#  0x71 -> LATIN SMALL LETTER Q
    u'r'	#  0x72 -> LATIN SMALL LETTER R
    u's'	#  0x73 -> LATIN SMALL LETTER S
    u't'	#  0x74 -> LATIN SMALL LETTER T
    u'u'	#  0x75 -> LATIN SMALL LETTER U
    u'v'	#  0x76 -> LATIN SMALL LETTER V
    u'w'	#  0x77 -> LATIN SMALL LETTER W
    u'x'	#  0x78 -> LATIN SMALL LETTER X
    u'y'	#  0x79 -> LATIN SMALL LETTER Y
    u'z'	#  0x7A -> LATIN SMALL LETTER Z
    u'{'	#  0x7B -> LEFT CURLY BRACKET
    u'|'	#  0x7C -> VERTICAL LINE
    u'}'	#  0x7D -> RIGHT CURLY BRACKET
    u'~'	#  0x7E -> TILDE
    u'\x7F'	#  0x7f -> DELETE (DEL)
    u'\x80'	#  0x80
    u'\x81'	#  0x81
    u'\x82'	#  0x82
    u'\x83'	#  0x83
    u'\x84'	#  0x84
    u'\u2026'	#  0x85 -> HORIZONTAL ELLIPSIS
    u'\xC7'	#  0x86 -> LATIN CAPITAL LETTER C WITH CEDILLA
    u'\x87'	#  0x87
    u'\xCB'	#  0x88 -> LATIN CAPITAL LETTER E WITH DIAERESIS
    u'\xCA'	#  0x89 -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    u'\xCF'	#  0x8a -> LATIN CAPITAL LETTER I WITH DIAERESIS
    u'\xCE'	#  0x8b -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    u'\x8C'	#  0x8c
    u'\x8D'	#  0x8d
    u'\x8E'	#  0x8e
    u'\x8F'	#  0x8f
    u'\x90'	#  0x90
    u'\u2018'	#  0x91 -> LEFT SINGLE QUOTATION MARK
    u'\u2019'	#  0x92 -> RIGHT SINGLE QUOTATION MARK
    u'\u201c'	#  0x93 -> LEFT DOUBLE QUOTATION MARK
    u'\u201d'	#  0x94 -> RIGHT DOUBLE QUOTATION MARK
    u'\u2022'	#  0x95 -> BULLET
    u'\u2013'	#  0x96 -> EN DASH
    u'\u2014'	#  0x97 -> EM DASH
    u'\x98'	#  0x98
    u'\x99'	#  0x99
    u'\xDC'	#  0x9a -> LATIN CAPITAL LETTER U WITH DIAERESIS
    u'\xDB'	#  0x9b -> LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    u'\x9C'	#  0x9c
    u'\x9D'	#  0x9d
    u'\x9E'	#  0x9e
    u'\x9F'	#  0x9f
    u'\xA0'	#  0xa0 -> NO-BREAK SPACE
    u'\u0102'	#  0xa1 -> LATIN CAPITAL LETTER A WITH BREVE
    u'\xC2'	#  0xa2 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    u'\xCA'	#  0xa3 -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    u'\xD4'	#  0xa4 -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    u'\u01A0'	#  0xa5 -> LATIN CAPITAL LETTER O WITH HORN
    u'\u01AF'	#  0xa6 -> LATIN CAPITAL LETTER U WITH HORN
    u'\u0110'	#  0xa7 -> LATIN CAPITAL LETTER D WITH STROKE
    u'\u0103'	#  0xa8 -> LATIN SMALL LETTER A WITH BREVE
    u'\xE2'	#  0xa9 -> LATIN SMALL LETTER A WITH CIRCUMFLEX
    u'\xEA'	#  0xaa -> LATIN SMALL LETTER E WITH CIRCUMFLEX
    u'\xF4'	#  0xab -> LATIN SMALL LETTER O WITH CIRCUMFLEX
    u'\u01A1'	#  0xac -> LATIN SMALL LETTER O WITH HORN
    u'\u01B0'	#  0xad -> LATIN SMALL LETTER U WITH HORN
    u'\u0111'	#  0xae -> LATIN SMALL LETTER D WITH STROKE
    u'\xAF'	#  0xaf
    u'\xB0'	#  0xb0
    u'\xB1'	#  0xb1
    u'\xB2'	#  0xb2
    u'\xB3'	#  0xb3
    u'\xB4'	#  0xb4
    u'\xE0'	#  0xb5 -> LATIN SMALL LETTER A WITH GRAVE
    u'\u1EA3'	#  0xb6 -> LATIN SMALL LETTER A WITH HOOK ABOVE
    u'\xE3'	#  0xb7 -> LATIN SMALL LETTER A WITH TILDE
    u'\xE1'	#  0xb8 -> LATIN SMALL LETTER A WITH ACUTE
    u'\u1EA1'	#  0xb9 -> LATIN SMALL LETTER A WITH DOT BELOW
    u'\xBA'	#  0xba
    u'\u1EB1'	#  0xbb -> LATIN SMALL LETTER A WITH BREVE AND GRAVE
    u'\u1EB3'	#  0xbc -> LATIN SMALL LETTER A WITH BREVE AND HOOK ABOVE
    u'\u1EB5'	#  0xbd -> LATIN SMALL LETTER A WITH BREVE AND TILDE
    u'\u1EAF'	#  0xbe -> LATIN SMALL LETTER A WITH BREVE AND ACUTE
    u'\xBF'	#  0xbf
    u'\u1EBB'	#  0xc0 -> LATIN SMALL LETTER E WITH HOOK ABOVE
    u'\u1EBD'	#  0xc1 -> LATIN SMALL LETTER E WITH TILDE
    u'\u1EB9'	#  0xc2 -> LATIN SMALL LETTER E WITH DOT BELOW
    u'\xEB'	#  0xc3 -> LATIN SMALL LETTER E WITH DIAERESIS
    u'\u0192'	#  0xc4 -> LATIN SMALL LETTER F WITH HOOK
    u'\xC5'	#  0xc5
    u'\u1EB7'	#  0xc6 -> LATIN SMALL LETTER A WITH BREVE AND DOT BELOW
    u'\u1EA7'	#  0xc7 -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND GRAVE
    u'\u1EA9'	#  0xc8 -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE
    u'\u1EAB'	#  0xc9 -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE
    u'\u1EA5'	#  0xca -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND ACUTE
    u'\u1EAD'	#  0xcb -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND DOT BELOW
    u'\xE8'	#  0xcc -> LATIN SMALL LETTER E WITH GRAVE
    u'\xCD'	#  0xcd
    u'\u1EBB'	#  0xce -> LATIN SMALL LETTER E WITH HOOK ABOVE
    u'\u1EBD'	#  0xcf -> LATIN SMALL LETTER E WITH TILDE
    u'\xE9'	#  0xd0 -> LATIN SMALL LETTER E WITH ACUTE
    u'\u1EB9'	#  0xd1 -> LATIN SMALL LETTER E WITH DOT BELOW
    u'\u1EC1'	#  0xd2 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND GRAVE
    u'\u1EC3'	#  0xd3 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE
    u'\u1EC5'	#  0xd4 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND TILDE
    u'\u1EBF'	#  0xd5 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND ACUTE
    u'\u1EC7'	#  0xd6 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND DOT BELOW
    u'\xEC'	#  0xd7 -> LATIN SMALL LETTER I WITH GRAVE
    u'\u1EC9'	#  0xd8 -> LATIN SMALL LETTER I WITH HOOK ABOVE
    u'\xD9'	#  0xd9
    u'\xEF'	#  0xda -> LATIN SMALL LETTER I WITH DIAERESIS
    u'\xEE'	#  0xdb -> LATIN SMALL LETTER I WITH CIRCUMFLEX
    u'\u0129'	#  0xdc -> LATIN SMALL LETTER I WITH TILDE
    u'\xED'	#  0xdd -> LATIN SMALL LETTER I WITH ACUTE
    u'\u1ECB'	#  0xde -> LATIN SMALL LETTER I WITH DOT BELOW
    u'\xF2'	#  0xdf -> LATIN SMALL LETTER O WITH GRAVE
    u'\xE0'	#  0xe0
    u'\u1ECF'	#  0xe1 -> LATIN SMALL LETTER O WITH HOOK ABOVE
    u'\xF5'	#  0xe2 -> LATIN SMALL LETTER O WITH TILDE
    u'\xF3'	#  0xe3 -> LATIN SMALL LETTER O WITH ACUTE
    u'\u1ECD'	#  0xe4 -> LATIN SMALL LETTER O WITH DOT BELOW
    u'\u1ED3'	#  0xe5 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND GRAVE
    u'\u1ED5'	#  0xe6 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE
    u'\u1ED7'	#  0xe7 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND TILDE
    u'\u1ED1'	#  0xe8 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND ACUTE
    u'\u1ED9'	#  0xe9 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND DOT BELOW
    u'\u1EDD'	#  0xea -> LATIN SMALL LETTER O WITH HORN AND GRAVE
    u'\u1EDF'	#  0xeb -> LATIN SMALL LETTER O WITH HORN AND HOOK ABOVE
    u'\u1EE1'	#  0xec -> LATIN SMALL LETTER O WITH HORN AND TILDE
    u'\u1EDB'	#  0xed -> LATIN SMALL LETTER O WITH HORN AND ACUTE
    u'\u1EE3'	#  0xee -> LATIN SMALL LETTER O WITH HORN AND DOT BELOW
    u'\xF9'	#  0xef -> LATIN SMALL LETTER U WITH GRAVE
    u'\xF0'	#  0xf0
    u'\u1EE7'	#  0xf1 -> LATIN SMALL LETTER U WITH HOOK ABOVE
    u'\u0169'	#  0xf2 -> LATIN SMALL LETTER U WITH TILDE
    u'\xFA'	#  0xf3 -> LATIN SMALL LETTER U WITH ACUTE
    u'\u1EE5'	#  0xf4 -> LATIN SMALL LETTER U WITH DOT BELOW
    u'\u1EEB'	#  0xf5 -> LATIN SMALL LETTER U WITH HORN AND GRAVE
    u'\u1EED'	#  0xf6 -> LATIN SMALL LETTER U WITH HORN AND HOOK ABOVE
    u'\u1EEF'	#  0xf7 -> LATIN SMALL LETTER U WITH HORN AND TILDE
    u'\u1EE9'	#  0xf8 -> LATIN SMALL LETTER U WITH HORN AND ACUTE
    u'\u1EF1'	#  0xf9 -> LATIN SMALL LETTER U WITH HORN AND DOT BELOW
    u'\u1EF3'	#  0xfa -> LATIN SMALL LETTER Y WITH GRAVE
    u'\u1EF7'	#  0xfb -> LATIN SMALL LETTER Y WITH HOOK ABOVE
    u'\u1EF9'	#  0xfc -> LATIN SMALL LETTER Y WITH TILDE
    u'\xFD'	#  0xfd -> LATIN SMALL LETTER Y WITH ACUTE
    u'\u1EF5'	#  0xfe -> LATIN SMALL LETTER Y WITH DOT BELOW
    u'\xFF'	#  0xff
)

_VnTime_TCVN_encoding_map = codecs.charmap_build(_VnTime_TCVN_decoding_table)

def _VnTime_TCVN_encode(input, errors='strict'):
    return codecs.charmap_encode(input, errors, _VnTime_TCVN_encoding_map)

def _VnTime_TCVN_decode(input, errors='strict'):
    return codecs.charmap_decode(input, errors, _VnTime_TCVN_decoding_table)

#============================================================================
# codec 'vni': from VNISoft company
#============================================================================

def _create_VNI_secondhalf_decoding_table():
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

_VNI_secondhalf_decoding_table = _create_VNI_secondhalf_decoding_table()

def _VNI_decode(input, errors='strict'):
    assert errors == 'strict'
    output = u''
    _decoding_table = _VNI_secondhalf_decoding_table
    for i in range(len(input)):
        c = input[i]
        if ord(c) < 0x80:
            output += c
        elif type(_decoding_table[c]) == dict:
            try:
                output = output[:-1] + _decoding_table[c][input[i-1]]
            except KeyError:
                # FIXME: finish exception catch here (= bad encoding data)
                raise ValueError, u"bad encoded data: " + input[i:]
        else:
            output += _decoding_table[c]
    return (output, len(input))

#============================================================================
# codec 'cp1252' from Microsoft
#============================================================================

def _create_cp1252_to_unicode_map():
    cp1252_begin = ''.join(map(unichr,range(0,0x80)))
    cp1252_specials = (
        u'\u20ac'   #  0x80 -> EURO SIGN
        u'\x81'     #  0x81
        u'\u201a'   #  0x82 -> SINGLE LOW-9 QUOTATION MARK
        u'\u0192'   #  0x83 -> LATIN SMALL LETTER F WITH HOOK
        u'\u201e'   #  0x84 -> DOUBLE LOW-9 QUOTATION MARK
        u'\u2026'   #  0x85 -> HORIZONTAL ELLIPSIS
        u'\u2020'   #  0x86 -> DAGGER
        u'\u2021'   #  0x87 -> DOUBLE DAGGER
        u'\u02c6'   #  0x88 -> MODIFIER LETTER CIRCUMFLEX ACCENT
        u'\u2030'   #  0x89 -> PER MILLE SIGN
        u'\u0160'   #  0x8A -> LATIN CAPITAL LETTER S WITH CARON
        u'\u2039'   #  0x8B -> SINGLE LEFT-POINTING ANGLE QUOTATION MARK
        u'\u0152'   #  0x8C -> LATIN CAPITAL LIGATURE OE
        u'\x8D'     #  0x8D
        u'\u017d'   #  0x8E -> LATIN CAPITAL LETTER Z WITH CARON
        u'\x8F'     #  0x8F
        u'\x90'     #  0x90
        u'\u2018'   #  0x91 -> LEFT SINGLE QUOTATION MARK
        u'\u2019'   #  0x92 -> RIGHT SINGLE QUOTATION MARK
        u'\u201c'   #  0x93 -> LEFT DOUBLE QUOTATION MARK
        u'\u201d'   #  0x94 -> RIGHT DOUBLE QUOTATION MARK
        u'\u2022'   #  0x95 -> BULLET
        u'\u2013'   #  0x96 -> EN DASH
        u'\u2014'   #  0x97 -> EM DASH
        u'\u02dc'   #  0x98 -> SMALL TILDE
        u'\u2122'   #  0x99 -> TRADE MARK SIGN
        u'\u0161'   #  0x9A -> LATIN SMALL LETTER S WITH CARON
        u'\u203a'   #  0x9B -> SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
        u'\u0153'   #  0x9C -> LATIN SMALL LIGATURE OE
        u'\x9D'     #  0x9D
        u'\u017e'   #  0x9E -> LATIN SMALL LETTER Z WITH CARON
        u'\u0178'   #  0x9F -> LATIN CAPITAL LETTER Y WITH DIAERESIS
    )
    cp1252_end = ''.join(map(unichr,range(0xA0,0x100)))
    return cp1252_begin + cp1252_specials + cp1252_end

cp1252_map = _create_cp1252_to_unicode_map()

#============================================================================
# register new/internal codecs
#============================================================================

def _privateCodecSearch(name):
    if name == 'internal_vntime_tcvn':
        return (_VnTime_TCVN_encode, _VnTime_TCVN_decode, None, None)
    if name == 'internal_vni':
        return (None, _VNI_decode, None, None)
    return None

codecs.register(_privateCodecSearch)

#####################################################################
# PART 2 : re-encoding processing
#####################################################################

_vietnamese_diacritics = (
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
_without_vietnamese_diacritics = (
    u'aAaAdDeEoOoOuU'
    u'aAaAaAaAaAaAaAaAaAaAaAaAaAaAaA'
    u'eEeEeEeEeEeEeEeEeEeEiIiIiIiIiI'
    u'oOoOoOoOoOoOoOoOoOoOoOoOoOoOoO'
    u'uUuUuUuUuUuUuUuUuUuUyYyYyYyYyY'
)

def removeDiacritics(str):
    global _vietnamese_diacritics, _without_vietnamese_diacritics
    result = u''
    for c in str:
        idx = _vietnamese_diacritics.find(c)
        if idx >= 0:
            c = _without_vietnamese_diacritics[idx]
        result += c
    return result

def convertVietnameseString(str, real, upper=False):
    global _settings
    if not str: return u''
    result = u''

    logging.debug("convertString(%s)", str)
    # compensate for (supposedly) some VNI encoder's bug(s)
    if _settings["VNIHacks"] and real == 'internal_vni':
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
        while (j < len(str) and str[j] in cp1252_map): j += 1
        segment = str[i:j].encode('cp1252').decode(real)
        if _settings["RemoveDiacritics"]:
            segment = removeDiacritics(segment)
        if upper: segment = segment.upper()
        result += segment
        # find Unicode content and keep it
        # XXX: could use this information to detect text already converted!
        k = j
        while (k < len(str) and ord(str[k]) >= 256): k += 1
        result += str[j:k]
        i = k

    # compensate for OOo's bug on MS-Office's soft hyphen importation
    if real == 'internal_vntime_tcvn':
        # luckily there is no Vietnamese word with two consecutive 'ư'
        while (result.find(u'\u01B0\u01B0') >= 0):
            result = result.replace(u'\u01B0\u01B0', u'\u01B0')
    elif real == 'internal_vntime_vnlabs':
        # luckily there is no Vietnamese word with two consecutive 'ạ'
        while (result.find(u'\u1EA1\u1EA1') >= 0):
            result = result.replace(u'\u1EA1\u1EA1', u'\u1EA1')
    logging.debug("convertString -> %s", result)
    return result

#####################################################################
# PART 3 : OpenOffice processing
#####################################################################

import uno
import unohelper
from com.sun.star.lang import Locale

def processTextPortion(text):
    old = text.getString()
    new = None
    properties = {}
    logging.debug("processing text portion [%s]", old)
    fontName = text.getPropertyValue("CharFontName")
    # XXX: sometime fontName==None ?!? see test file from IFI
    # XXX: manage situation where the fontname has got wrong letter case
    #      (eg: .vntime for .VnTime)
    if not fontName: return # XXX wrong wrong wrong
    if fontName.startswith('.Vn'):
        upper = fontName.endswith('H')
        new = convertVietnameseString(old, 'internal_vntime_tcvn', upper=upper)
        if fontName.startswith('.VnCourier New'):
            properties["CharFontName"] = "Courier New"
        elif fontName.startswith('.VnArial'):
            properties["CharFontName"] = "Arial"
        else:
            properties["CharFontName"] = "Times New Roman"
        # FIXME: could it be some English text in Vietnamese font?
        properties["CharLocale"] = Locale('vi', 'VN', '')
    elif fontName.startswith('VNI'):
        new = convertVietnameseString(old, 'internal_vni')
        if fontName == 'VNI-Couri':
            properties["CharFontName"] = "Courier New"
        elif fontName == 'VNI-Arial':
            properties["CharFontName"] = "Arial"
        else:
            properties["CharFontName"] = "Times New Roman"
        # FIXME: could it be some English text in Vietnamese font?
        properties["CharLocale"] = Locale('vi', 'VN', '')

    # FIXME: using setString makes loose all properties!!!
    # FIXME: may be use text.getPropertyValues() & text.setPropertyValues ??
    # TODO: - save _all_ properties into an array
    # TODO: - push additionnal properties if any
    # TODO: - update the text string content with setString
    # TODO: - reset properties from properties array
    if new and new != old:
        text.setString(new)
        #text.String = new
    for k,v in properties.items():
        text.setPropertyValue(k, v)

def processTextParagraph(paragraph):
    #logging.debug("dir(paragraph) = ( %s )", ' '.join(dir(paragraph)))
    #logging.debug("  services: %s", ', '.join(paragraph.getSupportedServiceNames()))
    #logging.debug("  hasElements: %s", paragraph.hasElements())
    enum = paragraph.createEnumeration()
    #logging.debug("dir(enum) = ( %s )", ' '.join(dir(enum)))
    # reverse process all portions, since text boundaries
    # get altered when using setString with a longer string
    portions = []
    while (enum.hasMoreElements()):
        portions.append(enum.nextElement())
    for textPortion in reversed(portions):
        type = textPortion.getPropertyValue("TextPortionType")
        logging.debug("processing text paragraph element (type %s) [%s]",
                                            type, textPortion.getString())
        if type == 'Text':
            processTextPortion(textPortion)
        elif type == 'SoftPageBreak':
            pass
        elif type == 'Frame':
            # logging.debug("found a Frame (ignored, parsed later)")
            pass
        else:
            logging.warning("unknown text portion type '%s'", type)

def processTextTable(table):
    for name in table.getCellNames():
        cell = table.getCellByName(name)
        processText(cell)

def processText(text):
    enum = text.createEnumeration()
    while (enum.hasMoreElements()):
        paragraph = enum.nextElement()
        if paragraph.supportsService("com.sun.star.text.TextTable"):
            logging.debug("processing text element (table)")
            # this is a table "paragraph"
            processTextTable(paragraph)
        else:
            logging.debug("processing text element [%s]", paragraph.getString())
            # this is a text paragraph
            processTextParagraph(paragraph)

def processShape(shape):
    type = shape.getShapeType()
    if type == "com.sun.star.drawing.TextShape":
        processText(shape)
    elif type == "com.sun.star.drawing.GroupShape":
        for index in range(shape.getCount()):
            processShape(shape.getByIndex(index))
    #elif type == "FrameShape":
    #    pass
    #elif type == "com.sun.star.drawing.LineShape":
    #    pass
    #elif type == "com.sun.star.drawing.RectangleShape":
    #    pass
    elif type == "com.sun.star.drawing.CustomShape":
        processText(shape)
    elif type == "com.sun.star.presentation.TitleTextShape":
        processText(shape)
    elif type == "com.sun.star.presentation.SubtitleShape":
        processText(shape)
    elif type == "com.sun.star.presentation.OutlinerShape":
        processText(shape)
    else:
        logging.warning("unknown shape type '%s' for object named '%s'",
                                                        type, shape.Name)

def processPageStyle(pageStyle):
    logging.debug("processing page style '%s'", pageStyle.Name)
    if pageStyle.HeaderIsOn:
        if pageStyle.HeaderText:
            processText(pageStyle.HeaderText)
        if pageStyle.HeaderTextLeft:
            processText(pageStyle.HeaderTextLeft)
        if pageStyle.HeaderTextRight:
            processText(pageStyle.HeaderTextRight)
    if pageStyle.FooterIsOn:
        if pageStyle.FooterText:
            processText(pageStyle.FooterText)
        if pageStyle.FooterTextLeft:
            processText(pageStyle.FooterTextLeft)
        if pageStyle.FooterTextRight:
            processText(pageStyle.FooterTextRight)

def processTextDocument(doc):
    # convert text body
    text = doc.Text
    processText(text)
    # convert text frames
    frames = doc.getTextFrames()
    for index in range(frames.getCount()):
        frame = frames.getByIndex(index)
        processText(frame)
    # convert text shapes (in draw pages)
    drawPages = doc.getDrawPage()
    for index in range(drawPages.getCount()):
        drawPage = drawPages.getByIndex(index)
        processShape(drawPage)
    # convert text footnotes
    footnotes = doc.getFootnotes()
    for index in range(footnotes.getCount()):
        footnote = footnotes.getByIndex(index)
        logging.warning("found footnote '%s' (ignored)", footnote.Name)
        #logging.debug("dir(footnote) : %s", "|".join(dir(footnote)))
        #processText(footnote)
    # convert text sections
    sections = doc.getTextSections()
    #logging.debug("dir(sections) : %s", "|".join(dir(sections)))
    for index in range(sections.getCount()):
        section = sections.getByIndex(index)
        logging.warning("found section '%s' (ignored)", section.Name)
        #logging.debug("dir(section) : %s", "|".join(dir(section)))
        #processText(section)
    # CONVERT PAGE STYLES (mainly for text header & footer)
    pageStyles = doc.getStyleFamilies().getByName("PageStyles")
    for index in range(pageStyles.getCount()):
        pageStyle = pageStyles.getByIndex(index)
        logging.info("found page style '%s'", pageStyle.Name)
        if pageStyle.isInUse():
            processPageStyle(pageStyle)

def processSheet(sheet):
    cursor = sheet.createCursor()
    cursor.gotoEndOfUsedArea(False)
    cursor.gotoStartOfUsedArea(True)
    rangeAddress = cursor.getRangeAddress()
    rows = rangeAddress.EndRow - rangeAddress.StartRow + 1
    columns = rangeAddress.EndColumn - rangeAddress.StartColumn + 1
    logging.debug("rows=%s & columns=%s", str(rows), str(columns))
    for row in range(rows):
        for column in range(columns):
            logging.debug("cell(%s,%s)", str(column), str(row))
            cell = cursor.getCellByPosition(column, row)
            logging.debug("dir(cell) = ( %s )", ' '.join(dir(cell)))
            processText(cell.Text)

def processSpreadsheetDocument(doc):
    # disable automatic-calculation during process
    autoCalc = doc.isAutomaticCalculationEnabled()
    if autoCalc: doc.enableAutomaticCalculation(False)
    # process all sheets
    enum = doc.getSheets().createEnumeration()
    while (enum.hasMoreElements()):
        sheet = enum.nextElement()
        processSheet(sheet)
    # re-enable automatic-calculation if required
    if autoCalc: doc.enableAutomaticCalculation(True)

def processDrawPresentationDocument(doc):
    # process all pages
    drawPages = doc.getDrawPages()
    for index in range(drawPages.getCount()):
        drawPage = drawPages.getByIndex(index)
        # convert page body
        logging.info("converting draw page '%s'", drawPage.getName())
        for index in range(drawPage.getCount()):
            draw = drawPage.getByIndex(index)
            processShape(draw)
        # FIXME: should process text in drawPage.getNotesPage() too
        # convert page name
        # FIXME: should not arbitrary convert from VnTime_TCVN
        # FIXME: should detect if name has already been converted
        drawPage.setName(convertVietnameseString(drawPage.getName(), 'internal_vntime_tcvn'))

def processDocument(doc):
    # XXX: check if it really works
    #doc.RecordChanges = False

    if doc.supportsService("com.sun.star.text.GenericTextDocument"):
        logging.info("this is a text document")
        processTextDocument(doc)
    elif doc.supportsService("com.sun.star.sheet.SpreadsheetDocument"):
        logging.info("this is a spreadsheet document")
        processSpreadsheetDocument(doc)
    elif doc.supportsService("com.sun.star.presentation.PresentationDocument"):
        logging.info("this is a presentation document")
        processDrawPresentationDocument(doc)
    elif doc.supportsService("com.sun.star.drawing.GenericDrawingDocument"):
        logging.info("this is a drawing document")
        processDrawPresentationDocument(doc)
    else:
        logging.warning("unknown document type")

    # convert document title
    info = doc.getDocumentInfo()
    # FIXME: should not arbitrary convert from VnTime_TCVN
    # FIXME: should detect if title has already been converted
    info.Title = convertVietnameseString(info.Title, 'internal_vntime_tcvn')

    # XXX: check if it really works
    #doc.RecordChanges = True

class B2UConverterOOoParser(object):
    """OOo document parser."""

    def __init__(self):
        pass

######################################################################

def B2UConverterScript(event=False):
    """Convert all document text segments from old Vietnamese encodings and fonts to Unicode encoding and fonts."""
    return processDocument(XSCRIPTCONTEXT.getDocument())

g_exportedScripts = B2UConverterScript,

######################################################################

#from com.sun.star.awt import Rectangle
from com.sun.star.awt import WindowDescriptor
from com.sun.star.awt.WindowClass import MODALTOP
from com.sun.star.awt.VclWindowPeerAttribute import OK, DEF_OK

# Show a message box with the UNO based toolkit
def messageBox(document, message):
    #doc = XSCRIPTCONTEXT.getDocument()
    window = document.CurrentController.Frame.ContainerWindow

    aDescriptor = WindowDescriptor()
    aDescriptor.Type = MODALTOP
    aDescriptor.WindowServiceName = "infobox"
    aDescriptor.ParentIndex = -1
    aDescriptor.Parent = window
    #aDescriptor.Bounds = Rectangle()
    aDescriptor.WindowAttributes = OK

    tk = window.getToolkit()
    msgbox = tk.createWindow(aDescriptor)
    msgbox.setCaptionText("Convert to Unicode")
    msgbox.setMessageText(message)

    return msgbox.execute()

######################################################################

from com.sun.star.task import XJobExecutor

class B2UConverterJob(unohelper.Base, XJobExecutor):
    def __init__(self, context):
        self._context = context

        logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(message)s',
            filename='/tmp/b2uconverter-ooo.log', filemode='w')
        logging.info("B2UConverter loaded (Python %s)", sys.version)

        self._cfgprov = self._context.ServiceManager.createInstanceWithContext(
            "com.sun.star.configuration.ConfigurationProvider",
            self._context)
        node = uno.createUnoStruct("com.sun.star.beans.PropertyValue")
        node.Name = "nodepath"
        node.Value = "/vn.gov.oss.openoffice.B2UConverter/General"
        self._node = node
        self._cfgnames = ("Debug", "RemoveDiacritics")

    def _readconfig(self):
        global _settings
        ConfigReader = self._cfgprov.createInstanceWithArguments(
            "com.sun.star.configuration.ConfigurationAccess",
            (self._node,))
        cfgvalues = ConfigReader.getPropertyValues(self._cfgnames)
        for i in range(len(self._cfgnames)):
            _settings[self._cfgnames[i]] = cfgvalues[i]

    def convertDocument(self):
        self._readconfig()
        logging.debug("call to convertDocument")
        desktop = self._context.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", self._context)
        self._document = desktop.getCurrentComponent()
        try:
            processDocument(self._document)
            logging.info("Unicode conversion completed.")
        except:
            logging.exception("Exception during conversion:")
            raise

    def convertClipboard(self, args):
        #copy/paste from above
        self._readconfig()
        logging.debug("call to convertClipboard")
        desktop = self._context.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", self._context)
        clipboard = self._context.ServiceManager.createInstanceWithContext(
            "com.sun.star.datatransfer.clipboard.SystemClipboard",
            self._context)
        contents = clipboard.getContents()
        logging.debug("Contents:\n%s\n%s\n%s",
            "-" * 78,
            "* " + "\n* ".join(dir(contents)),
            "=" * 78)
        flavors = contents.getTransferDataFlavors()
        logging.debug("Flavors:\n%s\n%s\n%s",
            "-" * 78,
            "* " + "\n* ".join([flavor.MimeType for flavor in flavors]),
            "=" * 78)
        mimetype = \
        'application/x-openoffice-embed-source-xml;windows_formatname="Star \
         Embed Source (XML)"'
        found_flavor = None
        for flavor in contents.getTransferDataFlavors():
            if flavor.MimeType == mimetype:
                found_flavor = flavor
                break
        # No suitable flavor found, warn user that nothing has been converted
        # if found_flavor == None:
        data = contents.getTransferData(found_flavor)
        open('/tmp/clipboarddata', 'w').write(data.value)
        # Now we need to convert the data we have just received
        # There should be a better way than open it in a new window :-/

    def trigger(self, args):
        logging.debug("Trigger arguments: %s", args)
        try:
            self.convertDocument()
            if args == 'frommenu':
                messageBox(self._document, "Unicode conversion completed.")
        except:
            if args == 'frommenu':
                err = traceback.format_exc()
                messageBox(self._document, "Unicode conversion failed:\n" + err)


g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation( \
    B2UConverterJob, "vn.gov.oss.openoffice.B2UConverterJob", \
    ("com.sun.star.task.Job",),)
