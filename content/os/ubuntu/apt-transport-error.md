---
title: "[Solution] Ubuntu Server: apt-transport-error"
description: "Fix Ubuntu apt-transport-error. APT cannot use the specified protocol to fetch packages."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Transport Error

APT cannot use the specified protocol to fetch packages because the transport module is missing.

## Common Causes
- apt-transport-https not installed
- apt-transport-socks missing for SOCKS proxy
- Outdated transport package with TLS incompatibility
- Repository using unsupported protocol

## How to Fix
1. Install required transport package
```bash
sudo apt install apt-transport-https
```
2. For SOCKS proxy support
```bash
sudo apt install apt-transport-socks
```
3. Update after installing
```bash
sudo apt update
```

## Examples
```bash
$ sudo apt update
Err:1 https://download.docker.com/ubuntu focal stable
  Could not execute apt-key to add key

$ sudo apt install apt-transport-https
```
