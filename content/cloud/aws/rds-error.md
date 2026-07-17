---
title: "AWS RDS Error: DB Instance Not Found / Cannot Connect"
description: "RDS: DB instance not found / cannot connect — Fix AWS RDS connection and configuration errors."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The `DBInstanceNotFound` or connection failure errors occur when an RDS database instance is not in an available state, the endpoint is wrong, or network/security group rules block the connection.

## Common Causes

- The DB instance is in `stopped` state or was deleted
- The security group does not allow inbound traffic on the database port
- The instance is in a private subnet with no route to the client
- The master password was rotated and the application has stale credentials
- The DB instance is in a different VPC than the client

## How to Fix

Check the DB instance status:

```bash
aws rds describe-db-instances \
  --db-instance-identifier mydb-instance \
  --query 'DBInstances[0].{Status:DBInstanceStatus,Endpoint:Endpoint.Address,Port:Endpoint.Port}'
```

Verify security group allows inbound traffic:

```bash
# Get the security group attached to the DB
aws rds describe-db-instances \
  --db-instance-identifier mydb-instance \
  --query 'DBInstances[0].VpcSecurityGroups[].VpcSecurityGroupId'

# Check inbound rules
aws ec2 describe-security-groups \
  --group-ids sg-0123456789abcdef0 \
  --query 'SecurityGroups[0].IpPermissions'
```

Add an inbound rule for the database port:

```bash
aws ec2 authorize-security-group-ingress \
  --group-id sg-0123456789abcdef0 \
  --protocol tcp \
  --port 5432 \
  --cidr 10.0.1.0/24
```

Test connectivity:

```bash
# From an EC2 instance in the same VPC
nc -zv mydb-instance.abc123.us-east-1.rds.amazonaws.com 5432
```

## Examples

- Application cannot connect to RDS after VPC peering is removed
- `Connection refused` because the security group only allows port 3306 but the DB is PostgreSQL on 5432
- RDS instance in a stopped state after manual stop — start it with `aws rds start-db-instance`

## Related Errors

- [AWS AccessDenied]({{< relref "/cloud/aws/access-denied" >}}) — IAM lacks RDS permissions.
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC configuration issues.
- [Azure RDS Error]({{< relref "/cloud/aws/rds-error" >}}) — Azure equivalent.
