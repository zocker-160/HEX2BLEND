#! /usr/bin/env bash

import json

FILE = "mysample.json"

with open(FILE, "r") as js:
    for line in js:
        print(json.loads(line))
