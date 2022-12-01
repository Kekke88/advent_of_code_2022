#!/bin/bash

DEFAULT_DAY=$(date +%d)
read -p "[*] Please enter day ($DEFAULT_DAY): " DAY
DAY=${DAY:-$DEFAULT_DAY}

echo "[*] Creating folder.."
mkdir $DAY
cd $DAY

echo "[*] Creating files.."
touch $DAY.input
touch $DAY.py

echo "[*] Done!"