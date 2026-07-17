---
title: "[Solution] C TLS handshake failure"
description: "Fix C TLS handshake failure. Resolve SSL/TLS certificate and protocol issues."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["tls", "ssl", "handshake", "openssl", "certificate"]
weight: 5
---

# TLS handshake failure

A TLS handshake failure occurs when the client and server cannot agree on security parameters during the SSL/TLS connection establishment.

## Common Causes

```c
// Cause 1: Protocol version mismatch
// Client requires TLS 1.3, server only supports TLS 1.2

// Cause 2: Cipher suite mismatch
// No common cipher suites between client and server

// Cause 3: Certificate verification failure
// Untrusted CA, expired cert, hostname mismatch
```

## How to Fix

### Fix 1: Check OpenSSL error stack

```c
#include <openssl/err.h>

SSL_CTX *ctx = SSL_CTX_new(TLS_client_method());
SSL *ssl = SSL_new(ctx);
if (SSL_connect(ssl) <= 0) {
    ERR_print_errors_fp(stderr);
}
```

### Fix 2: Set minimum TLS version

```c
SSL_CTX_set_min_proto_version(ctx, TLS1_2_VERSION);
```

### Fix 3: Disable certificate verification (testing only)

```c
SSL_CTX_set_verify(ctx, SSL_VERIFY_NONE, NULL); // NOT for production
```

## Examples

```c
#include <openssl/ssl.h>
#include <openssl/err.h>

int main(void) {
    SSL_CTX *ctx = SSL_CTX_new(TLS_client_method());
    if (!ctx) {
        ERR_print_errors_fp(stderr);
        return 1;
    }
    
    SSL *ssl = SSL_new(ctx);
    SSL_set_fd(ssl, sock);
    
    if (SSL_connect(ssl) <= 0) {
        ERR_print_errors_fp(stderr);
    }
    
    SSL_free(ssl);
    SSL_CTX_free(ctx);
    return 0;
}
```

## Related Errors

- [Certificate expired]({{< relref "/languages/c/certificate-expired" >}}) — expired certificate.
- [Hostname mismatch]({{< relref "/languages/c/hostname-mismatch" >}}) — SSL hostname error.
- [Self-signed certificate]({{< relref "/languages/c/self-signed-certificate" >}}) — untrusted cert.
