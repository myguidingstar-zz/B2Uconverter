#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
B2UConverter — UNO extension for OpenOffice.org and LibreOffice
File: scripts/build-B2UConverter.py

Copyright ©2009  Ministry of Science and Technology of Vietnam
License: GNU Lesser General Public License version 2.1
Authors: Jean Christophe André <jcandre@hanoilug.org>
         Lê Quốc Thái <lqthai@hanoilug.org>
         Võ Đức Phương <vdphuong@hanoilug.org>
"""

import sys
from StringIO import StringIO

if len(sys.argv) != 1:
    print "Syntax: %s"
    sys.exit(1)

data = [
  StringIO("""# -*- coding: utf-8 -*-
# WARNING: This file has been dynamically generated, don't edit it!
# WARNING: You can edit files in the 'include' folder instead,
# WARNING: then run 'python %s'.
""" % sys.argv[0]),
  file('include/openoffice/header.py'),
  file('include/openoffice/encodings_header.py'),
  file('include/encodings/vntime_tcvn.py'),
  file('include/encodings/vni.py'),
  file('include/encodings/cp1252.py'),
  file('include/openoffice/encodings_footer.py'),
  file('include/vietnamese_recoding.py'),
  file('include/openoffice/document_processing.py'),
  file('include/openoffice/extension_object.py'),
]

for d in data:
    sys.stdout.write(d.read())
    d.close()

sys.exit(0)
