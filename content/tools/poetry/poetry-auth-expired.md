---
title: "[Solution] Poetry Auth Expired -- Fix Expired Repository Credentials"
description: "Fix Poetry auth expired errors when repository authentication credentials have expired. Refresh tokens and update configuration."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the credentials Poetry is using for a private repository have expired. The server rejected the authentication.

## Common Causes

- API token has an expiration date
- Password was changed on the remote server
- OAuth token needs refreshing
- Credentials were rotated

## How to Fix

### 1. Update Credentials

```bash
poetry config pypi-token.private pypi-AgEI...newtoken...
```

### 2. Use Keyring for Auto-Renewal

```bash
poetry config keyring-backend python.keyring.backends.SecretService.Keyring
```

### 3. Set Up .netrc

```bash
cat >> ~/.netrc << EOF
machine pypi.internal.com
login user
password new-token
EOF
```

### 4. Re-authenticate Interactively

```bash
poetry publish --repository private --username user
# Enter password when prompted
```

## Examples

```bash
$ poetry install
HTTPError: 401 Unauthorized from https://pypi.internal.com/simple/

$ poetry config pypi-token.private pypi-AgEI...newtoken...
$ poetry install
Installing dependencies from lock file...
```
