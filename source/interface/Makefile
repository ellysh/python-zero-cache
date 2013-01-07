CLIENT_DIR = ../client
CXXFLAGS = -I"/usr/include/python2.7" -I"/usr/lib/python2.7/config" -I"../common"

all: clean
	swig -python -c++ -make_default registrar_client.i
	gcc -c -fpic registrar_client_wrap.cxx $(CLIENT_DIR)/registrar_client.cpp -DHAVE_CONFIG_H $(CXXFLAGS)
	g++ -shared registrar_client.o registrar_client_wrap.o -o _registrar_client.so

clean:
	rm -f *_wrap.* *.so *.o *.py
