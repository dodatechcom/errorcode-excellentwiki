---
title: "[Solution] Helm OCI Registry Authentication Failed Error Fix"
description: "Fix 'OCI registry authentication failed' errors in Helm. Resolve registry login and credential issues for chart storage."
tools: ["helm"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Helm OCI Registry Authentication Failed Error Fix

The OCI registry authentication failed error occurs when Helm cannot authenticate with an OCI-compatible registry for pulling or pushing charts.

## What This Error Means

OCI registries require authentication for chart operations. When credentials are wrong, expired, or not provided, Helm cannot access the registry.

A typical error:

```
Error: MANIFEST_UNKNOWN: manifest unknown
```

Or:

```
Error: UNAUTHORIZED: authentication required
```

## Why It Happens

Common causes include:

- **Wrong credentials** — Username or password incorrect.
- **Token expired** — Authentication token needs refresh.
- **Registry does not support OCI** — Registry is not OCI-compatible.
- **Network restrictions** — Firewall blocking registry access.
- **Docker config issues** — Using docker credential store incorrectly.
- **Multi-factor auth** — MFA tokens not supported.

## How to Fix It

### Fix 1: Login to registry

```bash
# RIGHT: Login with credentials
helm registry login ghcr.io -u $GITHUB_USER -p $GITHUB_TOKEN

# Interactive login
helm registry login ghcr.io
```

### Fix 2: Use credential helpers

```bash
# RIGHT: Use Docker credential helper
helm registry login ghcr.io --username $USER --password $PASS

# Or use keychain on macOS
helm registry login ghcr.io
```

### Fix 3: Check registry compatibility

```bash
# RIGHT: Verify OCI support
# Test with OCI endpoint
helm registry login registry.example.com

# Check if registry supports OCI
curl -s https://registry.example.com/v2/ | head -5
```

### Fix 4: Handle token refresh

```bash
# RIGHT: Re-login when token expires
helm registry logout ghcr.io
helm registry login ghcr.io -u $USER -p $NEW_TOKEN
```

### Fix 5: Configure insecure registries

```bash
# RIGHT: For self-hosted registries
helm registry login localhost:5000 --insecure
```

## Common Mistakes

- **Using personal access token instead of password** — Many registries need tokens.
- **Not refreshing expired tokens** — Tokens expire; re-login regularly.
- **Assuming all registries support OCI** — Not all registries are OCI-compatible.

## Related Pages

- [Helm Push Error](helm-push-error) — Chart push issues
- [Helm Render Error](helm-render-error) — Template rendering issues
- [Helm Notation Error](helm-notation-error) — Secrets decryption issues
