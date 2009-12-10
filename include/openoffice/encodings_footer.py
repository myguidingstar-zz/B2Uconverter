"""
B2UConverter — UNO extension for OpenOffice.org
File: include/openoffice/encodings_footer.py

Copyright ©2009  Ministry of Science and Technology of Vietnam
License: GNU Lesser General Public License version 2.1
Authors: Jean Christophe André <jcandre@hanoilug.org>
         Lê Quốc Thái <lqthai@hanoilug.org>
         Võ Đức Phương <vdphuong@hanoilug.org>
"""

def _privateCodecSearch(name):
    if name == 'internal_vntime_tcvn':
        return (vntime_tcvn_encode, vntime_tcvn_decode, None, None)
    if name == 'internal_vni':
        return (None, vni_decode, None, None)
    return None

# register new/internal codecs
codecs.register(_privateCodecSearch)

