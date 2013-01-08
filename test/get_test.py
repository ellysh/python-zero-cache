#!/usr/bin/env python

import registrar_client

client = registrar_client.RegistrarClient("get_test.log", "ipc:///var/run/zero-cache/0", 0)

key = "key1"
data = "test data 1"

client.WriteData(key, data, len(data))
print client.ReadData(key)
