scp -i ocf_key .\mingbot.py .\secrets.py mingfong@ssh.ocf.berkeley.edu:~/discordbot

ssh -i .\ocf_key mingfong@ssh.ocf.berkeley.edu
pkill -9 -f mingbot.py
nohup python3 ~/discordbot/mingbot.py