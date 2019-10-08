#! /bin/sh

curl --silent $1 | grep -Eoi 'href="[^\"]+"' | cut -c 7- | rev | cut -c 2- | rev