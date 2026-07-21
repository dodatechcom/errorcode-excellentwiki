---
title: "[Solution] OpenSSL PRNG Not Seeded Error"
description: "Fix OpenSSL PRNG not seeded error. Resolve random number generator seeding issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL PRNG Not Seeded Error

The PRNG is not seeded. OpenSSL cannot generate random numbers.

## Common Causes

- Entropy source is not available
- /dev/urandom is not accessible
- RAND_seed was not called

## How to Fix

### Solution 1

```bash
openssl rand -hex 32
```

### Solution 2

```bash
ls -la /dev/urandom
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
