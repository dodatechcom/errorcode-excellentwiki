---
title: "[Solution] C Blocked by firewall: EACCES"
description: "Fix C blocked by firewall (EACCES). Configure firewall rules to allow connections."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Blocked by firewall: EACCES

A connection being blocked by a firewall typically manifests as EACCES (permission denied) or ECONNREFUSED (connection refused), depending on whether the firewall sends a rejection or silently drops packets.

## Common Causes

```c
// Cause 1: iptables blocking outgoing
iptables -A OUTPUT -d 10.0.0.1 -j DROP;

// Cause 2: iptables blocking incoming
iptables -A INPUT -p tcp --dport 8080 -j DROP;

// Cause 3: Security groups (cloud)
// AWS security group not allowing port
```

## How to Fix

### Fix 1: Check firewall rules

```bash
iptables -L -n -v
# or
nft list ruleset
```

### Fix 2: Allow the connection

```bash
iptables -A OUTPUT -d 10.0.0.1 -p tcp --dport 80 -j ACCEPT
```

### Fix 3: Check cloud security groups

```bash
# AWS
aws ec2 describe-security-groups

# GCP
gcloud compute firewall-rules list
```

## Examples

```bash
# Check if port is blocked
iptables -L -n | grep 8080

# Temporarily allow all (testing only!)
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
```

## Related Errors

- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
- [Connection timed out]({{< relref "/languages/c/operation-timed-out" >}}) — ETIMEDOUT.
- [Network unreachable]({{< relref "/languages/c/network-unreachable" >}}) — ENETUNREACH.
