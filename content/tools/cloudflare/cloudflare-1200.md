---
title: "[Solution] Cloudflare 1200 Error — SSL/TLS Protocol Error"
description: "Fix Cloudflare Error 1200 when SSL/TLS connection between Cloudflare and origin fails. Resolve cipher mismatches, protocol versions, and certificate issues."
tools: ["cloudflare"]
error-types: ["ssl-error"]
severities: ["error"]
weight: 5
---

Cloudflare Error 1200 occurs when the SSL/TLS handshake between Cloudflare and the origin server fails. No secure connection can be established.

## What This Error Means

Cloudflare attempts to connect to your origin server over SSL/TLS, but the handshake fails. This is different from certificate errors (526, 527) as it indicates a protocol-level failure.

## Why It Happens

- The origin server does not support SSL/TLS at all (plain HTTP only)
- Cipher mismatch between Cloudflare and the origin's SSL configuration
- The origin uses an outdated SSL protocol version (SSLv3, TLS 1.0)
- The origin certificate is self-signed and rejected during the handshake
- The origin certificate has an incorrect key usage or extended key usage
- The origin server configuration requires SNI but does not support it properly
- Firewall or reverse proxy is intercepting the SSL connection

## How to Fix It

### Check Origin SSL Configuration

```bash
openssl s_client -connect your-origin.com:443 -servername your-origin.com
```

### Test with Different TLS Versions

```bash
openssl s_client -tls1_2 -connect your-origin.com:443
openssl s_client -tls1_3 -connect your-origin.com:443
```

### Configure SSL Mode in Cloudflare

In Cloudflare dashboard, set SSL/TLS encryption mode:
- **Full**: Requires a certificate on the origin (can be self-signed)
- **Full (strict)**: Requires a valid CA-signed certificate
- **Flexible**: Not recommended; only encrypts browser-to-Cloudflare

### Update Origin SSL Ciphers

```nginx
# nginx configuration
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
```

### Enable SSL on the Origin

```bash
# If the origin only supports HTTP, enable SSL:
# nginx
sudo apt install nginx
sudo nano /etc/nginx/sites-available/default
# Add SSL configuration
```

### Check for Intercepting Proxies

Ensure no intermediate proxy (load balancer, reverse proxy) is interfering with the SSL handshake.

## Common Mistakes

- Using SSL mode Full (strict) with a self-signed certificate
- Not enabling TLS 1.2 or higher on the origin server
- Configuring ciphers that Cloudflare does not support
- Forgetting that Flexible mode sends plain HTTP from Cloudflare to origin

## Related Pages

- [Cloudflare 1303 Error]({{< relref "/tools/cloudflare/cloudflare-1303" >}}) -- SSL certificate error
- [Cloudflare 525 Error]({{< relref "/tools/cloudflare/cloudflare-525" >}}) -- SSL handshake failed
- [Cloudflare 526 Error]({{< relref "/tools/cloudflare/cloudflare-526" >}}) -- Invalid SSL certificate
