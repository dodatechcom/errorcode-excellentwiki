---
title: "[Solution] Linux iptables 'No chain/target/match' Error — Firewall Fix"
description: "Fix Linux iptables 'No chain/target/match by that name' errors. Resolve firewall rule issues, missing modules, and iptables configuration problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: iptables: No chain/target/match by that name

The `iptables: No chain/target/match by that name` error means iptables cannot find the specified chain, target, or match module. This happens when a required kernel module is not loaded, the iptables version doesn't support a feature, the syntax is wrong, or you're trying to use a match/target that isn't installed. It can also occur if the kernel was updated without matching iptables modules.

## Common Causes

- Required kernel module not loaded (e.g., `xt_state`, `xt_conntrack`)
- iptables version mismatch with kernel modules
- Incorrect iptables syntax or typo in chain/target name
- Using a match or target from an uninstalled package (e.g., `iptables-persistent`)
- Kernel updated without matching netfilter modules
- Trying to use iptables on a system using nftables backend

## How to Fix

### 1. Check Loaded Kernel Modules

```bash
# List loaded netfilter modules
lsmod | grep -E 'ip_|nf_|xt_|ipt_'

# Check if the specific module exists
modprobe -n -v xt_conntrack
```

### 2. Load Missing Modules

```bash
# Load the state module (commonly needed)
sudo modprobe xt_state

# Load connection tracking
sudo modprobe xt_conntrack

# Load common match modules
sudo modprobe xt_tcpudp
sudo modprobe xt_LOG
sudo modprobe xt_REJECT

# Load NAT modules
sudo modprobe ipt_MASQUERADE
sudo modprobe iptable_nat

# Make modules load on boot
echo "xt_state" | sudo tee -a /etc/modules
echo "xt_conntrack" | sudo tee -a /etc/modules
```

### 3. Check iptables Version

```bash
# Check iptables version
iptables --version

# List available targets
iptables -j | head -20

# List available matches
iptables -m help 2>&1 | head -20
```

### 4. Fix Syntax Errors

Common iptables syntax mistakes:

```bash
# Wrong: misspelled chain
iptables -A INPUF -p tcp --dport 80 -j ACCEPT
# Correct:
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Wrong: missing dash before option
iptables -A INPUT ptcp --dport 80 -j ACCEPT
# Correct:
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Check existing rules to see correct syntax
iptables -L -n -v
```

### 5. Handle iptables/nftables Conflict

Modern systems may use nftables as the backend:

```bash
# Check if nftables is the backend
iptables --version
# If it says "nf_tables" backend, nftables is being used

# Check nftables rules
sudo nft list ruleset

# Switch to iptables-legacy if needed
sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy
```

### 6. Install Required Packages

```bash
# Debian/Ubuntu
sudo apt install iptables iptables-persistent

# RHEL/CentOS/Fedora
sudo dnf install iptables iptables-services
```

### 7. Reset iptables Rules

If rules are corrupted:

```bash
# Flush all rules
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X

# Set default policies
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT

# Save clean rules
sudo iptables-save > /etc/iptables/rules.v4
```

## Examples

```bash
$ sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables: No chain/target/match by that name.

$ lsmod | grep xt_state
# No output — module not loaded

$ sudo modprobe xt_state
$ sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
# Works now
```

## Related Errors

- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Firewall blocking connections
- [SELinux denied]({{< relref "/os/linux/selinux-denied" >}}) — Security policy blocking access
- [NFS not responding]({{< relref "/os/linux/nfs-error" >}}) — NFS firewall issues
