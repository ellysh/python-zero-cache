#!/usr/bin/env python

import client_wrap

KEY_1 = "key1"
KEY_2 = "key2"

DATA_LONG = 1024

def init_data(client):
    client.WriteLong(KEY_1, DATA_LONG)
    client.WriteLong(KEY_2, DATA_LONG)

def check_keys(client):
    keys = client.GetKeys()
    print keys

def main():
    client = client_wrap.ClientWrap("get_test.log", "ipc:///var/run/zero-cache/0", 0)
    init_data(client)
    check_keys(client)

if __name__ == "__main__":
    main()
