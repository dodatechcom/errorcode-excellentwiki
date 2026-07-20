---
title: "[Solution] Terraform Variable Environment Not Set"
description: "Fix Terraform variable environment not set errors when expected environment variables are missing."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Missing environment variable errors occur when Terraform expects env vars:

```
Error: Missing required variable

Variable "AWS_ACCESS_KEY_ID" is required but not set in environment.
```

## Common Causes

- Environment variables not exported.
- Shell session doesn't have the variables.

## How to Fix

**Set environment variables:**

```bash
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."
terraform plan
```

**Source before running:**

```bash
source .env && terraform plan
```

## Examples

```bash
# AWS credentials
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."

# GCP credentials
export GOOGLE_CREDENTIALS="$(cat service-account.json)"

# Azure
export ARM_CLIENT_ID="..."
export ARM_CLIENT_SECRET="..."
```
