---
title: "[Solution] GCP Cloud SQL Connection Error"
description: "Fix GCP Cloud SQL connection errors. Resolve Cloud SQL connectivity issues."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
tags: ["gcp", "cloud-sql", "database", "connection", "postgres"]
weight: 5
---

A Cloud SQL connection error occurs when you cannot connect to a Cloud SQL instance. This can be caused by network, permission, or configuration issues.

## Common Causes

- Cloud SQL instance is not running
- Public IP not authorized for the client
- Private IP VPC peering not configured
- IAM permissions missing for Cloud SQL
- Connection string or credentials incorrect

## How to Fix

### Check Instance Status

```bash
gcloud sql instances describe my-instance
```

### Authorize IP

```bash
gcloud sql instances patch my-instance --authorize-networks=1.2.3.4
```

### Connect to Instance

```bash
gcloud sql connect my-instance --user=myuser --database=mydb
```

### Check Connection Name

```bash
gcloud sql instances describe my-instance --format="value(connectionName)"
```

### Set IAM Authentication

```bash
gcloud sql instances patch my-instance --enable-iam-auth
```

## Examples

```bash
# Example 1: Connection refused
# Connection refused: could not connect to server
# Fix: authorize client IP in Cloud SQL

# Example 2: IAM authentication failed
# IAM authentication failed for user
# Fix: enable IAM authentication and grant Cloud SQL Client role
```

## Related Errors

- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error" >}}) — Azure SQL error
- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) — RDS connection error
