---
title: "[Solution] Conda Channel SSL Error -- Fix SSL Certificate Issues"
description: "Fix conda channel SSL error when SSL certificate verification fails for a conda channel. Configure certificates and SSL settings."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda's SSL connection to a channel failed certificate verification. Packages cannot be downloaded from that channel.

## Common Causes

- Corporate proxy intercepts HTTPS with custom CA
- System CA certificates are outdated
- The channel server has an expired certificate
- Python's SSL module lacks the required CA bundle

## How to Fix

### 1. Update CA Certificates

```bash
sudo apt update && sudo apt install ca-certificates
sudo update-ca-certificates
```

### 2. Disable SSL Verification (Temporary)

```bash
conda config --set ssl_verify false
```

### 3. Set Custom CA Bundle

```bash
conda config --set ssl_verify /path/to/custom-ca-bundle.crt
```

### 4. Use HTTP Instead (Last Resort)

```bash
conda config --add channels http://mirrors.example.com/anaconda/pkgs/main
```

## Examples

```bash
$ conda install numpy
SSLError: SSL certificate verify failed

$ conda config --set ssl_verify false
$ conda install numpy
Solving environment: done
```
