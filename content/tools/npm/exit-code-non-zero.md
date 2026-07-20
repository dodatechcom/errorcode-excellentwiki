---
title: "[Solution] npm run-script Exit Code Non-Zero"
description: "Handle npm run-script exit code non-zero errors by checking the script output, fixing failing commands, and using --if-present flag."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm run-script Exit Code Non-Zero

This guide helps you diagnose and resolve npm run-script Exit Code Non-Zero errors encountered when running npm commands.

## Common Causes

- Script contains a failing command with non-zero exit code
- Test suite has failing tests causing exit code 1
- Build command failed due to missing dependencies or configuration

## How to Fix

### Check Script Output for Errors

```bash
npm run <script> --verbose
```

### Run Script and Capture Output

```bash
npm run <script> 2>&1 | tee output.log
```

### Use --if-present to Skip Missing Scripts

```bash
npm run <script> --if-present
```

## Examples

```bash
# Test suite failing
npm test
# Fix: Check which tests fail
npm test -- --reporter spec

# Build script failing
npm run build
# Fix: Check build errors
npm run build --verbose

```

## Related Errors

- [Script Not Found]({{< relref "/tools/npm/script-not-found" >}}) -- script missing
- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
