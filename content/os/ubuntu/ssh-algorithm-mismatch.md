---
title: "[Solution] Ubuntu Server: ssh-algorithm-mismatch"
description: "Fix Ubuntu ssh-algorithm-mismatch. SSH client and server cannot agree on key exchange algorithm."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# SSH Algorithm Mismatch

SSH client and server cannot agree on algorithms.

## Common Causes
- Client uses old algorithms not supported by server
- Server configured to use only new algorithms
- Host key algorithm not enabled on one side
- DiffieHellman key exchange mismatch

## How to Fix
1. Check supported algorithms
```bash
ssh -Q kex
ssh -Q hostkey
```
2. Enable legacy algorithms temporarily
```bash
ssh -o KexAlgorithms=+diffie-hellman-group14-sha256 user@server
```
3. Update server config
```bash
sudo nano /etc/ssh/sshd_config
KexAlgorithms curve25519-sha256,ecdh-sha2-nistp256,diffie-hellman-group14-sha256
sudo systemctl restart sshd
```

## Examples
```bash
$ ssh -v user@server
Unable to negotiate with 192.168.1.100 port 22: no matching host key found
```

write_page "ssh-connection-refused" \
"[Solution] Ubuntu Server: ssh-connection-refused" \
"Fix Ubuntu ssh-connection-refused. SSH connection is actively refused by the server." \
#
