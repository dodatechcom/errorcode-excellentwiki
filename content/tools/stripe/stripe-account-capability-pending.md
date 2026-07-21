---
title: "[Solution] Stripe Account Capability Pending"
description: "Fix Stripe capability pending errors. Wait for capability verification and onboarding completion."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

## Error Description

The `stripe` command encountered a **capability_pending** issue. This error stops normal operation and must be resolved before continuing with your workflow.

## Common Causes

- Misconfigured settings or missing configuration
- Incompatible version of stripe or one of its dependencies
- File or directory permissions issue
- Network or connectivity problem during operation
- Platform-specific incompatibility
- Incorrect command syntax or API usage

## Typical Error Output

```
Error: capability_pending
```

## How to Fix

### 1. Verify Installation

```bash
stripe --version
```

### 2. Check Configuration

```bash
cat stripe.yaml 2>/dev/null || cat ~/.config/stripe/config 2>/dev/null
```

### 3. Clear Cache and Retry

```bash
stripe clean 2>/dev/null || true
```

### 4. Test in Isolation

```bash
stripe --help
```

## Common Scenarios

**After upgrading stripe.**
A recent upgrade may have changed defaults or removed deprecated options. Check the
release notes for breaking changes.

## Prevention

1. Pin stripe versions in CI configuration
2. Run `stripe doctor` or equivalent health check before making changes
3. Keep a backup of your configuration before modifying it
4. Test changes in a staging environment before applying to production
