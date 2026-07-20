---
title: "[Solution] npm install E401 Unauthorized"
description: "Fix E401 unauthorized errors in npm install by refreshing authentication tokens, configuring .npmrc, and checking registry credentials."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install E401 Unauthorized

This guide helps you diagnose and resolve npm install E401 Unauthorized errors encountered when running npm commands.

## Common Causes

- Authentication token has expired or been revoked
- .npmrc file contains invalid or outdated credentials
- Private registry requires fresh login authentication

## How to Fix

### Re-login to npm Registry

```bash
npm login
```

### Clear Stored Credentials

```bash
npm config delete //registry.npmjs.org/:_authToken
```

### Set New Auth Token

```bash
npm config set //registry.npmjs.org/:_authToken <new-token>
```

## Examples

```bash
# Expired token on private registry
npm install @myorg/package
# Fix: Re-authenticate
npm login
npm config set //registry.npmjs.org/:_authToken $(npm token create)

# Invalid .npmrc credentials
npm install private-pkg
# Fix: Remove old credentials and re-login
npm config delete //registry.npmjs.org/:_authToken
npm login

```

## Related Errors

- [E403 Forbidden]({{< relref "/tools/npm/e403-forbidden" >}}) -- access denied
- [E404 Not Found]({{< relref "/tools/npm/e404-not-found" >}}) -- package not found
