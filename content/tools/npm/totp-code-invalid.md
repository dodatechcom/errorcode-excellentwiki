---
title: "[Solution] npm publish TOTP Code Invalid"
description: "Handle TOTP code invalid errors in npm publish by resyncing authenticator, checking time drift, and generating fresh OTP codes."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish TOTP Code Invalid

This guide helps you diagnose and resolve npm publish TOTP Code Invalid errors encountered when running npm commands.

## Common Causes

- Authenticator app time is out of sync with npm servers
- OTP code was entered after it expired (30-second window)
- Multiple publish attempts used the same OTP code

## How to Fix

### Resync Authenticator Time

```bash
# In Google Authenticator: Settings > Time correction > Sync
```

### Generate Fresh OTP Code

```bash
# Wait for new code generation (every 30 seconds)
```

### Use npm OTP Flag Correctly

```bash
npm publish --otp=<new-code>
```

## Examples

```bash
# Expired OTP code
npm publish --otp=123456
# Fix: Wait for new code
npm publish --otp=<new-6-digit-code>

# Authenticator time drift
npm publish --otp=123456
# Fix: Resync authenticator time
# Then generate fresh code and retry

```

## Related Errors

- [Two-Factor Required]({{< relref "/tools/npm/two-factor-required" >}}) -- 2FA requirement
- [E401 Unauthorized Publish]({{< relref "/tools/npm/publish-e401-unauthorized" >}}) -- auth error
