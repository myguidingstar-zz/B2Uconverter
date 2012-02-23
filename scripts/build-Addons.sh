#!/bin/bash
cat include/addons-menu/${1}_header.xml
echo "<!--"
echo "# WARNING: This file has been dynamically generated, don't edit it!"
echo "# WARNING: You can edit files in the 'include' folder instead,"
echo "# WARNING: then run 'python %s'"
echo "-->"
cat include/addons-menu/common.xml
cat include/addons-menu/${1}_footer.xml
  
