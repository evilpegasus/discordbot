#!/bin/bash

pkill -9 -f mingbot.py
nohup python3 ~/discordbot/mingbot.py > test.txt 2>&1 </dev/null &