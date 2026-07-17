---
title: "[Solution] Linux /etc/resolv.conf DNS Error — Fix"
description: "Fix Linux DNS resolution errors in /etc/resolv.conf. Resolve 'Temporary failure in name resolution' and configure DNS correctly."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: /etc/resolv.conf DNS error

The `/etc/resolv.conf` DNS error occurs when the system cannot resolve domain names. The file `resolv.conf` configures DNS name servers — if it is missing, empty, misconfigured, or overwritten, name resolution fails.

## Common Causes

- Empty or missing /etc/resolv.conf
- Incorrect nameserver IP addresses
- Network manager overwrote custom DNS settings
- resolvconf/systemd-resolved package misconfiguration
- Network connectivity to DNS server lost
- DNS server timeout or failure
- Symlink broken (e.g., /etc/resolv.conf -> ../run/systemd/resolve/stub-resolv.conf)

## How to Fix

### 1. Check Current DNS Configuration

```bash
# View resolv.conf
cat /etc/resolv.conf

# Check if it's a symlink
ls -la /etc/resolv.conf

# Test DNS resolution
nslookup google.com
dig google.com
host google.com
```

### 2. Temporarily Set DNS Servers

```bash
# Override with Google DNS
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
echo "nameserver 8.8.4.4" | sudo tee -a /etc/resolv.conf

# Test again
nslookup google.com
```

### 3. Configure DNS Permanently (NetworkManager)

```bash
# Edit the connection
nmcli con show
sudo nmcli con mod "Wired connection 1" ipv4.dns "8.8.8.8 8.8.4.4"
sudo nmcli con mod "Wired connection 1" ipv4.ignore-auto-dns yes
sudo nmcli con down "Wired connection 1"
sudo nmcli con up "Wired connection 1"
```

### 4. Configure DNS Permanently (systemd-networkd)

```bash
# Edit the network config
sudo nano /etc/systemd/network/20-wired.network

# Add:
# [Network]
# DNS=8.8.8.8
# DNS=8.8.4.4

sudo systemctl restart systemd-networkd
```

### 5. Fix systemd-resolved Issues

```bash
# Check systemd-resolved status
sudo systemctl status systemd-resolved

# Restart it
sudo systemctl restart systemd-resolved

# Check resolved DNS
resolvectl status

# Flush DNS cache
sudo resolvectl flush-caches
```

### 6. Prevent resolv.conf from Being Overwritten

```bash
# Make resolv.conf immutable (not recommended for dynamic systems)
sudo chattr +i /etc/resolv.conf

# Or configure NetworkManager to not manage DNS
sudo nano /etc/NetworkManager/NetworkManager.conf
# Add under [main]:
# dns=none

sudo systemctl restart NetworkManager
```

### 7. Configure DNS via /etc/resolvconf (Legacy)

```bash
# Edit the base configuration
sudo nano /etc/resolvconf/resolv.conf.d/base

# Add nameservers:
# nameserver 8.8.8.8
# nameserver 8.8.4.4

# Regenerate resolv.conf
sudo resolvconf -u
```

### 8. Test DNS Connectivity

```bash
# Check if DNS server is reachable
nc -zv 8.8.8.8 53
nc -zvu 8.8.8.8 53

# Check if local resolver is working
ss -tulpn | grep 53
```

## Examples

```bash
$ cat /etc/resolv.conf
# Empty file

$ nslookup google.com
;; connection timed out; no servers could be reached

$ echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
$ nslookup google.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	google.com
Address: 142.250.80.14
```

```bash
$ ls -la /etc/resolv.conf
/etc/resolv.conf -> /run/systemd/resolve/stub-resolv.conf

$ cat /etc/resolv.conf
nameserver 127.0.0.53
options edns0 trust-ad

# Check if systemd-resolved is running
$ sudo systemctl status systemd-resolved
```

## Related Errors

- [NetworkManager error]({{< relref "/os/linux/linux-network-manager" >}}) — Network configuration issues
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Network connectivity issues
- [dig server failure]({{< relref "/os/linux/linux-dig-error" >}}) — DNS query failures
