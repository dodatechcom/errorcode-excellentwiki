---
title: "[Solution] AWS QLDB Error — ledger/journal/query failures"
description: "Fix AWS QLDB errors. Resolve ledger, journal, and PartiQL query issues."
error-types: ["api-error"]
severities: ["error"]
weight: 145
---

An AWS QLDB error occurs when ledgers fail to create, journal streams break, or queries return errors. Amazon QLDB provides an immutable ledger database but requires proper journal and query management.

## Common Causes

- Ledger deletion protection enabled
- Journal export to S3 fails due to IAM permissions
- PartiQL query syntax errors
- Stream is in CREATING state and not ready
- KMS key does not exist or is disabled

## How to Fix

### List Ledgers

```bash
aws qldb list-ledgers \
  --query 'Ledgers[*].{Name:Name,State:State,DeletionProtection:DeletionProtection}'
```

### Create Ledger

```bash
aws qldb create-ledger \
  --name my-ledger \
  --permissions-mode STANDARD \
  --deletion-protection
```

### Describe Ledger

```bash
aws qldb describe-ledger --name my-ledger
```

### Export Journal to S3

```bash
aws qldb export-journal-to-s3 \
  --ledger-name my-ledger \
  --role-arn arn:aws:iam::123456789012:role/QLDBExportRole \
  --s3-export-configuration '{"Bucket":"my-qldb-bucket","Prefix":"exports/","EncryptionConfiguration":{"ObjectEncryptionType":"SSE_S3"}}' \
  --exclusive-start-time 2025-01-01T00:00:00Z \
  --inclusive-end-time 2025-01-31T23:59:59Z
```

### Delete Ledger

```bash
aws qldb delete-ledger --name my-ledger
```

## Examples

```bash
# Example 1: Deletion protection
# BadRequestException: Cannot delete ledger with deletion protection
# Fix: disable deletion protection first

# Example 2: Export failed
# InvalidParameterValueException: Invalid S3 bucket
# Fix: verify S3 bucket exists and IAM role has access
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 bucket errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) — KMS key errors
