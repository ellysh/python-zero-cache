%module registrar_client

%{
#include "../client/registrar_client.h"

using namespace zero_cache;
%}

%include "std_string.i"

%include "../client/registrar_client.h"
