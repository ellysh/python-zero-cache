#!/usr/bin/env python

import registrar_client

client = registrar_client.RegistrarClient()

key = "key1"
data = "test data 1"

client.WriteData(key, data, len(data))
