"""
B2UConverter — UNO extension for OpenOffice.org and LibreOffice
File: include/openoffice/encodings_header.py

Copyright ©2009  Ministry of Science and Technology of Vietnam
License: GNU Lesser General Public License version 2.1
Authors: Jean Christophe André <jcandre@hanoilug.org>
         Lê Quốc Thái <lqthai@hanoilug.org>
         Võ Đức Phương <vdphuong@hanoilug.org>
"""

import codecs

# codecs.charmap_build lacks in the Python 2.3.4 bundled with Windows's OOo
if not 'charmap_build' in codecs.__dict__:
    # this code has been "stolen" from Python 2.5 codecs.py
    def _encoding_map_from_decoding_table(table):
        m = {}
        for k,v in list(table.items()):
            if not v in m:
                m[v] = k
            else:
                m[v] = None
        return m

    codecs.charmap_build = _encoding_map_from_decoding_table

