"""
B2UConverter — UNO extension for OpenOffice.org
File: include/openoffice/header.py

Copyright ©2009  Ministry of Science and Technology of Vietnam
License: GNU Lesser General Public License version 2.1
Authors: Jean Christophe André <jcandre@hanoilug.org>
         Lê Quốc Thái <lqthai@hanoilug.org>
         Võ Đức Phương <vdphuong@hanoilug.org>
"""

import sys
import logging
import traceback

_settings = {
  "Debug": False,
  "RemoveDiacritics": False,
  "VNIHacks": False,
}
_error_count = 0

