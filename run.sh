#!/bin/bash

DEFAULT_DAY=$(date +%d)
read -p "[*] Please enter day ($DEFAULT_DAY): " DAY
DAY=${DAY:-$DEFAULT_DAY}

cd $DAY
python3 $DAY.py