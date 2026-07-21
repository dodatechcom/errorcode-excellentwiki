---
title: "[Solution] Ubuntu Server: ssh-permission-denied-publickey"
description: "Fix Ubuntu ssh-permission-denied-publickey. SSH authentication by public key is denied."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# SSH Permission Denied Publickey

SSH server rejects public key authentication.

## Common Causes
- Authorized_keys file has wrong permissions
- Public key not added to authorized_keys
- SSH server configured to disable pubkey auth
- SELinux or AppArmor blocking access
- Home directory or .ssh permissions wrong

## How to Fix
1. Check SSH server config
```bash
sudo grep -i PubkeyAuthentication /etc/ssh/sshd_config
```
2. Fix authorized_keys permissions
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chown -R $(whoami):$(whoami) ~/.ssh
```
3. Verify key is on server
```bash
cat ~/.ssh/authorized_keys
```

## Examples
```bash
$ ssh -v user@server
debug1: Authentications that can continue: publickey
debug1: Trying private key: /home/user/.ssh/id_rsa
debug1: Authentications that can continue: publickey
Permission denied (publickey).

$ ls -la ~/.ssh/
drwx------ 2 user user 4096 .
-rw------- 1 user user  570 authorized_keys
```
