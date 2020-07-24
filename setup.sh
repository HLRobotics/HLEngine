#!/bin/bash
echo "Hyper Library Dynamic Integration Technology 2020";
echo "HL Engine Setup 2020 ";

wait
sudo apt-get update
wait
sudo apt-get install idle3
wait
sudo apt-get install python3-pip
wait
sudo apt-get install python-pyaudio python3-pyaudio 
wait
sudo apt-get install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools
wait
sudo apt-get install motion
wait
sudo apt-get install sox
wait
sudo apt-get install sox libsox-fmt-all
wait
sudo apt install libespeak1
wait
sudo apt-get install python3-pygame
wait
sudo apt-get install python3-bluez
wait
sudo apt-get install qttools5-dev-tools
wait
sudo apt-get install qttools5-dev
wait
python3 HLEngine_EnvironmentSetup.py &
wait
gif-for-cli "HL_Flags/updating_HLEngine.gif"
echo "HL Engine Installation 2020 [Completed] ";
