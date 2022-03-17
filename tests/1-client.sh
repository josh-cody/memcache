#!/bin/sh
cd ..
cd client
echo "set key 2 \r\n val \r\n" | python client.py
echo "get key \r\n" | python client.py
