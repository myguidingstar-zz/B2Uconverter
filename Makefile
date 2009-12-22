#MENU_TYPE=addon-menu
MENU_TYPE=top-menu

all: uninstall install

openoffice/B2UConverter.py: scripts/build-B2UConverter.py $(shell find include -type f)
	python scripts/build-B2UConverter.py

openoffice/Addons.xcu: include/openoffice/Addons-$(MENU_TYPE).xcu
	cp -af include/openoffice/Addons-$(MENU_TYPE).xcu openoffice/Addons.xcu

B2UConverter.oxt: openoffice/B2UConverter.py openoffice/Addons.xcu $(shell find openoffice -type f)
	rm -f B2UConverter.oxt
	cd openoffice ; zip -q9rpD ../B2UConverter.oxt .

build: B2UConverter.oxt

install: build
	unopkg add B2UConverter.oxt

uninstall:
	unopkg remove vn.gov.oss.openoffice.b2uconverter

clean:
	rm -f B2UConverter.oxt
	rm -f openoffice/B2UConverter.py
	rm -f openoffice/Addons.xcu

