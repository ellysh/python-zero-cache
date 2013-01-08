SUBDIRS = source

.PHONY: all deb $(SUBDIRS)

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

deb:
	dpkg-buildpackage -rfakeroot -b -us -uc
	mv -f ../*.changes ../*.deb deb
