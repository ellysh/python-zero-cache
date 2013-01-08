#!/usr/bin/env python

import registrar_client

client = registrar_client.RegistrarClient("tcp_test.log", "tcp://localhost:5570", 0)

key = "key1"
data = "test data 1\0"

client.WriteData(key, data, len(data))
result = client.ReadData(key) + '\0'

assert data == result
