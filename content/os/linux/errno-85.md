---
title: "[Solution] Linux KEYREVOKED (errno 85) — Key Has Been Revoked Fix"
description: "Fix Linux KEYREVOKED (errno 85) Key has been revoked error. Solutions for revoked key and credential management issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["keyrevoked", "key", "errno-85", "revoked", "security"]
weight: 5
---

# Linux KEYREVOKED (errno 85) — Key Has Been Revoked

KEYREVOKED (errno 85) means the cryptographic key has been explicitly revoked. This error occurs when a program tries to use a key that has been invalidated by an administrator or security policy. It is distinct from KEYEXPIRED (errno 84) because KEYREVOKED indicates intentional revocation, not natural expiration.

## Common Causes

- Key was revoked by an administrator
- Security policy invalidated the key
- Kerberos principal was disabled or revoked
- Key was compromised and invalidated

## How to Fix KEYREVOKED

### 1. Check Key Revocation Status

Verify if keys have been revoked:

```bash
keyctl show -a
keyctl describe <key_id>
```

### 2. Obtain a New Key

Request a fresh key from the key authority:

```bash
# For Kerberos
kinit user@REALM.COM

# For custom keys
keyctl new_session
```

### 3. Contact Security Administrator

If the key was revoked for security reasons, contact the administrator to get a new authorized key.

### 4. Clear Revoked Keys

Remove revoked keys from the keyring:

```bash
keyctl clear @u
```

### 5. Re-authenticate

Start a new authentication session:

```bash
kdestroy
kinit user@REALM.COM
```

## Verification

After obtaining a new key, confirm it is valid:

```bash
keyctl show -a
klist
```

## Related Error Codes

- [ENOKEY (errno 83)](/os/linux/errno-83/) — Required key not available
- [KEYEXPIRED (errno 84)](/os/linux/errno-84/) — Key has expired
- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
