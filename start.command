#!/bin/bash

cd /Users/christoph/Git/dkb-fetcher
poetry run python main.py
read -n 1 -s -r -p "Drücke eine Taste zum Beenden..."