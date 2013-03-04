#!/usr/bin/env python

import zero_cache

def check_keys(client):
    for index in range(10):
        print("%d = %d" % (index, client.ReadLong(index)))

def main():
    client = zero_cache.Client()
    check_keys(client)

if __name__ == "__main__":
    main()
