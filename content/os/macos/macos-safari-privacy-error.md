---
title: "[Solution] macOS Safari Privacy Error -- Safari Cannot Verify Website Identity"
description: "Fix macOS Safari privacy error when Safari shows 'This connection is not private' or certificate warnings. Resolve Safari SSL errors."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Safari Privacy Error -- Safari Cannot Verify Website Identity

Safari shows privacy errors when it cannot verify a website's SSL/TLS certificate. The most common message is 'This connection is not private' with a warning not to proceed.

## Common Causes
- Website has an expired or self-signed SSL certificate
- System date and time are incorrect
- Corporate proxy is intercepting HTTPS traffic
- Root certificate authority is not trusted by macOS
- Antivirus software is intercepting SSL connections

## How to Fix
1. Check and correct the system date and time
2. Ensure the website's SSL certificate is valid (not expired)
3. If on a corporate network, install the corporate root certificate
4. Temporarily disable antivirus SSL scanning
5. Try a different network to rule out proxy issues

```bash
# Check system date
date

# Check trusted certificates
security find-certificate -a -c "Corporate Root" /Library/Keychains/System.keychain
```

## Examples

```bash
# Test SSL certificate from terminal
openssl s_client -connect example.com:443 -servername example.com < /dev/null 2>&1 | grep -A 2 "Certificate chain"
```

This error is common when the system clock is incorrect, when a corporate proxy intercepts HTTPS, or when a website has an expired or misconfigured SSL certificate.
