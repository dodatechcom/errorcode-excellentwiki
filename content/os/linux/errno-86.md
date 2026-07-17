---
title: "[Solution] Linux KEYREJECTED (errno 86) — Key Was Rejected by Service Fix"
description: "Fix Linux KEYREJECTED (errno 86) Key was rejected by service error. Solutions for rejected authentication key issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux KEYREJECTED (errno 86) — Key Was Rejected by Service

KEYREJECTED (errno 86) means the key was rejected by the service or authority. This error occurs when a program presents a key to a service but the service refuses to accept it. It is distinct from EACCES (errno 13) because KEYREJECTED indicates the service specifically rejected the key, not a general permission problem.

## Common Causes

- Key was presented to wrong service or server
- Key type is not supported by the service
- Service configuration changed and no longer accepts the key
- Key was tampered with or corrupted

## How to Fix KEYREJECTED

### 1. Check Key Details

Verify the key properties:

```bash
keyctl describe <key_id>
keyctl show -a
```

### 2. Verify Key Type and Format

Ensure the key matches what the service expects:

```bash
keyctl pipe <key_id> | xxd | head -5
```

### 3. Generate a New Key

Create a key that meets the service requirements:

```bash
keyctl new_session
keyctl add user mykey "correct_secret" @u
```

### 4. Check Service Configuration

Verify the service is configured to accept your key type:

```bash
# For Kerberos, check krb5.conf
cat /etc/krb5.conf
```

### 5. Re-authenticate

Start fresh with new credentials:

```bash
kdestroy
kinit user@REALM.COM
```

## Verification

After fixing the key, confirm the service accepts it:

```bash
klist
keyctl show -a
```

## Related Error Codes

- [ENOKEY (errno 83)](/os/linux/errno-83/) — Required key not available
- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
- [EPERM (errno 1)](/os/linux/errno-1/) — Operation not permitted
