CLIENT_DIR = ../client
COMMON_DIR = ../common
CPP_FILES = $(CLIENT_DIR)/registrar_client.cpp \
			$(CLIENT_DIR)/client_list.cpp \
			$(CLIENT_DIR)/client.cpp \
			$(COMMON_DIR)/debug.cpp \
			$(COMMON_DIR)/connection.cpp \
			$(COMMON_DIR)/functions.cpp \
			$(COMMON_DIR)/speaker.cpp \
			$(COMMON_DIR)/socket.cpp

OBJ_FILES = registrar_client.o debug.o functions.o client_list.o client.o connection.o socket.o speaker.o
CXXFLAGS = -I"/usr/include/python2.7" -I"/usr/lib/python2.7/config" -I"../common" -I"../server"
MODULE_NAME = registrar_client

all: clean $(MODULE_NAME)

$(MODULE_NAME):
	swig -python -c++ -make_default $(MODULE_NAME).i
	gcc -c -fpic $(MODULE_NAME)_wrap.cxx $(CPP_FILES) -DHAVE_CONFIG_H $(CXXFLAGS)
	g++ -shared $(OBJ_FILES) $(MODULE_NAME)_wrap.o -lczmq -o _$(MODULE_NAME).so

clean:
	rm -f *_wrap.* *.so *.o *.py
