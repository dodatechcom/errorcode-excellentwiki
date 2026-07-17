---
title: "[Solution] pip SSL Error — Fix Certificate Verification Failed During Install"
description: "Fix pip SSL certificate verification errors when installing packages over HTTPS. Update CA certificates and resolve corporate proxy SSL inspection issues."
tools: ["pip"]
error-types: ["ssl-error"]
severities: ["error"]
weight: 5
---

This error means pip could not verify the SSL/TLS certificate of the package index server. The download is aborted before any data is transferred, blocking the entire install.

## What This Error Means

pip requires HTTPS for all package downloads. When the SSL certificate presented by the server cannot be verified against the local certificate authority bundle, pip refuses to proceed. The error looks like:

```
ERROR: Could not find a version that satisfies the requirement <package>
SSLError: HTTPSConnectionPool: Max retries exceeded: certificate verify failed
```

## Why It Happens

- The system CA bundle is outdated or missing (common in Docker images)
- A corporate proxy or firewall is performing SSL inspection with a custom CA
- The Python installation was compiled without SSL support
- The target index server uses a self-signed or expired certificate
- Time on the machine is out of sync, making valid certificates appear expired

## How to Fix It

### Update the CA Certificates

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install ca-certificates

# macOS
brew install openssl

# Fedora/RHEL
sudo dnf install ca-certificates
```

### Install with Trusted Hosts (Temporary)

```bash
pip install <package> \
  --trusted-host pypi.org \
  --trusted-host files.pythonhosted.org
```

### Fix Corporate Proxy SSL Issues

For environments where a proxy performs SSL inspection:

```bash
export REQUESTS_CA_BUNDLE=/path/to/corporate-ca-bundle.crt
pip install <package>
```

Or point pip to the system bundle:

```bash
pip install <package> --cert /etc/ssl/certs/ca-certificates.crt
```

### Reinstall Python with SSL Support

If Python was compiled without SSL:

```bash
# Check SSL availability
python3 -c "import ssl; print(ssl.OPENSSL_VERSION)"
```

If this raises `ImportError`, rebuild Python with:

```bash
sudo apt install libssl-dev
# Then rebuild Python from source
```

### Sync System Clock

```bash
sudo timedatectl set-ntp true
date
```

An incorrect clock causes even valid certificates to fail verification.

## Common Mistakes

- Using `--trusted-host` as a permanent fix instead of updating the CA bundle
- Setting `PIP_TRUSTED_HOST` globally in pip config, which weakens security
- Forgetting to install `ca-certificates` in Docker images based on slim or alpine
- Not checking `python3 -c "import ssl"` before blaming the network

## Related Pages

- [pip Connection Error]({{< relref "/tools/pip/pip-connection-error" >}}) -- network failures during install
- [pip Install Error]({{< relref "/tools/pip/pip-install-error" >}}) -- environment errors
- [pip Version Error]({{< relref "/tools/pip/pip-version-error" >}}) -- no matching distribution found
