import os
import sys
sudo_pass = sys.argv[0]
username = sys.argv[1]
os.system('echo ' + sudo_pass + ' | sudo -S mv czplayer.py /usr/local/bin/czplayer')
os.system('echo ' + sudo_pass + ' | sudo -S chown -R ' + username + ' /usr/local/CZPlayer')
