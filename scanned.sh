#!/bin/sh

if [ "$#" -ne 2 ]
then
    echo "Usage: $0 infile outfile"
    echo "Description: Make files look like scanned for troublesome bureaucracy"
    exit 1
else
  ROTATION=$(shuf -n 1 -e '-' '')$(shuf -n 1 -e $(seq 0 .05 .5))
  magick -density 150 $1 \
    -linear-stretch '1.5%x2%' \
    -rotate ${ROTATION} \
    -attenuate '0.01' \
    +noise  Multiplicative \
    -colorspace 'gray' $2
fi

