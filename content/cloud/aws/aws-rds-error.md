---
title: "[Solution] AWS RDS Error — connection or instance error"
description: "Fix AWS RDS errors. Resolve RDS connection and instance issues."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "rds", "database", "connection", "instance"]
weight: 5
---

An AWS RDS error occurs when you cannot connect to or manage an RDS database instance. This can be caused by network, permission, or configuration issues.

## Common Causes

- Security group does not allow inbound traffic on the DB port
- Database instance is in a stopped state
- IAM authentication not configured correctly
- Database endpoint or port is incorrect
- VPC/subnet configuration blocks connectivity

## How to Fix

### Check Instance Status

```bash
aws rds describe-db-instances \
  --db-instance-identifier my-db \
  --query 'DBInstances[*].DBInstanceStatus'
```

### Verify Security Group

```bash
aws ec2 describe-security-groups \
  --group-ids sg-xxx \
  --query 'SecurityGroups[*].IpPermissions'
```

### Test Connection

```bash
psql -h my-db.abc123.us-east-1.rds.amazonaws.com -U myuser -d mydb
```

### Check Endpoint

```bash
aws rds describe-db-instances \
  --db-instance-identifier my-db \
  --query 'DBInstances[*].Endpoint.Address'
```

## Examples

```bash
# Example 1: Connection refused
# Fix: add inbound rule to security group for port 5432

# Example 2: Instance stopped
# Fix: aws rds start-db-instance --db-instance-identifier my-db
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission denied
- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) — ECS task failed
