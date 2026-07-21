---
title: "[Solution] Linux: network-dns-cache-pollution -- DNS cache pollution"
description: "Fix Linux DNS cache pollution errors. DNS cache pollution causing incorrect name resolution."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: DNS Cache Pollution

DNS cache pollution occurs when incorrect or malicious DNS entries are stored in cache.

## Common Causes

- DNS spoofing attack injecting bad records
- Upstream DNS server returning poisoned responses
- Local /etc/hosts overriding DNS with stale entries
- mDNS responding with cached stale data
- dnsmasq caching negative responses too long

## How to Fix

### 1. Flush DNS Cache

```bash
sudo resolvectl flush-caches
sudo /etc/init.d/nscd restart 2>/dev/null
```

### 2. Check Hosts File

```bash
cat /etc/hosts
grep -v "^#" /etc/hosts | grep -v "^$"
```

### 3. Verify Resolution

```bash
dig example.com +norecurse
dig +trace example.com
nslookup example.com 8.8.8.8
```

## Examples

```bash
$ dig example.com +short
192.168.1.100
# Should not be a private IP for public domain
$ sudo resolvectl flush-caches
$ dig example.com +short
93.184.216.34
```
