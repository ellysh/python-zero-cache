#!/usr/bin/env python

import client_wrap


KEY_LONG = "key1"
DATA_LONG = 1024

def init_data(client):
    client.WriteLong(KEY_LONG, DATA_LONG)

def check_data(client):
    assert DATA_LONG == client.ReadLong(KEY_LONG)

def main():
    client = client_wrap.ClientWrap("tcp_test.log", "tcp://localhost:5570", 0)

    init_data(client)
    check_data(client)

if __name__ == "__main__":
    main()
