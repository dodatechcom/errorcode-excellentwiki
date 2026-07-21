---
title: "[Solution] Apache HTTP/2 Error"
description: "Fix Apache HTTP/2 protocol errors when h2 connections fail or fall back to HTTP/1.1."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache HTTP/2 Error

Apache HTTP/2 module fails to establish or maintain HTTP/2 connections.

```
AH01630: client denied by server configuration (HTTP/2)
```

## Common Causes

- mod_http2 not loaded or improperly configured
- TLS not configured for HTTP/2
- Incompatible modules loaded alongside mod_http2
- Connection pool limits exceeded
- ALPN negotiation failed

## How to Fix

### Enable HTTP/2

```bash
a2enmod http2
systemctl restart apache2
```

### Basic HTTP/2 Configuration

```apache
# Enable HTTP/2 with TLS
Protocols h2 h2c http/1.1

# Set H2 engine
H2Engine on

# Configure TLS (required for h2)
SSLEngine on
SSLCertificateFile /etc/ssl/certs/ssl-cert-snakeoil.pem
SSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key
```

### Enable HTTP/2 Without TLS (h2c)

```apache
# For local or proxy scenarios
Protocols h2c http/1.1

<VirtualHost *:80>
    Protocols h2c http/1.1
    H2Engine on
</VirtualHost>
```

### Limit Connections

```apache
# Prevent resource exhaustion
H2MaxSessionStreams 100
H2StreamTimeout 300
H2Push on
```

### Check Module Compatibility

```bash
# Verify no conflicting modules
apachectl -M | grep -E "mpm_|http2"
# mod_http2 works with event MPM, not prefork
```

## Examples

```apache
# Full HTTP/2 configuration
<IfModule mod_http2.c>
    Protocols h2 h2c http/1.1
    H2Engine on
    H2MaxSessionStreams 100
    H2StreamTimeout 300
    H2Push on
    H2PushPriority * after
</IfModule>

# Per-virtual host
<VirtualHost *:443>
    Protocols h2 http/1.1
    H2Engine on
    SSLEngine on
</VirtualHost>
```
