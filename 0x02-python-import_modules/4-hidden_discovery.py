#!/usr/bin/python3
import hidden_4 as hidden
import sys

if __name__ != '__main__':
    exit()

for item in dir(hidden):
    if item[0:2] != "__":
        print(item)
