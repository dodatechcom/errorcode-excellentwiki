---
title: "[Solution] GitHub Actions Billing Not Set Up"
description: "Fix GitHub Actions billing not configured errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Billing not set up errors occur when the organization does not have billing configured:

```
Error: GitHub Actions requires a billing account
```

## Common Causes

- Free tier limits reached.
- Organization does not have a payment method.

## How to Fix

**Set up billing:**

Go to Settings > Billing > Add payment method

## Examples

```yaml
# Free tier: 2000 minutes/month for private repos
# Pro: 3000 minutes/month
# Team: 3000 minutes/month per member
```
