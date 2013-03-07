#!/usr/bin/env python

import zero_cache

INDEX_LONG = 0
DATA_LONG = 1024

INDEX_DOUBLE = 1
DATA_DOUBLE = 100.53

def init_data(client):
    client.WriteLong(INDEX_LONG, DATA_LONG)
    client.WriteDouble(INDEX_DOUBLE, DATA_DOUBLE)

def check_data(client):
    assert DATA_LONG == client.ReadLong(INDEX_LONG)
    assert DATA_DOUBLE == client.ReadDouble(INDEX_DOUBLE)

def main():
    client = zero_cache.TypedClient()
    client.ClearCache()
    init_data(client)
    check_data(client)

if __name__ == "__main__":
    main()
