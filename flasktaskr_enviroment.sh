#!/bin/bash

sleep 2 &&
guake -r "FlaskTaskr" -e "cd ~/Dropbox/Training/RealPython/Part2-Repo/FlaskTaskr/; workon realflask; printf '\033c'" &