---
title: "[Solution] npm init License Invalid"
description: "Fix npm init invalid license errors by using SPDX license identifiers, selecting from standard licenses, and configuring default license settings."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm init License Invalid

This guide helps you diagnose and resolve npm init License Invalid errors encountered when running npm commands.

## Common Causes

- License string is not a valid SPDX license identifier
- Custom license text was entered instead of a standard identifier
- License identifier contains typos or incorrect format

## How to Fix

### Use Valid SPDX Identifier

```bash
MIT, Apache-2.0, GPL-3.0, ISC, BSD-3-Clause
```

### List All Valid SPDX Licenses

```bash
npm search license --long | head -20
```

### Set Default License Config

```bash
npm config set init-license 'MIT'
```

## Examples

```bash
# Invalid license text entered
npm init
# Enter: MIT
# Not: Open Source, Free, Custom

# Set default license globally
npm init
# Configure default
npm config set init-license 'MIT'

```

## Related Errors

- [Author Invalid]({{< relref "/tools/npm/author-invalid" >}}) -- author error
- [Name Validation Failed]({{< relref "/tools/npm/init-name-validation-failed" >}}) -- name error
