CLIENT_DIR = ../client
COMMON_DIR = ../common
CPP_FILES = $(CLIENT_DIR)/client.cpp \
			$(COMMON_DIR)/debug.cpp \
			$(COMMON_DIR)/speaker.cpp
INSTALL_LIB_DIR = usr/lib/python2.7/lib-dynload
INSTALL_MODULE_DIR = usr/lib/python2.7

OBJ_FILES = client.o debug.o speaker.o
CXXFLAGS = -I"/usr/include/python2.7" -I"/usr/lib/python2.7/config" -I"../common" -I"../server"
MODULE_NAME = client

all: clean $(MODULE_NAME)

$(MODULE_NAME):
	swig -python -c++ -make_default $(MODULE_NAME).i
	gcc -c -fpic $(MODULE_NAME)_wrap.cxx $(CPP_FILES) -DHAVE_CONFIG_H $(CXXFLAGS)
	g++ -shared $(OBJ_FILES) $(MODULE_NAME)_wrap.o -o _$(MODULE_NAME).so

install:
	mkdir -p $(DESTDIR)/$(INSTALL_MODULE_DIR)
	cp $(MODULE_NAME).py $(DESTDIR)/$(INSTALL_MODULE_DIR)
	mkdir -p $(DESTDIR)/$(INSTALL_LIB_DIR)
	cp _$(MODULE_NAME).so $(DESTDIR)/$(INSTALL_LIB_DIR)

clean:
	rm -f *.cxx *.so *.o *.py
