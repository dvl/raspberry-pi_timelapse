#!/bin/bash
# https://trac.ffmpeg.org/wiki/Slideshow

TIMESTAMP=`date +%Y%m%d`

ffmpeg -framerate 120 -pattern_type glob -i "images/img_*.png" -c:v libx264 -pix_fmt yuv420p "videos/${TIMESTAMP}.mp4"
