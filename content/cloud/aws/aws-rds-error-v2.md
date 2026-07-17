---
title: "[Solution] AWS RDS — Can't connect to MySQL server"
description: "Fix AWS RDS MySQL connection error. Resolve RDS connectivity and access issues."
cloud: ["aws"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["aws", "rds", "mysql", "connection", "database", "connect"]
weight: 5
---

A "Can't connect to MySQL server" error means the application cannot establish a TCP connection to the RDS database instance. The database may be unavailable, the security group may be blocking traffic, or the endpoint may be incorrect.

## What This Error Means

RDS MySQL uses port 3306 by default. When an application attempts to connect, the connection passes through several layers: the client's VPC/subnet, security groups, the RDS instance's security group, and the database's authentication. A failure at any layer produces a connection error. The error `Can't connect to MySQL server on 'xxx.rds.amazonaws.com' (110)` indicates a network-level timeout, while `(111)` indicates an explicit refusal.

## Common Causes

- RDS instance is in a stopped state
- Security group does not allow inbound traffic on port 3306
- Application is in a different VPC without VPC peering
- RDS endpoint hostname is incorrect or stale
- Database is overloaded and cannot accept new connections
- Max connections limit reached on the RDS instance
- RDS instance is in a different subnet group with no route

## How to Fix

### Check RDS Instance Status

```bash
aws rds describe-db-instances \
  --db-instance-identifier my-db \
  --query 'DBInstances[*].[DBInstanceStatus,Endpoint.Address,Endpoint.Port]'
```

### Verify Security Group Rules

```bash
aws ec2 describe-security-groups \
  --group-ids sg-xxx \
  --query 'SecurityGroups[*].IpPermissions'
```

### Add Inbound Rule for MySQL

```bash
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxx \
  --protocol tcp \
  --port 3306 \
  --cidr 10.0.0.0/16
```

### Test Connection

```bash
mysql -h my-db.xxx.rds.amazonaws.com -P 3306 -u admin -p
nc -zv my-db.xxx.rds.amazonaws.com 3306
telnet my-db.xxx.rds.amazonaws.com 3306
```

### Check Max Connections

```sql
SHOW VARIABLES LIKE 'max_connections';
SHOW STATUS LIKE 'Threads_connected';
```

### Increase Max Connections

```bash
aws rds modify-db-instance \
  --db-instance-identifier my-db \
  --max-connections 200 \
  --apply-immediately
```

### Verify VPC Subnet Route

```bash
aws ec2 describe-route-tables \
  --filters "Name=vpc-id,Values=vpc-xxx" \
  --query 'RouteTables[*].Routes'
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error-v2" >}}) — IAM access denied
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error-v2" >}}) — S3 access denied
- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error-v2" >}}) — Azure SQL firewall
