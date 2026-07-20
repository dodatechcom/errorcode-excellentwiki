---
title: "[Solution] AWS PrivateLink/VPC Endpoint Error — connectivity failures"
description: "Fix AWS PrivateLink errors. Resolve VPC endpoint connectivity, DNS, and service issues."
error-types: ["api-error"]
severities: ["error"]
weight: 109
---

An AWS PrivateLink error occurs when VPC endpoints fail to connect, DNS resolution breaks, or private connectivity to services malfunctions. This can be due to route table, subnet, or security group misconfiguration.

## Common Causes

- VPC endpoint subnet route table missing required routes
- Security group blocks traffic on endpoint port
- DNS resolution not enabled for VPC endpoint
- Endpoint service availability zone mismatch
- Private DNS name not resolving correctly

## How to Fix

### Check VPC Endpoint Status

```bash
aws ec2 describe-vpc-endpoints \
  --filters "Name=vpc-id,Values=vpc-xxx" \
  --query 'VpcEndpoints[*].{ID:VpcEndpointId,State:State,Service:ServiceName}'
```

### Verify Route Table

```bash
aws ec2 describe-route-tables \
  --filters "Name=vpc-id,Values=vpc-xxx" \
  --query 'RouteTables[*].Routes'
```

### Check Endpoint DNS

```bash
aws ec2 describe-vpc-endpoints \
  --vpc-endpoint-ids vpce-xxx \
  --query 'VpcEndpoints[*].DnsEntries'
```

### Create VPC Endpoint

```bash
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-xxx \
  --service-name com.amazonaws.us-east-1.s3 \
  --route-table-ids rtb-xxx
```

### Modify Endpoint Security Group

```bash
aws ec2 modify-vpc-endpoint \
  --vpc-endpoint-id vpce-xxx \
  --add-security-group-ids sg-xxx
```

## Examples

```bash
# Example 1: DNS resolution failure
# DNSNameNotFound: Could not resolve endpoint DNS name
# Fix: enable private DNS or add endpoint to route table

# Example 2: Connection refused
# Connection refused to endpoint vpce-xxx
# Fix: check security group allows traffic on required port
```

## Related Errors

- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
- [AWS Route53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) — Route53 DNS errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
