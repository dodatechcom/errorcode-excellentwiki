---
title: "[Solution] Linux KEYEXPIRED (errno 84) — Key Has Expired Fix"
description: "Fix Linux KEYEXPIRED (errno 84) Key has expired error. Solutions for expired key and credential management issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux KEYEXPIRED (errno 84) — Key Has Expired

KEYEXPIRED (errno 84) means the cryptographic key or credential has expired. This error occurs when a program attempts to use a key that has passed its expiration date, such as an expired Kerberos ticket or an expired key in the kernel keyring. It is distinct from ENOKEY (errno 83) because KEYEXPIRED indicates the key exists but is no longer valid.

## Common Causes

- Kerberos ticket expired
- Key in kernel keyring has passed its timeout
- TLS certificate or key has expired
- Token or credential expired in authentication system

## How to Fix KEYEXPIRED

### 1. Check Key Expiration Status

Verify key validity:

```bash
keyctl show -a
klist -e
```

### 2. Renew Kerberos Tickets

Renew expired credentials:

```bash
kinit -R
kinit --renew
```

### 3. Obtain Fresh Credentials

Get new tickets if renewal is not possible:

```bash
kinit user@REALM.COM
```

### 4. Update Expired Keys

Replace expired keys in the kernel keyring:

```bash
# Remove expired key
keyctl unlink <key_id>

# Add new key
keyctl add user mykey "new_secret" @u
```

### 5. Check TLS Certificate Expiration

Verify certificate validity:

```bash
openssl x509 -in cert.pem -noout -dates
```

## Verification

After renewing or replacing the key, confirm validity:

```bash
klist -e
keyctl show -a
```

## Related Error Codes

- [ENOKEY (errno 83)](/os/linux/errno-83/) — Required key not available
- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
- [EPERM (errno 1)](/os/linux/errno-1/) — Operation not permitted
