---
title: "[Solution] Systemd Networkd Configuration Error — How to Fix"
description: "Fix systemd-networkd configuration errors by validating .network files, resolving IP assignment issues, fixing DNS configuration, and debugging link states"
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Systemd Networkd Configuration Error

This error means systemd-networkd failed to configure a network interface. This can result in no network connectivity, incorrect IP addresses, or DNS resolution failures.

## Why It Happens

- The `.network` file has syntax errors or invalid directives
- The `Match` section does not match the correct interface name
- The static IP configuration has a subnet mask or gateway error
- DNS configuration points to unreachable servers
- The link file in `/etc/systemd/network/` conflicts with another network manager
- NetworkManager and systemd-networkd are both managing the same interface
- The DHCP server is not responding or the lease expired
- VLAN or bonding configuration is incorrect

## Common Error Messages

```
systemd-networkd: eth0: Could not bring interface up: No such device
```

```
systemd-networkd: eth0: Failed to set route: Network is unreachable
```

```
systemd-networkd: eth0: DHCPv4 client: No route to host
```

```
systemd-networkd: Configuration file ... is not trusted. Ignoring.
```

## How to Fix It

### 1. Check Networkd Status

```bash
# Check networkd status
systemctl status systemd-networkd

# Check networkd logs
journalctl -u systemd-networkd -n 50 --no-pager

# List all network interfaces
networkctl status

# Check which files are being applied
networkctl list
```

### 2. Verify Interface Name Matching

```bash
# Find the correct interface name
ip link show

# Common names: eth0, ens3, enp0s3, wlan0
# Check what networkd sees
networkctl status eth0
```

```ini
# /etc/systemd/network/10-eth0.network
[Match]
Name=eth0

[Network]
DHCP=no

[Address]
Address=192.168.1.100/24

[Route]
Gateway=192.168.1.1
```

### 3. Fix Static IP Configuration

```ini
# Correct static IP configuration
[Match]
Name=eth0

[Network]
Address=192.168.1.100/24
Gateway=192.168.1.1
DNS=8.8.8.8
DNS=8.8.4.4

# Or use separate sections
[Address]
Address=192.168.1.100/24

[Route]
Gateway=192.168.1.1
Destination=0.0.0.0/0

[DNS]
DNS=8.8.8.8
```

### 4. Fix DHCP Configuration

```ini
# /etc/systemd/network/20-dhcp.network
[Match]
Name=eth*

[Network]
DHCP=yes

[DHCP]
UseDNS=yes
UseNTP=yes
RouteMetric=100
```

### 5. Resolve Conflicts with NetworkManager

```bash
# Check which network manager is active
systemctl status systemd-networkd
systemctl status NetworkManager

# If both are running, disable one
sudo systemctl disable --now NetworkManager
sudo systemctl enable --now systemd-networkd

# Or if you want to use NetworkManager instead
sudo systemctl disable --now systemd-networkd
sudo systemctl enable --now NetworkManager
```

### 6. Validate and Restart Networkd

```bash
# Check configuration syntax
systemd-networkd --verify

# Restart networkd after changes
sudo systemctl restart systemd-networkd

# Force re-evaluation of link files
sudo networkctl reconfigure eth0
```

## Common Scenarios

- **Cloud VM with different interface name**: The VM uses `ens3` instead of `eth0`. Update the `Name=` match or use `MACAddress=` to match by MAC.
- **Dual-stack IPv4/IPv6**: A configuration file only sets IPv4 but the network requires IPv6. Add an `[Address]` section with the IPv6 address and gateway.
- **NetworkManager conflict**: Both NetworkManager and systemd-networkd are enabled. Disable the one you are not using.

## Prevent It

- Use `systemd-networkd --verify` to validate configuration files before deploying
- Only enable one network manager per system (either NetworkManager or systemd-networkd)
- Use `networkctl status` after every change to verify the interface is configured correctly

## Related Pages

- [Systemd Mount Error](/tools/systemd/systemd-mount-error)
- [Systemd Unit Failed](/tools/systemd/systemd-unit-failed)
- [Systemd Sysctl Error](/tools/systemd/systemd-sysctl-error)
