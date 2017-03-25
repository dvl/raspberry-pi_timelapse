#!/bin/bash

TIMESTAMP=`date +%Y%m%d`

ffmpeg -r 120 -pattern_type glob -i "images/img_*.png" -vf format=yuv420p "videos/${TIMESTAMP}.mp4"
