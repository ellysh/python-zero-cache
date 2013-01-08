SUBDIRS = interface

.PHONY: all $(SUBDIRS)

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ clean
	$(MAKE) -C $@

install:
	$(MAKE) -C $(SUBDIRS) install
