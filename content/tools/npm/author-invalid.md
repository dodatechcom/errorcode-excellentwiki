---
title: "[Solution] npm init Author Invalid"
description: "Resolve npm init author validation errors by using the correct format, including email properly, and configuring global npm author settings."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm init Author Invalid

This guide helps you diagnose and resolve npm init Author Invalid errors encountered when running npm commands.

## Common Causes

- Author string does not follow the expected name <email> (url) format
- Email address is missing angle brackets
- Author field contains invalid characters or encoding

## How to Fix

### Use Correct Author Format

```bash
Name <email> (url)
```

### Set Global Author Config

```bash
npm config set init-author-name 'Your Name'
npm config set init-author-email 'you@example.com'
```

### Set Author During Init

```bash
npm init --author='Your Name <you@example.com>'
```

## Examples

```bash
# Wrong author format
npm init
# Enter: John Doe <john@example.com>
# Not: John Doe john@example.com

# Set global to avoid manual entry
npm init
# Configure global defaults
npm config set init-author-name 'Your Name'
npm config set init-author-email 'you@email.com'

```

## Related Errors

- [License Invalid]({{< relref "/tools/npm/license-invalid" >}}) -- license error
- [Name Validation Failed]({{< relref "/tools/npm/init-name-validation-failed" >}}) -- name error
