#!/bin/sh
wget https://data.keithito.com/data/speech/LJSpeech-1.1.tar.bz2
mkdir data
tar -jxvf LJSpeech-1.1.tar.bz2
mv LJSpeech-1.1 data
sudo mkdir -p /data/checkpoint
sudo mkdir -p /data/samples/
