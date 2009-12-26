#MENU_TYPE=addons
MENU_TYPE=top

all: build

openoffice/Addons.xcu: scripts/build-Addons.xcu $(shell find include/addons-menu -type f)
	python scripts/build-Addons.xcu $(MENU_TYPE) > openoffice/Addons.xcu

openoffice/B2UConverter.py: scripts/build-B2UConverter.py $(shell find include -type f)
	python scripts/build-B2UConverter.py > openoffice/B2UConverter.py

B2UConverter.oxt: openoffice/Addons.xcu openoffice/B2UConverter.py $(shell find openoffice -type f)
	rm -f B2UConverter.oxt
	cd openoffice ; zip -q9rpD -x.svn ../B2UConverter.oxt .

build: B2UConverter.oxt

uninstall:
	unopkg remove vn.gov.oss.openoffice.b2uconverter

install: build uninstall
	unopkg add B2UConverter.oxt

clean:
	rm -f openoffice/Addons.xcu
	rm -f openoffice/B2UConverter.py
	rm -f B2UConverter.oxt

