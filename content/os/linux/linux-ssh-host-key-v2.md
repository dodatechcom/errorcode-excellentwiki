---
title: "[Solution] Linux SSH Host Key Verification Failed — Fix v2"
description: "Fix Linux 'ssh: Host key verification failed' errors. Accept, remove, or update SSH host keys to restore remote connections."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ssh", "host-key", "known-hosts", "fingerprint", "security", "remote-access"]
weight: 5
---

# Linux: ssh: Host key verification failed

The `Host key verification failed` error means the SSH client detected that the remote host's public key does not match what is stored in `~/.ssh/known_hosts`. This is a security feature that protects against man-in-the-middle attacks. The mismatch typically occurs when the server was reinstalled, the host key was regenerated, or someone is intercepting your connection.

## What This Error Means

When you first connect to an SSH server, the server presents its public host key. SSH stores this key in `~/.ssh/known_hosts`. On every subsequent connection, SSH compares the server's key with the stored one. If they don't match, SSH refuses to connect and warns about a potential MITM attack. This commonly happens after server reinstalls, IP address changes, or when the server's `/etc/ssh/ssh_host_*_key` files are regenerated.

## Common Causes

- Server was reinstalled or host key was regenerated
- Server IP address changed (DHCP, migration)
- Man-in-the-middle attack intercepting the connection
- Load balancer or proxy presenting a different host key
- DNS pointing to a different server than expected
- `known_hosts` file corrupted or from a different user

## How to Fix

### 1. Remove the Old Host Key

The most common fix — remove the stale entry from known_hosts:

```bash
# Remove a specific host by IP or hostname
ssh-keygen -R 192.168.1.100
ssh-keygen -R example.com

# Or manually edit known_hosts
nano ~/.ssh/known_hosts
# Find and delete the line for the host
```

### 2. Accept the New Host Key

After removing the old key, reconnect and accept the new one:

```bash
$ ssh user@192.168.1.100
The authenticity of host '192.168.1.100' can't be established.
ED25519 key fingerprint is SHA256:Abc123...
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```

### 3. Check the Host Key Fingerprint

Verify the key matches what you expect:

```bash
# On the server, get the fingerprint
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub

# Compare with what the client shows during connection
```

### 4. Fix for Multiple IPs on Same Host

If the host has multiple IPs and you connect using different ones:

```bash
# Remove all entries for the host
ssh-keygen -R hostname
ssh-keygen -R 192.168.1.100
ssh-keygen -R 10.0.0.100

# Reconnect to each IP to re-add
ssh user@hostname
ssh user@192.168.1.100
ssh user@10.0.0.100
```

### 5. Use StrictHostKeyChecking for Automation

For scripts and automated connections (less secure):

```bash
# Disable host key checking for a specific host
ssh -o StrictHostKeyChecking=no user@host

# In ssh_config (~/.ssh/config):
Host hostalias
    HostName 192.168.1.100
    User user
    StrictHostKeyChecking=no
    UserKnownHostsFile=/dev/null
```

### 6. Backup and Restore known_hosts

```bash
# Backup known_hosts before changes
cp ~/.ssh/known_hosts ~/.ssh/known_hosts.backup

# Restore if something goes wrong
cp ~/.ssh/known_hosts.backup ~/.ssh/known_hosts
```

### 7. Use Certificate-Based Authentication

Avoid host key issues entirely with SSH certificates:

```bash
# On the server, sign the host key
ssh-keygen -s ca_key -I host_key -h -V +52w /etc/ssh/ssh_host_ed25519_key.pub

# On the client, trust the CA
@cert-authority *.example.com ssh-ed25519 AAAAC3...ca_key...
```

## Examples

```bash
$ ssh user@192.168.1.100
@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:Abc123def456...
Please contact your system administrator.
Add correct host key in ~/.ssh/known_hosts to get rid of this message.

$ ssh-keygen -R 192.168.1.100
# Host 192.168.1.100 found: line 5
# /home/user/.ssh/known_hosts updated.

$ ssh user@192.168.1.100
The authenticity of host '192.168.1.100' can't be established.
ED25519 key fingerprint is SHA256:NewKey123...
Are you sure you want to continue connecting (yes/no)? yes
```

## Related Errors

- [SSH connection refused]({{< relref "/os/linux/linux-ssh-connection-refused-v2" >}}) — SSH server not running
- [SSH permission denied]({{< relref "/os/linux/linux-ssh-permission-denied" >}}) — Authentication failures
- [SSH permission denied]({{< relref "/os/linux/ssh-error" >}}) — SSH authentication and connection issues
