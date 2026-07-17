---
title: "[Solution] AWS Secrets Manager Error"
description: "Fix AWS Secrets Manager errors. Resolve secret retrieval and management issues."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "secrets-manager", "secret", "credentials", "rotation"]
weight: 5
---

An AWS Secrets Manager error occurs when you cannot retrieve, create, or rotate secrets stored in Secrets Manager.

## Common Causes

- Secret does not exist or wrong region
- IAM permissions not granted for secretsmanager actions
- Secret version is disabled or pending deletion
- KMS key for secret encryption is not accessible
- Rotation function not configured or failing

## How to Fix

### Check Secret Exists

```bash
aws secretsmanager describe-secret --secret-id my-secret
```

### Get Secret Value

```bash
aws secretsmanager get-secret-value --secret-id my-secret
```

### Check Secret Versions

```bash
aws secretsmanager list-secret-version-ids --secret-id my-secret
```

### Rotate Secret

```bash
aws secretsmanager rotate-secret --secret-id my-secret
```

### Check Rotation Function

```bash
aws lambda get-function --function-name secret-rotation
```

## Examples

```bash
# Example 1: Secret not found
# ResourceNotFoundException: Secrets Manager can't find the specified secret
# Fix: verify secret name and region

# Example 2: Access denied
# AccessDeniedException
# Fix: add secretsmanager:GetSecretValue permission
```

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) — KMS key error
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission denied
