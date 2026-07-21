---
title: "[Solution] Ubuntu Server: ssh-host-key-changed"
description: "Fix Ubuntu ssh-host-key-changed. SSH host key changed warning on connection."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# SSH Host Key Changed

SSH client warns that host key has changed since last connection.

## Common Causes
- Server reinstalled or upgraded
- IP address now points to different server
- Man-in-the-middle attack (rare)
- /etc/ssh/ssh_host_* keys regenerated

## How to Fix
1. Remove old host key from known_hosts
```bash
ssh-keygen -R <hostname>
ssh-keygen -R <ip-address>
```
2. Connect and accept new key
```bash
ssh user@server
```
3. Verify new key fingerprint
```bash
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

## Examples
```bash
$ ssh user@server
@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!

$ ssh-keygen -R 192.168.1.100
# Host 192.168.1.100 found: line 5
# /home/user/.ssh/known_hosts updated.
```
