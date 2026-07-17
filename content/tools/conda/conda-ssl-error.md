---
title: "[Solution] Conda SSL Error — Fix Certificate Errors With Channels"
description: "Fix conda SSL certificate errors when connecting to channels and downloading packages. Update CA bundles and configure corporate proxy SSL settings correctly."
tools: ["conda"]
error-types: ["ssl-error"]
severities: ["error"]
weight: 5
---

This error means conda could not verify the SSL certificate of a channel server. The connection is blocked before any package data is transferred, preventing all installs and updates.

## What This Error Means

conda uses Python's `ssl` module to verify channel certificates. When verification fails, you see:

```
SSLError

HTTPSConnectionPool(host='repo.anaconda.com', port=443): Max retries exceeded: SSL: CERTIFICATE_VERIFY_FAILED
```

Or:

```
CondaSSLError

Encountered an SSL error. SSL validation is disabled.
```

## Why It Happens

- The system CA certificate bundle is outdated or missing (common in Docker images)
- A corporate proxy is performing SSL inspection with a private CA
- Python was compiled without proper SSL support
- The system clock is wrong, making valid certificates appear expired
- conda's `ssl_verify` setting is pointing to a certificate file that does not exist

## How to Fix It

### Update CA Certificates

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install ca-certificates

# macOS
brew install openssl

# Fedora/RHEL
sudo dnf install ca-certificates
```

### Point conda to the System Certificate Bundle

```bash
conda config --set ssl_verify /etc/ssl/certs/ca-certificates.crt
```

### Disable SSL Verification (Temporary Only)

```bash
conda config --set ssl_verify False
```

This is insecure. Only use while diagnosing and fix the root cause immediately.

### Install Corporate CA Certificate

```bash
conda config --set ssl_verify /path/to/corporate-ca-bundle.crt
```

### Fix Python's SSL Module

```bash
python -c "import ssl; print(ssl.get_default_verify_paths())"
```

If this shows missing paths, reinstall Python with SSL support:

```bash
conda install python=3.11 --force-reinstall
```

### Sync System Clock

```bash
sudo timedatectl set-ntp true
date
```

An incorrect clock invalidates every certificate on the system.

### Clear DNS Cache

```bash
sudo systemd-resolve --flush-caches
nslookup repo.anaconda.com
```

## Common Mistakes

- Leaving `ssl_verify False` in conda config permanently
- Not updating CA certificates after cloning a minimal Docker image
- Forgetting that Python built from source may lack SSL
- Blaming conda when the problem is a system-level certificate issue

## Related Pages

- [Conda Channel Error]({{< relref "/tools/conda/conda-channel-error" >}}) -- channel and package lookup errors
- [Conda Update Error]({{< relref "/tools/conda/conda-update-error" >}}) -- update failures
- [Conda Environment Error]({{< relref "/tools/conda/conda-environment-error" >}}) -- environment issues
