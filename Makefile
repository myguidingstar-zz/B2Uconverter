all: clean build remove install

build:
	rm -f B2UConverter.oxt ; cd openoffice ; zip -9rpD ../B2UConverter.oxt .

install:
	unopkg add B2UConverter.oxt

remove:
	unopkg remove vn.gov.most.openoffice.b2uconverter

clean:
	rm -f B2UConverter.oxt

