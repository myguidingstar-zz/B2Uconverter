VERSION=$(shell cat doc/VERSION)

all: top-build
	echo 'push b2uconverter-update.xml and b2uconverter-news to http://myguidingstar.github.com/'
make-executable:
	chmod +x scripts/build-Addons.sh scripts/build-B2UConverter.sh
description:
	cd openoffice; sed s~{{VERSION}}~$(VERSION)~ description.xml.template > description.xml
	sed s~{{VERSION}}~$(VERSION)~g b2uconverter-update.xml.template > b2uconverter-update.xml
	cp doc/NEWS b2uconverter-news
top-menu: make-executable
	scripts/build-Addons.sh top > openoffice/Addons.xcu
addons-menu: make-executable
	scripts/build-Addons.sh addons > openoffice/Addons.xcu

openoffice/B2UConverter.py: make-executable
	scripts/build-B2UConverter.sh > openoffice/B2UConverter.py

zip-it:
	mkdir -p openoffice/images
	cp -a include/images/white-red/* openoffice/images/
	rm -f B2UConverter-*.oxt
	cd openoffice ; zip -q9rpD -xdescription.xml.template ../B2UConverter-$(VERSION).oxt .

top-build: description top-menu openoffice/B2UConverter.py zip-it

addons-build: description addons-menu openoffice/B2UConverter.py zip-it

build: top-build

uninstall:
	unopkg remove vn.gov.oss.openoffice.b2uconverter

install: build uninstall
	unopkg add B2UConverter-$(VERSION).oxt

clean:
	rm -f openoffice/description.xml
	rm -f openoffice/Addons.xcu
	rm -f openoffice/B2UConverter.py
	rm -f B2UConverter-*.oxt
	rm -f b2uconverter-update.xml
	rm -f b2uconverter-news

