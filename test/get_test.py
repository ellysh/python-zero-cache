#!/usr/bin/env python

import client_wrap

KEY_LONG = "key1"
DATA_LONG = 1024

KEY_DOUBLE = "key2"
DATA_DOUBLE = 100.53

KEY_STRING = "key3"
DATA_STRING = "test data"

def init_data(client):
    client.WriteLong(KEY_LONG, DATA_LONG)
    client.WriteDouble(KEY_DOUBLE, DATA_DOUBLE)
    client.WriteString(KEY_STRING, DATA_STRING)

def check_data(client):
    assert DATA_LONG == client.ReadLong(KEY_LONG)
    assert DATA_DOUBLE == client.ReadDouble(KEY_DOUBLE)
    assert DATA_STRING == client.ReadString(KEY_STRING)

def main():
    client = client_wrap.ClientWrap("get_test.log", "ipc:///var/run/zero-cache/0", 0)
    init_data(client)
    check_data(client)

if __name__ == "__main__":
    main()
