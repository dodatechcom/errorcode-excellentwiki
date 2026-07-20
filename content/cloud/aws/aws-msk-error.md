---
title: "[Solution] AWS MSK Error — broker/topic/consumer failures"
description: "Fix AWS MSK errors. Resolve Managed Kafka broker, topic, and consumer group issues."
error-types: ["api-error"]
severities: ["error"]
weight: 136
---

An AWS MSK error occurs when brokers become unreachable, topics fail to replicate, or consumer groups stop processing. Amazon MSK provides managed Apache Kafka but requires careful broker and topic management.

## Common Causes

- Broker storage space exhausted
- Topic replication factor exceeds broker count
- Security group does not allow Kafka port (9092/9098)
- Client SSL/TLS configuration mismatch
- Consumer group rebalance stuck

## How to Fix

### Check Cluster Status

```bash
aws kafka describe-cluster \
  --cluster-arn arn:aws:kafka:us-east-1:123456789012:cluster/my-cluster/xxx
```

### List Brokers

```bash
aws kafka list-brokers \
  --cluster-arn arn:aws:kafka:us-east-1:123456789012:cluster/my-cluster/xxx \
  --query 'BrokerInfoList[*].{ID:BrokerId,Zone:BrokerAZ,Storage:CurrentBrokerStorageInfo}'
```

### Describe Configuration

```bash
aws kafka describe-configuration \
  --arn arn:aws:kafka:us-east-1:123456789012:configuration/my-config/xxx
```

### Update Broker Storage

```bash
aws kafka update-broker-storage \
  --cluster-arn arn:aws:kafka:us-east-1:123456789012:cluster/my-cluster/xxx \
  --target-broker-storage-info '{"volumeSize":500}'
```

### Get Bootstrap Brokers

```bash
aws kafka get-bootstrap-brokers \
  --cluster-arn arn:aws:kafka:us-east-1:123456789012:cluster/my-cluster/xxx
```

## Examples

```bash
# Example 1: Broker unreachable
# TimeoutException: Broker not available
# Fix: check security groups and broker status

# Example 2: Topic replication failed
# NotEnoughReplicasException: Not enough in-sync replicas
# Fix: add more brokers or reduce replication factor
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
