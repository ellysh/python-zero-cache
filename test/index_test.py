#!/usr/bin/env python

import zero_cache

def print_index(client):
    for index in range(10):
        print("%d = %d" % (index, client.ReadLong(index)))

def main():
    client = zero_cache.Client()
    print_index(client)

if __name__ == "__main__":
    main()
