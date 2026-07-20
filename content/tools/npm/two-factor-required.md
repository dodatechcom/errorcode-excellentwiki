---
title: "[Solution] npm publish Two-Factor Required"
description: "Fix two-factor authentication required errors in npm publish by configuring 2FA, generating OTP codes, and setting up automation tokens."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish Two-Factor Required

This guide helps you diagnose and resolve npm publish Two-Factor Required errors encountered when running npm commands.

## Common Causes

- npm account has 2FA enabled but no OTP was provided
- CI/CD pipeline does not have an automation token configured
- OTP code expired before the publish request completed

## How to Fix

### Enable 2FA on npm Account

```bash
npm profile enable-2fa auth-and-writes
```

### Generate OTP Code

```bash
# Use authenticator app to generate 6-digit code
```

### Set Up Automation Token for CI/CD

```bash
npm token create --type=automation
```

## Examples

```bash
# Publish without OTP
npm publish
# Fix: Provide OTP code
npm publish --otp=<6-digit-code>

# CI/CD pipeline needs auth
npm publish
# Fix: Use automation token
npm token create --type=automation
# Set NPM_TOKEN env var in CI

```

## Related Errors

- [TOTP Code Invalid]({{< relref "/tools/npm/totp-code-invalid" >}}) -- invalid OTP
- [E401 Unauthorized Publish]({{< relref "/tools/npm/publish-e401-unauthorized" >}}) -- auth error
