import os
import sys
sudo_pass = sys.argv[1]
username = sys.argv[2]
os.system('echo ' + sudo_pass + ' | sudo -S mv /usr/local/CZPlayer/czplayer.py /usr/local/bin/czplayer')
os.system('echo ' + sudo_pass + ' | sudo -S chown -R ' + username + ' /usr/local/CZPlayer')
