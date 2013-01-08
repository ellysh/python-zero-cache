SUBDIRS = source

.PHONY: all deb $(SUBDIRS)

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

install:
	$(MAKE) -C $(SUBDIRS) install

deb:
	rm -fR deb/*
	dpkg-buildpackage -rfakeroot -b -us -uc
	mv -f ../*.changes ../*.deb deb
