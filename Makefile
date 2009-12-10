all: uninstall install

openoffice/B2UConverter.py: build-B2UConverter.py $(shell find include -type f)
	python build-B2UConverter.py

B2UConverter.oxt: $(shell find openoffice -type f)
	rm -f B2UConverter.oxt
	cd openoffice ; zip -q9rpD ../B2UConverter.oxt .

build: B2UConverter.oxt

install: build
	unopkg add B2UConverter.oxt

uninstall:
	unopkg remove vn.gov.oss.openoffice.b2uconverter

clean:
	rm -f B2UConverter.oxt openoffice/B2UConverter.py

