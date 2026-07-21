---
title: "[Solution] Vagrant Cloud Authentication Error"
description: "Fix Vagrant Cloud authentication errors when login to Vagrant Cloud fails."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Cloud Authentication Error

Vagrant Cloud login fails with authentication errors.

```
VagrantCloud authentication failed: Invalid credentials
```

## Common Causes

- Incorrect username or password
- Token expired
- Two-factor authentication required
- API token not generated
- Network connectivity issues

## How to Fix

### Login via CLI

```bash
# Login with credentials
vagrant cloud auth login

# Login with token
vagrant cloud auth login --token YOUR_TOKEN
```

### Generate API Token

```
1. Go to Vagrant Cloud > Settings > Security
2. Generate new API token
3. Copy token
```

### Store Token

```bash
# Store token for future use
vagrant cloud auth login --token YOUR_TOKEN --check

# Verify stored token
vagrant cloud auth whoami
```

### Logout and Re-login

```bash
vagrant cloud auth logout
vagrant cloud auth login
```

### Check Token Permissions

```bash
# Verify token works
curl -H "Authorization: Bearer YOUR_TOKEN" https://vagrantcloud.com/api/v2/auth
```

## Examples

```bash
# Automated login for CI/CD
export VAGRANT_CLOUD_TOKEN="your-token-here"
vagrant cloud auth login --token "$VAGRANT_CLOUD_TOKEN"
```
