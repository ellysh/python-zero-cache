%module client_wrap

%{
#include "../client/client_wrap.h"

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

%include "../client/client_wrap.h"
