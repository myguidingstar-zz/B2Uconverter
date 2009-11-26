all: clean build remove install

build:
	rm -f OvniConv.oxt ; cd openoffice ; zip -9rpD ../OvniConv.oxt .

install:
	unopkg add OvniConv.oxt

remove:
	unopkg remove org.hanoilug.openoffice.ovniconv

clean:
	rm -f OvniConv.oxt

