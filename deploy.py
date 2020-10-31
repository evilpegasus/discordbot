from __future__ import print_function,unicode_literals
import subprocess
from time import sleep
"""
HOW TO DEPLOY THE BOT (LINUX)
1. Run this file to copy new mingbot.py to host machine
2. SSH into host machine and cd to ~/discordbot
3. Run start.bash on host machine to kill old bot process and start a new one
"""
# subprocess.run(r"scp -i ocf_key .\mingbot.py .\secrets.py .\start.bash mingfong@ssh.ocf.berkeley.edu:~/discordbot")
subprocess.run(r"scp -i ocf_key .\mingbot.py mingfong@ssh.ocf.berkeley.edu:~/discordbot")

sshProcess = subprocess.Popen(['ssh', '-i', 'ocf_key',
                               'mingfong@ssh.ocf.berkeley.edu'],
                               stdin = subprocess.PIPE,
                               stdout = subprocess.PIPE,
                               universal_newlines = True,
                               bufsize = 0)
# sshProcess.stdin.write("killall python3\n")
# sshProcess.stdin.write("nohup python3 ~/discordbot/mingbot.py > test.txt 2>&1 </dev/null &\n")

# sshProcess.stdin.write("chmod 755 ~/discordbot/start.bash\n")
# sshProcess.stdin.write("./start.bash\n")
sshProcess.stdin.close()

# subprocess.run(r"scp -i ocf_key .\mingbot.py .\secrets.py mingfong@ssh.ocf.berkeley.edu:~/discordbot")
# subprocess.run(r"ssh -i .\ocf_key mingfong@ssh.ocf.berkeley.edu 'pkill -9 -f mingbot.py; nohup python3 ~/discordbot/mingbot.py > test.txt 2>&1 </dev/null &'")

for line in sshProcess.stdout:
    if line == "END\n":
        break
    print(line,end="")

print("Finished deploying")