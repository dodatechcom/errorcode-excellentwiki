---
title: "[Solution] Git fatal: unable to look up"
description: "Fix 'unable to look up' error. Resolve Git DNS resolution failures when connecting to remote repositories."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: unable to look up

fatal: unable to look up '<hostname>' (port 9418) (Name or service not known)

This error occurs when Git cannot resolve the hostname of your remote repository server to an IP address. DNS resolution has failed.

## Common Causes

- No network connection or DNS server unreachable
- Hostname is incorrect
- DNS cache is stale or corrupted
- VPN not connected (for internal repositories)
- Network interface is down

## How to Fix

### Test DNS Resolution

```bash
nslookup github.com
dig github.com
```

### Check Network Connectivity

```bash
ping -c 4 8.8.8.8
```

### Use IP Address Instead

```bash
git remote set-url origin http://<ip-address>/user/repo.git
```

### Flush DNS Cache

```bash
# Linux
sudo systemctl restart systemd-resolved
# macOS
sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder
# Windows
ipconfig /flushdns
```

### Add to Hosts File

```bash
echo "<ip-address> github.com" >> /etc/hosts
```

## Examples

```bash
# Example 1: DNS resolution failure
git clone https://github.com/user/repo.git
# fatal: unable to look up github.com (port 443) (Name or service not known)
# Fix: check internet connection or use VPN

# Example 2: Corporate network DNS
nslookup github.com
# ** server can't find github.com: NXDOMAIN
# Fix: connect to VPN or use DNS server that resolves external domains

# Example 3: Add to hosts file as workaround
ping github.com  # get IP
echo "140.82.112.4 github.com" | sudo tee -a /etc/hosts
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
