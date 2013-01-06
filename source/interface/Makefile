all: clean
	swig -python try.i
	gcc -c -fpic try_wrap.c try.c  -DHAVE_CONFIG_H  -I"/usr/include/python2.7" -I"/usr/lib/python2.7/config"
	gcc -shared try.o try_wrap.o -o _mytry.so

clean:
	rm -f try_wrap.* *.so *.o mytry.py
