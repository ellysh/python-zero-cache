%module registrar_client

%{
#include "../client/registrar_client.h"

using namespace zero_cache;
%}

%include "std_string.i"

%typemap(in) Connection
{
    $1 = Connection(PyString_AsString($input));
}

%typemap(in) SocketType
{
    $1 = SocketType(PyLong_AsLong($input));
}

%typemap(in) void* {
    $1 = PyString_AsString($input);
}

%typemap(out) void* {
   if ( $1 != NULL )
        $result = PyString_FromString((char*)$1);
    else
        $result = PyString_FromString("");
}

%include "../client/registrar_client.h"
