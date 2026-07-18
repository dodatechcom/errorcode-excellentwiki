---
title: "[Solution] Conda SSL Certificate Verification Failed Error — How to Fix"
description: "Fix conda SSL certificate verification failed errors. Update CA bundles, configure corporate proxy SSL, and resolve channel connection issues quickly."
tools: ["conda"]
error-types: ["ssl-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means conda could not verify the SSL certificate of a channel server. The connection is rejected before any package data is transferred, blocking all installs and updates from HTTPS channels.

## Why It Happens

- The system CA certificate bundle is outdated or missing (common in Docker images and minimal installs)
- A corporate proxy is performing SSL interception with a private CA certificate that conda does not trust
- Python was compiled from source without proper SSL module support
- The system clock is set incorrectly, making valid certificates appear expired or not-yet-valid
- conda's `ssl_verify` configuration points to a certificate file that does not exist or is corrupted
- A firewall or security appliance is rewriting SSL certificates on the fly

## Common Error Messages

```
SSLError: HTTPSConnectionPool(host='repo.anaconda.com', port=443):
Max retries exceeded with url: /pkgs/main/...
Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED]
certificate verify failed: self signed certificate in certificate chain'))
```

```
CondaSSLError: Encountered an SSL error.
SSLError(MaxRetryError('HTTPSConnectionPool(...): Max retries exceeded ...
SSL: CERTIFICATE_VERIFY_FAILED'))
```

```
SSLError: HTTPSConnectionPool(host='conda.anaconda.org', port=443):
Max retries exceeded: SSL: DH_KEY_TOO_SMALL
```

```
ReadOnlyError: Conda could not verify the SSL certificate of the URL
https://repo.anaconda.com/pkgs/main/noarch/...
```

## How to Fix It

### 1. Update System CA Certificates

```bash
# Debian / Ubuntu
sudo apt update && sudo apt install --reinstall ca-certificates

# macOS (via Homebrew)
brew install openssl && brew upgrade ca-certificates

# Fedora / RHEL / CentOS
sudo dnf install --reinstall ca-certificates

# Alpine
apk add --no-cache ca-certificates
```

After updating, update the certificate store:

```bash
# Debian / Ubuntu
sudo update-ca-certificates

# RHEL / Fedora
sudo update-ca-trust
```

### 2. Point conda to the System Certificate Bundle

```bash
# Find the bundle path
openssl version -d

# Set it in conda config
conda config --set ssl_verify /etc/ssl/certs/ca-certificates.crt
```

Verify it works:

```bash
conda config --show ssl_verify
conda install numpy  # test download
```

### 3. Install a Corporate CA Certificate

If your network uses SSL inspection, you must add the proxy's CA certificate:

```bash
# Copy the corporate CA bundle
sudo cp corporate-ca-bundle.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates

# Point conda to the updated bundle
conda config --set ssl_verify /etc/ssl/certs/ca-certificates.crt
```

For per-user configuration:

```bash
mkdir -p ~/.conda
cat > ~/.condarc << 'EOF'
ssl_verify: /home/$USER/.conda/corporate-ca.pem
EOF
```

### 4. Disable SSL Verification (Temporary Diagnostic Only)

```bash
conda config --set ssl_verify False
```

This is insecure and should only be used to confirm the problem is SSL-related. Re-enable verification immediately:

```bash
conda config --set ssl_verify True
```

### 5. Fix Python's SSL Module

```bash
python -c "import ssl; print(ssl.get_default_verify_paths())"
```

If paths show as missing, reinstall Python with SSL support through conda:

```bash
conda install python=3.11 --force-reinstall
```

### 6. Sync the System Clock

An incorrect clock invalidates every certificate on the system:

```bash
# Check current time
date

# Enable NTP sync
sudo timedatectl set-ntp true

# Manual sync if NTP is unavailable
sudo ntpdate time.nist.gov
```

## Common Scenarios

**Docker builds fail during conda install.** Minimal Docker images like `python:3.11-slim` often lack CA certificates. Add this to your Dockerfile before any conda commands:

```dockerfile
RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates
```

**Corporate laptop cannot reach any channel.** Your company's proxy rewrites SSL certificates. Export the corporate CA bundle and point conda at it. You may also need to configure `http_proxy` and `https_proxy` environment variables.

**conda works in one environment but not another.** Each conda environment has its own Python with potentially different SSL configurations. Run `python -c "import ssl; print(ssl.get_default_verify_paths())"` inside each environment to compare.

## Prevent It

1. Always install `ca-certificates` in Docker images and CI environments before running conda commands
2. Never leave `ssl_verify: False` in your `.condarc` permanently — fix the root cause and re-enable verification
3. Keep your system clock synchronized with NTP to prevent certificate timestamp validation failures
