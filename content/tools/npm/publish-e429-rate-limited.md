---
title: "[Solution] npm publish E429 Rate Limited"
description: "Fix E429 rate limited errors in npm publish by waiting for rate limit reset, reducing publish frequency, and using token-based authentication."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish E429 Rate Limited

This guide helps you diagnose and resolve npm publish E429 Rate Limited errors encountered when running npm commands.

## Common Causes

- Too many publish requests sent within the rate limit window
- Automated CI/CD pipeline publishing too frequently
- Multiple accounts sharing the same IP hitting rate limits

## How to Fix

### Wait for Rate Limit Reset

```bash
sleep 300 && npm publish
```

### Check Rate Limit Headers

```bash
curl -I https://registry.npmjs.org/<package>
```

### Reduce Publish Frequency

```bash
# Add delays between publishes in CI/CD pipeline
```

## Examples

```bash
# CI/CD hitting rate limit
npm publish
# Fix: Add delay in pipeline
sleep 300 && npm publish

# Too many rapid publishes
npm publish
# Fix: Batch publishes with delays
for pkg in packages/*; do
cd $pkg && npm publish && cd ..
sleep 60
done

```

## Related Errors

- [E500 Internal Server Error]({{< relref "/tools/npm/e500-internal-error" >}}) -- server error
- [Two-Factor Required]({{< relref "/tools/npm/two-factor-required" >}}) -- 2FA requirement
