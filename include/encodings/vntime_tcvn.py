""" Python Character Mapping Codec vntime_tcvn (.VnTime font - Vietnamese)
                        (kind of TCVN 5712:1993 VN3 with CP1252 additions)
    Copyright (c) 2008-2009  Jean Christophe André <jcandre@hanoilug.org>
    License: GNU Lesser General Public License version 2.1
    To enable this encoding, move this file into /usr/lib/python2.5/encodings/
"""

vntime_tcvn_decoding_table = (
    '\x00'     #  0x00 -> NULL (NUL)
    '\x01'     #  0x01
    '\x02'     #  0x02
    '\x03'     #  0x03 -> END OF TEXT
    '\x04'     #  0x04
    '\x05'     #  0x05
    '\x06'     #  0x06
    '\x07'     #  0x07 -> BELL (BEL)
    '\x08'     #  0x08 -> BACKSPACE (BS)
    '\x09'     #  0x09 -> CHARACTER TABULATION (HT)
    '\x0A'     #  0x0a -> LINE FEED (LF)
    '\x0B'     #  0x0b -> LINE TABULATION (VT)
    '\x0C'     #  0x0c -> FORM FEED (FF)
    '\x0D'     #  0x0d -> CARRIAGE RETURN (CR)
    '\x0E'     #  0x0e -> SHIFT OUT (SO)
    '\x0F'     #  0x0f -> SHIFT IN (SI)
    '\x10'     #  0x10 -> DATA LINK ESCAPE (DLE)
    '\x11'     #  0x11
    '\x12'     #  0x12
    '\x13'     #  0x13
    '\x14'     #  0x14
    '\x15'     #  0x15
    '\x16'     #  0x16
    '\x17'     #  0x17
    '\x18'     #  0x18 -> CANCEL (CAN)
    '\x19'     #  0x19 -> END OF MEDIUM (EM)
    '\x1A'     #  0x1a -> SUBSTITUTE (SUB)
    '\x1B'     #  0x1b -> ESCAPE (ESC)
    '\x1C'     #  0x1c -> FILE SEPARATOR (IS4)
    '\x1D'     #  0x1d -> GROUP SEPARATOR (IS3)
    '\x1E'     #  0x1e -> RECORD SEPARATOR (IS2)
    '\x1F'     #  0x1f -> UNIT SEPARATOR (IS1)
    ' '        #  0x20 -> SPACE
    '!'        #  0x21 -> EXCLAMATION MARK
    '"'        #  0x22 -> QUOTATION MARK
    '#'        #  0x23 -> NUMBER SIGN
    '$'        #  0x24 -> DOLLAR SIGN
    '%'        #  0x25 -> PERCENT SIGN
    '&'        #  0x26 -> AMPERSAND
    "'"        #  0x27 -> APOSTROPHE
    '('        #  0x28 -> LEFT PARENTHESIS
    ')'        #  0x29 -> RIGHT PARENTHESIS
    '*'        #  0x2A -> ASTERISK
    '+'        #  0x2B -> PLUS SIGN
    ','        #  0x2C -> COMMA
    '-'        #  0x2D -> HYPHEN-MINUS
    '.'        #  0x2E -> FULL STOP
    '/'        #  0x2F -> SOLIDUS
    '0'        #  0x30 -> DIGIT ZERO
    '1'        #  0x31 -> DIGIT ONE
    '2'        #  0x32 -> DIGIT TWO
    '3'        #  0x33 -> DIGIT THREE
    '4'        #  0x34 -> DIGIT FOUR
    '5'        #  0x35 -> DIGIT FIVE
    '6'        #  0x36 -> DIGIT SIX
    '7'        #  0x37 -> DIGIT SEVEN
    '8'        #  0x38 -> DIGIT EIGHT
    '9'        #  0x39 -> DIGIT NINE
    ':'        #  0x3A -> COLON
    ';'        #  0x3B -> SEMICOLON
    '<'        #  0x3C -> LESS-THAN SIGN
    '='        #  0x3D -> EQUALS SIGN
    '>'        #  0x3E -> GREATER-THAN SIGN
    '?'        #  0x3F -> QUESTION MARK
    '@'        #  0x40 -> COMMERCIAL AT
    'A'        #  0x41 -> LATIN CAPITAL LETTER A
    'B'        #  0x42 -> LATIN CAPITAL LETTER B
    'C'        #  0x43 -> LATIN CAPITAL LETTER C
    'D'        #  0x44 -> LATIN CAPITAL LETTER D
    'E'        #  0x45 -> LATIN CAPITAL LETTER E
    'F'        #  0x46 -> LATIN CAPITAL LETTER F
    'G'        #  0x47 -> LATIN CAPITAL LETTER G
    'H'        #  0x48 -> LATIN CAPITAL LETTER H
    'I'        #  0x49 -> LATIN CAPITAL LETTER I
    'J'        #  0x4A -> LATIN CAPITAL LETTER J
    'K'        #  0x4B -> LATIN CAPITAL LETTER K
    'L'        #  0x4C -> LATIN CAPITAL LETTER L
    'M'        #  0x4D -> LATIN CAPITAL LETTER M
    'N'        #  0x4E -> LATIN CAPITAL LETTER N
    'O'        #  0x4F -> LATIN CAPITAL LETTER O
    'P'        #  0x50 -> LATIN CAPITAL LETTER P
    'Q'        #  0x51 -> LATIN CAPITAL LETTER Q
    'R'        #  0x52 -> LATIN CAPITAL LETTER R
    'S'        #  0x53 -> LATIN CAPITAL LETTER S
    'T'        #  0x54 -> LATIN CAPITAL LETTER T
    'U'        #  0x55 -> LATIN CAPITAL LETTER U
    'V'        #  0x56 -> LATIN CAPITAL LETTER V
    'W'        #  0x57 -> LATIN CAPITAL LETTER W
    'X'        #  0x58 -> LATIN CAPITAL LETTER X
    'Y'        #  0x59 -> LATIN CAPITAL LETTER Y
    'Z'        #  0x5A -> LATIN CAPITAL LETTER Z
    '['        #  0x5B -> LEFT SQUARE BRACKET
    '\\'       #  0x5C -> REVERSE SOLIDUS
    ']'        #  0x5D -> RIGHT SQUARE BRACKET
    '^'        #  0x5E -> CIRCUMFLEX ACCENT
    '_'        #  0x5F -> LOW LINE
    '`'        #  0x60 -> GRAVE ACCENT
    'a'        #  0x61 -> LATIN SMALL LETTER A
    'b'        #  0x62 -> LATIN SMALL LETTER B
    'c'        #  0x63 -> LATIN SMALL LETTER C
    'd'        #  0x64 -> LATIN SMALL LETTER D
    'e'        #  0x65 -> LATIN SMALL LETTER E
    'f'        #  0x66 -> LATIN SMALL LETTER F
    'g'        #  0x67 -> LATIN SMALL LETTER G
    'h'        #  0x68 -> LATIN SMALL LETTER H
    'i'        #  0x69 -> LATIN SMALL LETTER I
    'j'        #  0x6A -> LATIN SMALL LETTER J
    'k'        #  0x6B -> LATIN SMALL LETTER K
    'l'        #  0x6C -> LATIN SMALL LETTER L
    'm'        #  0x6D -> LATIN SMALL LETTER M
    'n'        #  0x6E -> LATIN SMALL LETTER N
    'o'        #  0x6F -> LATIN SMALL LETTER O
    'p'        #  0x70 -> LATIN SMALL LETTER P
    'q'        #  0x71 -> LATIN SMALL LETTER Q
    'r'        #  0x72 -> LATIN SMALL LETTER R
    's'        #  0x73 -> LATIN SMALL LETTER S
    't'        #  0x74 -> LATIN SMALL LETTER T
    'u'        #  0x75 -> LATIN SMALL LETTER U
    'v'        #  0x76 -> LATIN SMALL LETTER V
    'w'        #  0x77 -> LATIN SMALL LETTER W
    'x'        #  0x78 -> LATIN SMALL LETTER X
    'y'        #  0x79 -> LATIN SMALL LETTER Y
    'z'        #  0x7A -> LATIN SMALL LETTER Z
    '{'        #  0x7B -> LEFT CURLY BRACKET
    '|'        #  0x7C -> VERTICAL LINE
    '}'        #  0x7D -> RIGHT CURLY BRACKET
    '~'        #  0x7E -> TILDE
    '\x7F'     #  0x7f -> DELETE (DEL)
    '\x80'     #  0x80
    '\x81'     #  0x81
    '\x82'     #  0x82
    '\x83'     #  0x83
    '\x84'     #  0x84
    '\u2026'   #  0x85 -> HORIZONTAL ELLIPSIS
    '\xC7'     #  0x86 -> LATIN CAPITAL LETTER C WITH CEDILLA
    '\x87'     #  0x87
    '\xCB'     #  0x88 -> LATIN CAPITAL LETTER E WITH DIAERESIS
    '\xCA'     #  0x89 -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    '\xCF'     #  0x8a -> LATIN CAPITAL LETTER I WITH DIAERESIS
    '\xCE'     #  0x8b -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    '\x8C'     #  0x8c
    '\x8D'     #  0x8d
    '\x8E'     #  0x8e
    '\x8F'     #  0x8f
    '\x90'     #  0x90
    '\u2018'   #  0x91 -> LEFT SINGLE QUOTATION MARK
    '\u2019'   #  0x92 -> RIGHT SINGLE QUOTATION MARK
    '\u201c'   #  0x93 -> LEFT DOUBLE QUOTATION MARK
    '\u201d'   #  0x94 -> RIGHT DOUBLE QUOTATION MARK
    '\u2022'   #  0x95 -> BULLET
    '\u2013'   #  0x96 -> EN DASH
    '\u2014'   #  0x97 -> EM DASH
    '\x98'     #  0x98
    '\x99'     #  0x99
    '\xDC'     #  0x9a -> LATIN CAPITAL LETTER U WITH DIAERESIS
    '\xDB'     #  0x9b -> LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    '\x9C'     #  0x9c
    '\x9D'     #  0x9d
    '\x9E'     #  0x9e
    '\x9F'     #  0x9f
    '\xA0'     #  0xa0 -> NO-BREAK SPACE
    '\u0102'   #  0xa1 -> LATIN CAPITAL LETTER A WITH BREVE
    '\xC2'     #  0xa2 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    '\xCA'     #  0xa3 -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    '\xD4'     #  0xa4 -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    '\u01A0'   #  0xa5 -> LATIN CAPITAL LETTER O WITH HORN
    '\u01AF'   #  0xa6 -> LATIN CAPITAL LETTER U WITH HORN
    '\u0110'   #  0xa7 -> LATIN CAPITAL LETTER D WITH STROKE
    '\u0103'   #  0xa8 -> LATIN SMALL LETTER A WITH BREVE
    '\xE2'     #  0xa9 -> LATIN SMALL LETTER A WITH CIRCUMFLEX
    '\xEA'     #  0xaa -> LATIN SMALL LETTER E WITH CIRCUMFLEX
    '\xF4'     #  0xab -> LATIN SMALL LETTER O WITH CIRCUMFLEX
    '\u01A1'   #  0xac -> LATIN SMALL LETTER O WITH HORN
    '\u01B0'   #  0xad -> LATIN SMALL LETTER U WITH HORN
    '\u0111'   #  0xae -> LATIN SMALL LETTER D WITH STROKE
    '\xAF'     #  0xaf
    '\xB0'     #  0xb0
    '\xB1'     #  0xb1
    '\xB2'     #  0xb2
    '\xB3'     #  0xb3
    '\xB4'     #  0xb4
    '\xE0'     #  0xb5 -> LATIN SMALL LETTER A WITH GRAVE
    '\u1EA3'   #  0xb6 -> LATIN SMALL LETTER A WITH HOOK ABOVE
    '\xE3'     #  0xb7 -> LATIN SMALL LETTER A WITH TILDE
    '\xE1'     #  0xb8 -> LATIN SMALL LETTER A WITH ACUTE
    '\u1EA1'   #  0xb9 -> LATIN SMALL LETTER A WITH DOT BELOW
    '\xBA'     #  0xba
    '\u1EB1'   #  0xbb -> LATIN SMALL LETTER A WITH BREVE AND GRAVE
    '\u1EB3'   #  0xbc -> LATIN SMALL LETTER A WITH BREVE AND HOOK ABOVE
    '\u1EB5'   #  0xbd -> LATIN SMALL LETTER A WITH BREVE AND TILDE
    '\u1EAF'   #  0xbe -> LATIN SMALL LETTER A WITH BREVE AND ACUTE
    '\xBF'     #  0xbf
    '\u1EBB'   #  0xc0 -> LATIN SMALL LETTER E WITH HOOK ABOVE
    '\u1EBD'   #  0xc1 -> LATIN SMALL LETTER E WITH TILDE
    '\u1EB9'   #  0xc2 -> LATIN SMALL LETTER E WITH DOT BELOW
    '\xEB'     #  0xc3 -> LATIN SMALL LETTER E WITH DIAERESIS
    '\u0192'   #  0xc4 -> LATIN SMALL LETTER F WITH HOOK
    '\xC5'     #  0xc5
    '\u1EB7'   #  0xc6 -> LATIN SMALL LETTER A WITH BREVE AND DOT BELOW
    '\u1EA7'   #  0xc7 -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND GRAVE
    '\u1EA9'   #  0xc8 -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE
    '\u1EAB'   #  0xc9 -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE
    '\u1EA5'   #  0xca -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND ACUTE
    '\u1EAD'   #  0xcb -> LATIN SMALL LETTER A WITH CIRCUMFLEX AND DOT BELOW
    '\xE8'     #  0xcc -> LATIN SMALL LETTER E WITH GRAVE
    '\xCD'     #  0xcd
    '\u1EBB'   #  0xce -> LATIN SMALL LETTER E WITH HOOK ABOVE
    '\u1EBD'   #  0xcf -> LATIN SMALL LETTER E WITH TILDE
    '\xE9'     #  0xd0 -> LATIN SMALL LETTER E WITH ACUTE
    '\u1EB9'   #  0xd1 -> LATIN SMALL LETTER E WITH DOT BELOW
    '\u1EC1'   #  0xd2 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND GRAVE
    '\u1EC3'   #  0xd3 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE
    '\u1EC5'   #  0xd4 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND TILDE
    '\u1EBF'   #  0xd5 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND ACUTE
    '\u1EC7'   #  0xd6 -> LATIN SMALL LETTER E WITH CIRCUMFLEX AND DOT BELOW
    '\xEC'     #  0xd7 -> LATIN SMALL LETTER I WITH GRAVE
    '\u1EC9'   #  0xd8 -> LATIN SMALL LETTER I WITH HOOK ABOVE
    '\xD9'     #  0xd9
    '\xEF'     #  0xda -> LATIN SMALL LETTER I WITH DIAERESIS
    '\xEE'     #  0xdb -> LATIN SMALL LETTER I WITH CIRCUMFLEX
    '\u0129'   #  0xdc -> LATIN SMALL LETTER I WITH TILDE
    '\xED'     #  0xdd -> LATIN SMALL LETTER I WITH ACUTE
    '\u1ECB'   #  0xde -> LATIN SMALL LETTER I WITH DOT BELOW
    '\xF2'     #  0xdf -> LATIN SMALL LETTER O WITH GRAVE
    '\xE0'     #  0xe0
    '\u1ECF'   #  0xe1 -> LATIN SMALL LETTER O WITH HOOK ABOVE
    '\xF5'     #  0xe2 -> LATIN SMALL LETTER O WITH TILDE
    '\xF3'     #  0xe3 -> LATIN SMALL LETTER O WITH ACUTE
    '\u1ECD'   #  0xe4 -> LATIN SMALL LETTER O WITH DOT BELOW
    '\u1ED3'   #  0xe5 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND GRAVE
    '\u1ED5'   #  0xe6 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE
    '\u1ED7'   #  0xe7 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND TILDE
    '\u1ED1'   #  0xe8 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND ACUTE
    '\u1ED9'   #  0xe9 -> LATIN SMALL LETTER O WITH CIRCUMFLEX AND DOT BELOW
    '\u1EDD'   #  0xea -> LATIN SMALL LETTER O WITH HORN AND GRAVE
    '\u1EDF'   #  0xeb -> LATIN SMALL LETTER O WITH HORN AND HOOK ABOVE
    '\u1EE1'   #  0xec -> LATIN SMALL LETTER O WITH HORN AND TILDE
    '\u1EDB'   #  0xed -> LATIN SMALL LETTER O WITH HORN AND ACUTE
    '\u1EE3'   #  0xee -> LATIN SMALL LETTER O WITH HORN AND DOT BELOW
    '\xF9'     #  0xef -> LATIN SMALL LETTER U WITH GRAVE
    '\xF0'     #  0xf0
    '\u1EE7'   #  0xf1 -> LATIN SMALL LETTER U WITH HOOK ABOVE
    '\u0169'   #  0xf2 -> LATIN SMALL LETTER U WITH TILDE
    '\xFA'     #  0xf3 -> LATIN SMALL LETTER U WITH ACUTE
    '\u1EE5'   #  0xf4 -> LATIN SMALL LETTER U WITH DOT BELOW
    '\u1EEB'   #  0xf5 -> LATIN SMALL LETTER U WITH HORN AND GRAVE
    '\u1EED'   #  0xf6 -> LATIN SMALL LETTER U WITH HORN AND HOOK ABOVE
    '\u1EEF'   #  0xf7 -> LATIN SMALL LETTER U WITH HORN AND TILDE
    '\u1EE9'   #  0xf8 -> LATIN SMALL LETTER U WITH HORN AND ACUTE
    '\u1EF1'   #  0xf9 -> LATIN SMALL LETTER U WITH HORN AND DOT BELOW
    '\u1EF3'   #  0xfa -> LATIN SMALL LETTER Y WITH GRAVE
    '\u1EF7'   #  0xfb -> LATIN SMALL LETTER Y WITH HOOK ABOVE
    '\u1EF9'   #  0xfc -> LATIN SMALL LETTER Y WITH TILDE
    '\xFD'     #  0xfd -> LATIN SMALL LETTER Y WITH ACUTE
    '\u1EF5'   #  0xfe -> LATIN SMALL LETTER Y WITH DOT BELOW
    '\xFF'     #  0xff
)

vntime_tcvn_encoding_map = codecs.charmap_build(vntime_tcvn_decoding_table)

def vntime_tcvn_decode(input, errors='strict'):
    return codecs.charmap_decode(input, errors, vntime_tcvn_decoding_table)

def vntime_tcvn_encode(input, errors='strict'):
    return codecs.charmap_encode(input, errors, vntime_tcvn_encoding_map)

