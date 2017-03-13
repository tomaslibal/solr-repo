#!/bin/bash

YEAR=$(date -u +"%Y")
MONTH=$(date -u +"%m")
DAY=$(date -u +"%d")
HOUR=$(date -u +"%H")
MINUTE=$(date -u +"%M")

LAT=1.367
LON_W=-103.8

OUT=$(python sunpos.py position $YEAR $MONTH $DAY $LAT $LON_W $HOUR $MINUTE)

AZIMUTH=$(echo $OUT | awk '{print $8}' | cut -d'=' -f2)
ALTITUDE=$(echo $OUT | awk '{print $10}' | cut -d'=' -f2)

python vis.py $LAT $LON_W "${HOUR}:${MINUTE}" $AZIMUTH $ALTITUDE

