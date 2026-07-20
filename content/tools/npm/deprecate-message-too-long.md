---
title: "[Solution] npm deprecate Message Too Long"
description: "Fix npm deprecate message too long errors by shortening the deprecation message, using concise language, and following npm character limits."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm deprecate Message Too Long

This guide helps you diagnose and resolve npm deprecate Message Too Long errors encountered when running npm commands.

## Common Causes

- Deprecation message exceeds npm character limit
- Message contains excessively long URLs or descriptions
- Multiple deprecation messages combined into one string

## How to Fix

### Shorten the Message

```bash
# Keep message under 100 characters when possible
```

### Use Concise Wording

```bash
npm deprecate <package>@<range> 'Use alt-pkg instead'
```

### Check Message Length

```bash
echo -n 'message' | wc -c
```

## Examples

```bash
# Message too long
npm deprecate old-pkg@'<2' 'This package is deprecated because...'
# Fix: Shorten message
npm deprecate old-pkg@'<2' 'Use new-pkg instead'

# Multiple lines in message
npm deprecate old-pkg@'<2' 'Line1\nLine2'
# Fix: Single concise line
npm deprecate old-pkg@'<2' 'Deprecated: use new-pkg'

```

## Related Errors

- [Package Not Found]({{< relref "/tools/npm/deprecate-package-not-found" >}}) -- package missing
- [E401 Unauthorized]({{< relref "/tools/npm/e401-unauthorized" >}}) -- auth error
