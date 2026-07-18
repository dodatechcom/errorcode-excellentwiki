---
title: "[Solution] C OpenSSL Error — How to Fix"
description: "Fix C OpenSSL errors including certificate verification, memory leaks, and initialization."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C OpenSSL Error — How to Fix

OpenSSL errors include SSL routines, certificate verification, and memory management. Common issues include not initializing OpenSSL, not checking SSL_get_error, and leaking SSL contexts.

## Common Error Messages

- `SSL: error:0A000086:SSL routines::certificate verify failed`
- `SSL_connect: error:14090086`
- `OpenSSL: error:0200006C:BIO routines::no start line`
- `SSL error:14094418`

## How to Fix It

### Initialize and cleanup OpenSSL

```c
#include <openssl/ssl.h>
#include <openssl/err.h>

int main(void) {
    SSL_library_init();
    SSL_load_error_strings();
    OpenSSL_add_all_algorithms();
    // ... use OpenSSL ...
    EVP_cleanup();
    ERR_free_strings();
    return 0;
}
```

### Check SSL error queue

```c
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <stdio.h>

void print_ssl_errors(void) {
    unsigned long err;
    while ((err = ERR_get_error()) != 0) {
        char buf[256];
        ERR_error_string_n(err, buf, sizeof(buf));
        fprintf(stderr, "SSL: %s\n", buf);
    }
}
```

### Use SSL_CTX with proper settings

```c
#include <openssl/ssl.h>
#include <stdio.h>

SSL_CTX *create_context(void) {
    const SSL_METHOD *method = TLS_client_method();
    SSL_CTX *ctx = SSL_CTX_new(method);
    if (!ctx) { print_ssl_errors(); return NULL; }
    SSL_CTX_set_verify(ctx, SSL_VERIFY_PEER, NULL);
    SSL_CTX_set_default_verify_paths(ctx);
    return ctx;
}
```

### Verify certificate chain

```c
#include <openssl/ssl.h>
#include <openssl/x509_vfy.h>

int verify_cert(SSL *ssl) {
    long result = SSL_get_verify_result(ssl);
    if (result != X509_V_OK) {
        fprintf(stderr, "Cert error: %ld\n", result);
        return -1;
    }
    return 0;
}
```

## Common Scenarios

### Scenario 1: SSL handshake fails due to expired certificate

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: SSL context not properly configured for TLS version

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: OpenSSL memory leak from not freeing SSL_CTX

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always initialize OpenSSL before use
- **Tip 2:** Check SSL_get_error after every SSL operation
- **Tip 3:** Free SSL_CTX, SSL, and BIO objects when done
