import os
import sys
username = sys.argv[1]
copy = ['data', 'Downloads', 'playlists', 'czplayer.py', 'LICENSE', 'play.py', 'read_write.py', 'readme.md', 'remove.py', 'setup.py', 'songdl.py']
os.system('mkdir -p ~/bin')
for path in copy:
    if not os.path.exists('~/bin/' + path):
        os.system('cp -r ' + path + ' ~/bin/')
        os.system('chmod +x ~/bin/' + path)
        os.system('chown -R ' + username + ' ~/bin/' + path)
    else:
        raise Exception('Unable to install CZPlayer. ~/bin/' + path + ' already exists.')

os.system('mv ~/bin/czplayer.py ~/bin/czplayer')
os.system('chown -R ' + username + ' ~/bin')
os.system('export PATH=$PATH":$HOME/bin"')
print("CZPlayer successfully installed!")
