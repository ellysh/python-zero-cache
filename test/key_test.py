#!/usr/bin/env python

import client_wrap

KEY_1 = "key1"
KEY_2 = "key2"

DATA_LONG = 1024

def init_data(client):
    client.WriteLong(KEY_1, DATA_LONG)
    client.WriteLong(KEY_2, DATA_LONG)

def check_keys(client):
    string = client.GetKeys()
    keys = string.split (';')
    del keys[-1]
    assert len(keys) == 2
    assert keys[0] == KEY_1
    assert keys[1] == KEY_2

def main():
    client = client_wrap.ClientWrap("tcp_test.log", "ipc:///var/run/zero-cache/0", 0)
    client.GetKeys()
    init_data(client)
    check_keys(client)

if __name__ == "__main__":
    main()
