""" Python Character Mapping Codec vntime_tcvn (.VnTime font - Vietnamese)
                        (kind of TCVN 5712:1993 VN3 with CP1252 additions)
    Copyright (c) 2008-2009  Jean Christophe André <jcandre@hanoilug.org>
    License: GNU Lesser General Public License version 2.1
    To enable this encoding, move this file into /usr/lib/python2.5/encodings/
"""

vntime_tcvn_decoding_table = (
    u'\x00'     #  0x00 -> NULL (NUL)
    u'\x01'     #  0x01
    u'\x02'     #  0x02
    u'\x03'     #  0x03 -> END OF TEXT
    u'\x04'     #  0x04
    u'\x05'     #  0x05
    u'\x06'     #  0x06
    u'\x07'     #  0x07 -> BELL (BEL)
    u'\x08'     #  0x08 -> BACKSPACE (BS)
    u'\x09'     #  0x09 -> CHARACTER TABULATION (HT)
    u'\x0A'     #  0x0a -> LINE FEED (LF)
    u'\x0B'     #  0x0b -> LINE TABULATION (VT)
    u'\x0C'     #  0x0c -> FORM FEED (FF)
    u'\x0D'     #  0x0d -> CARRIAGE RETURN (CR)
    u'\x0E'     #  0x0e -> SHIFT OUT (SO)
    u'\x0F'     #  0x0f -> SHIFT IN (SI)
    u'\x10'     #  0x10 -> DATA LINK ESCAPE (DLE)
    u'\x11'     #  0x11
    u'\x12'     #  0x12
    u'\x13'     #  0x13
    u'\x14'     #  0x14
    u'\x15'     #  0x15
    u'\x16'     #  0x16
    u'\x17'     #  0x17
    u'\x18'     #  0x18 -> CANCEL (CAN)
    u'\x19'     #  0x19 -> END OF MEDIUM (EM)
    u'\x1A'     #  0x1a -> SUBSTITUTE (SUB)
    u'\x1B'     #  0x1b -> ESCAPE (ESC)
    u'\x1C'     #  0x1c -> FILE SEPARATOR (IS4)
    u'\x1D'     #  0x1d -> GROUP SEPARATOR (IS3)
    u'\x1E'     #  0x1e -> RECORD SEPARATOR (IS2)
    u'\x1F'     #  0x1f -> UNIT SEPARATOR (IS1)
    u' '        #  0x20 -> SPACE
    u'!'        #  0x21 -> EXCLAMATION MARK
    u'"'        #  0x22 -> QUOTATION MARK
    u'#'        #  0x23 -> NUMBER SIGN
    u'$'        #  0x24 -> DOLLAR SIGN
    u'%'        #  0x25 -> PERCENT SIGN
    u'&'        #  0x26 -> AMPERSAND
    u"'"        #  0x27 -> APOSTROPHE
    u'('        #  0x28 -> LEFT PARENTHESIS
    u')'        #  0x29 -> RIGHT PARENTHESIS
    u'*'        #  0x2A -> ASTERISK
    u'+'        #  0x2B -> PLUS SIGN
    u','        #  0x2C -> COMMA
    u'-'        #  0x2D -> HYPHEN-MINUS
    u'.'        #  0x2E -> FULL STOP
    u'/'        #  0x2F -> SOLIDUS
    u'0'        #  0x30 -> DIGIT ZERO
    u'1'        #  0x31 -> DIGIT ONE
    u'2'        #  0x32 -> DIGIT TWO
    u'3'        #  0x33 -> DIGIT THREE
    u'4'        #  0x34 -> DIGIT FOUR
    u'5'        #  0x35 -> DIGIT FIVE
    u'6'        #  0x36 -> DIGIT SIX
    u'7'        #  0x37 -> DIGIT SEVEN
    u'8'        #  0x38 -> DIGIT EIGHT
    u'9'        #  0x39 -> DIGIT NINE
    u':'        #  0x3A -> COLON
    u';'        #  0x3B -> SEMICOLON
    u'<'        #  0x3C -> LESS-THAN SIGN
    u'='        #  0x3D -> EQUALS SIGN
    u'>'        #  0x3E -> GREATER-THAN SIGN
    u'?'        #  0x3F -> QUESTION MARK
    u'@'        #  0x40 -> COMMERCIAL AT
    u'A'        #  0x41 -> LATIN CAPITAL LETTER A
    u'B'        #  0x42 -> LATIN CAPITAL LETTER B
    u'C'        #  0x43 -> LATIN CAPITAL LETTER C
    u'D'        #  0x44 -> LATIN CAPITAL LETTER D
    u'E'        #  0x45 -> LATIN CAPITAL LETTER E
    u'F'        #  0x46 -> LATIN CAPITAL LETTER F
    u'G'        #  0x47 -> LATIN CAPITAL LETTER G
    u'H'        #  0x48 -> LATIN CAPITAL LETTER H
    u'I'        #  0x49 -> LATIN CAPITAL LETTER I
    u'J'        #  0x4A -> LATIN CAPITAL LETTER J
    u'K'        #  0x4B -> LATIN CAPITAL LETTER K
    u'L'        #  0x4C -> LATIN CAPITAL LETTER L
    u'M'        #  0x4D -> LATIN CAPITAL LETTER M
    u'N'        #  0x4E -> LATIN CAPITAL LETTER N
    u'O'        #  0x4F -> LATIN CAPITAL LETTER O
    u'P'        #  0x50 -> LATIN CAPITAL LETTER P
    u'Q'        #  0x51 -> LATIN CAPITAL LETTER Q
    u'R'        #  0x52 -> LATIN CAPITAL LETTER R
    u'S'        #  0x53 -> LATIN CAPITAL LETTER S
    u'T'        #  0x54 -> LATIN CAPITAL LETTER T
    u'U'        #  0x55 -> LATIN CAPITAL LETTER U
    u'V'        #  0x56 -> LATIN CAPITAL LETTER V
    u'W'        #  0x57 -> LATIN CAPITAL LETTER W
    u'X'        #  0x58 -> LATIN CAPITAL LETTER X
    u'Y'        #  0x59 -> LATIN CAPITAL LETTER Y
    u'Z'        #  0x5A -> LATIN CAPITAL LETTER Z
    u'['        #  0x5B -> LEFT SQUARE BRACKET
    u'\\'       #  0x5C -> REVERSE SOLIDUS
    u']'        #  0x5D -> RIGHT SQUARE BRACKET
    u'^'        #  0x5E -> CIRCUMFLEX ACCENT
    u'_'        #  0x5F -> LOW LINE
    u'`'        #  0x60 -> GRAVE ACCENT
    u'a'        #  0x61 -> LATIN SMALL LETTER A
    u'b'        #  0x62 -> LATIN SMALL LETTER B
    u'c'        #  0x63 -> LATIN SMALL LETTER C
    u'd'        #  0x64 -> LATIN SMALL LETTER D
    u'e'        #  0x65 -> LATIN SMALL LETTER E
    u'f'        #  0x66 -> LATIN SMALL LETTER F
    u'g'        #  0x67 -> LATIN SMALL LETTER G
    u'h'        #  0x68 -> LATIN SMALL LETTER H
    u'i'        #  0x69 -> LATIN SMALL LETTER I
    u'j'        #  0x6A -> LATIN SMALL LETTER J
    u'k'        #  0x6B -> LATIN SMALL LETTER K
    u'l'        #  0x6C -> LATIN SMALL LETTER L
    u'm'        #  0x6D -> LATIN SMALL LETTER M
    u'n'        #  0x6E -> LATIN SMALL LETTER N
    u'o'        #  0x6F -> LATIN SMALL LETTER O
    u'p'        #  0x70 -> LATIN SMALL LETTER P
    u'q'        #  0x71 -> LATIN SMALL LETTER Q
    u'r'        #  0x72 -> LATIN SMALL LETTER R
    u's'        #  0x73 -> LATIN SMALL LETTER S
    u't'        #  0x74 -> LATIN SMALL LETTER T
    u'u'        #  0x75 -> LATIN SMALL LETTER U
    u'v'        #  0x76 -> LATIN SMALL LETTER V
    u'w'        #  0x77 -> LATIN SMALL LETTER W
    u'x'        #  0x78 -> LATIN SMALL LETTER X
    u'y'        #  0x79 -> LATIN SMALL LETTER Y
    u'z'        #  0x7A -> LATIN SMALL LETTER Z
    u'{'        #  0x7B -> LEFT CURLY BRACKET
    u'|'        #  0x7C -> VERTICAL LINE
    u'}'        #  0x7D -> RIGHT CURLY BRACKET
    u'~'        #  0x7E -> TILDE
    u'\x7F'     #  0x7f -> DELETE (DEL)
    u'\x80'     #  0x80
    u'\x81'     #  0x81
    u'\x82'     #  0x82
    u'\x83'     #  0x83
    u'\x84'     #  0x84
    u'\u2026'   #  0x85 -> HORIZONTAL ELLIPSIS
    u'\xC7'     #  0x86 -> LATIN CAPITAL LETTER C WITH CEDILLA
    u'\x87'     #  0x87
    u'\xCB'     #  0x88 -> LATIN CAPITAL LETTER E WITH DIAERESIS
    u'\xCA'     #  0x89 -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    u'\xCF'     #  0x8a -> LATIN CAPITAL LETTER I WITH DIAERESIS
    u'\xCE'     #  0x8b -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    u'\x8C'     #  0x8c
    u'\x8D'     #  0x8d
    u'\x8E'     #  0x8e
    u'\x8F'     #  0x8f
    u'\x90'     #  0x90
    u'\u2018'   #  0x91 -> LEFT SINGLE QUOTATION MARK
    u'\u2019'   #  0x92 -> RIGHT SINGLE QUOTATION MARK
    u'\u201c'   #  0x93 -> LEFT DOUBLE QUOTATION MARK
    u'\u201d'   #  0x94 -> RIGHT DOUBLE QUOTATION MARK
    u'\u2022'   #  0x95 -> BULLET
    u'\u2013'   #  0x96 -> EN DASH
    u'\u2014'   #  0x97 -> EM DASH
    u'\x98'     #  0x98
    u'\x99'     #  0x99
    u'\xDC'     #  0x9a -> LATIN CAPITAL LETTER U WITH DIAERESIS
    u'\xDB'     #  0x9b -> LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    u'\x9C'     #  0x9c
    u'\x9D'     #  0x9d
    u'\x9E'     #  0x9e
    u'\x9F'     #  0x9f
    u'\xA0'     #  0xa0 -> NO-BREAK SPACE
    u'\u0102'   #  0xa1 -> LATIN CAPITAL LETTER A WITH BREVE
    u'\xC2'     #  0xa2 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    u'\xCA'     #  0xa3 -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    u'\xD4'     #  0xa4 -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    u'\u01A0'   #  0xa5 -> LATIN CAPITAL LETTER O WITH HORN
    u'\u01AF'   #  0xa6 -> LATIN CAPITAL LETTER U WITH HORN
    u'\u0110'   #  0xa7 -> LATIN CAPITAL LETTER D WITH STROKE
    u'\u0103'   #  0xa8 -> LATIN SMALL LETTER A WITH BREVE
    u'\xE2'     #  0xa9 -> LATIN SMALL LETTER A WITH CIRCUMFLEX
    u'\xEA'     #  0xaa -> LATIN SMALL LETTER E WITH CIRCUMFLEX
    u'\xF4'     #  0xab -> LATIN SMALL LETTER O WITH CIRCUMFLEX
    u'\u01A1'   #  0xac -> LATIN SMALL LETTER O WITH HORN
    u'\u01B0'   #  0xad -> LATIN SMALL LETTER U WITH HORN
    u'\u0111'   #  0xae -> LATIN SMALL LETTER D WITH STROKE
    u'\xAF'     #  0xaf
    u'\xB0'     #  0xb0
    u'\xB1'     #  0xb1
    u'\xB2'     #  0xb2
    u'\xB3'     #  0xb3
    u'\xB4'     #  0xb4
    u'\xE0'     #  0xb5 -> LATIN SMALL LETTER A WITH GRAVE
    u'\u1EA3'   #  0xb6 -> LATIN SMALL LETTER A WITH HOOK ABOVE
    u'\xE3'     #  0xb7 -> LATIN SMALL LETTER A WITH TILDE
    u'\xE1'     #  0xb8 -> LATIN SMALL LETTER A WITH ACUTE
    u'\u1EA1'   #  0xb9 -> LATIN SMALL LETTER A WITH DOT BELOW
    u'\xBA'     #  0xba
    u'\u1EB1'   #  0xbb -> LATIN SMALL LETTER A WITH BREVE AND GRAVE
    u'\u1EB3'   #  0xbc -> LATIN SMALL LETTER A WITH BREVE AND HOOK ABOVE
    u'\u1EB5'   #  0xbd -> LATIN SMALL LETTER A WITH BREVE AND TILDE
    u'\u1EAF'   #  0xbe -> LATIN SMALL LETTER A WITH BREVE AND ACUTE
    u'\xBF'     #  0xbf
    u'\u1EBB'   #  0xc0 -> LATIN SMALL LETTER E WITH HOOK ABOVE
    u'\u1EBD'   #  0xc1 -> LATIN SMALL LETTER E WITH TILDE
    u'\u1EB9'   #  0xc2 -> LATIN SMALL LETTER E WITH DOT BELOW
    u'\xEB'     #  0xc3 -> LATIN SMALL LETTER E WITH DIAERESIS
    u'\u0192'   #  0xc4 -> LATIN SMALL LETTER F WITH HOOK
    u'\xC5'     #  0xc5
    u'\u1EB7'   #  0xc6 -> LATIN SMALL LETTER A WITH BREVE AND DOT BELOW
    u'\u1EA7'   #  0xc7 -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND GRAVE
    u'\u1EA9'   #  0xc8 -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE
    u'\u1EAB'   #  0xc9 -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE
    u'\u1EA5'   #  0xca -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND ACUTE
    u'\u1EAD'   #  0xcb -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND DOT BELOW
    u'\xE8'     #  0xcc -> LATIN SMALL LETTER E WITH GRAVE
    u'\xCD'     #  0xcd
    u'\u1EBB'   #  0xce -> LATIN SMALL LETTER E WITH HOOK ABOVE
    u'\u1EBD'   #  0xcf -> LATIN SMALL LETTER E WITH TILDE
    u'\xE9'     #  0xd0 -> LATIN SMALL LETTER E WITH ACUTE
    u'\u1EB9'   #  0xd1 -> LATIN SMALL LETTER E WITH DOT BELOW
    u'\u1EC1'   #  0xd2 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND GRAVE
    u'\u1EC3'   #  0xd3 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE
    u'\u1EC5'   #  0xd4 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND TILDE
    u'\u1EBF'   #  0xd5 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND ACUTE
    u'\u1EC7'   #  0xd6 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND DOT BELOW
    u'\xEC'     #  0xd7 -> LATIN SMALL LETTER I WITH GRAVE
    u'\u1EC9'   #  0xd8 -> LATIN SMALL LETTER I WITH HOOK ABOVE
    u'\xD9'     #  0xd9
    u'\xEF'     #  0xda -> LATIN SMALL LETTER I WITH DIAERESIS
    u'\xEE'     #  0xdb -> LATIN SMALL LETTER I WITH CIRCUMFLEX
    u'\u0129'   #  0xdc -> LATIN SMALL LETTER I WITH TILDE
    u'\xED'     #  0xdd -> LATIN SMALL LETTER I WITH ACUTE
    u'\u1ECB'   #  0xde -> LATIN SMALL LETTER I WITH DOT BELOW
    u'\xF2'     #  0xdf -> LATIN SMALL LETTER O WITH GRAVE
    u'\xE0'     #  0xe0
    u'\u1ECF'   #  0xe1 -> LATIN SMALL LETTER O WITH HOOK ABOVE
    u'\xF5'     #  0xe2 -> LATIN SMALL LETTER O WITH TILDE
    u'\xF3'     #  0xe3 -> LATIN SMALL LETTER O WITH ACUTE
    u'\u1ECD'   #  0xe4 -> LATIN SMALL LETTER O WITH DOT BELOW
    u'\u1ED3'   #  0xe5 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND GRAVE
    u'\u1ED5'   #  0xe6 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE
    u'\u1ED7'   #  0xe7 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND TILDE
    u'\u1ED1'   #  0xe8 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND ACUTE
    u'\u1ED9'   #  0xe9 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND DOT BELOW
    u'\u1EDD'   #  0xea -> LATIN SMALL LETTER O WITH HORN AND GRAVE
    u'\u1EDF'   #  0xeb -> LATIN SMALL LETTER O WITH HORN AND HOOK ABOVE
    u'\u1EE1'   #  0xec -> LATIN SMALL LETTER O WITH HORN AND TILDE
    u'\u1EDB'   #  0xed -> LATIN SMALL LETTER O WITH HORN AND ACUTE
    u'\u1EE3'   #  0xee -> LATIN SMALL LETTER O WITH HORN AND DOT BELOW
    u'\xF9'     #  0xef -> LATIN SMALL LETTER U WITH GRAVE
    u'\xF0'     #  0xf0
    u'\u1EE7'   #  0xf1 -> LATIN SMALL LETTER U WITH HOOK ABOVE
    u'\u0169'   #  0xf2 -> LATIN SMALL LETTER U WITH TILDE
    u'\xFA'     #  0xf3 -> LATIN SMALL LETTER U WITH ACUTE
    u'\u1EE5'   #  0xf4 -> LATIN SMALL LETTER U WITH DOT BELOW
    u'\u1EEB'   #  0xf5 -> LATIN SMALL LETTER U WITH HORN AND GRAVE
    u'\u1EED'   #  0xf6 -> LATIN SMALL LETTER U WITH HORN AND HOOK ABOVE
    u'\u1EEF'   #  0xf7 -> LATIN SMALL LETTER U WITH HORN AND TILDE
    u'\u1EE9'   #  0xf8 -> LATIN SMALL LETTER U WITH HORN AND ACUTE
    u'\u1EF1'   #  0xf9 -> LATIN SMALL LETTER U WITH HORN AND DOT BELOW
    u'\u1EF3'   #  0xfa -> LATIN SMALL LETTER Y WITH GRAVE
    u'\u1EF7'   #  0xfb -> LATIN SMALL LETTER Y WITH HOOK ABOVE
    u'\u1EF9'   #  0xfc -> LATIN SMALL LETTER Y WITH TILDE
    u'\xFD'     #  0xfd -> LATIN SMALL LETTER Y WITH ACUTE
    u'\u1EF5'   #  0xfe -> LATIN SMALL LETTER Y WITH DOT BELOW
    u'\xFF'     #  0xff
)

vntime_tcvn_encoding_map = codecs.charmap_build(vntime_tcvn_decoding_table)

def vntime_tcvn_decode(input, errors='strict'):
    return codecs.charmap_decode(input, errors, vntime_tcvn_decoding_table)

def vntime_tcvn_encode(input, errors='strict'):
    return codecs.charmap_encode(input, errors, vntime_tcvn_encoding_map)

