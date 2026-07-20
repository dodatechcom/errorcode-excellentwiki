---
title: "[Solution] AWS DMS Error — migration/task/endpoint/replication failures"
description: "Fix AWS DMS errors. Resolve Database Migration Service task, endpoint, and replication issues."
error-types: ["api-error"]
severities: ["error"]
weight: 141
---

An AWS DMS error occurs when migration tasks fail, endpoints cannot connect, or replication instances encounter errors. DMS provides database migration but requires correct endpoint and task configuration.

## Common Causes

- Replication instance storage exhausted
- Source or target endpoint connection timeout
- IAM role lacks access to migration resources
- Table mapping rules contain invalid syntax
- LOB (Large Object) data exceeds max LOB size

## How to Fix

### Check Replication Instance

```bash
aws dms describe-replication-instances \
  --query 'ReplicationInstances[*].{ID:ReplicationInstanceId,Status:ReplicationInstanceStatus,Storage:AllocatedStorage}'
```

### List Tasks

```bash
aws dms describe-replication-tasks \
  --query 'ReplicationTasks[*].{ID:ReplicationTaskArn,Status:Status}'
```

### Check Endpoint Status

```bash
aws dms describe-endpoints \
  --query 'Endpoints[*].{ID:EndpointId,Type:EndpointType,Status:Status}'
```

### Test Connection

```bash
aws dms test-connection \
  --endpoint-arn arn:aws:dms:us-east-1:123456789012:endpoint:xxx \
  --replication-instance-arn arn:aws:dms:us-east-1:123456789012:rep:xxx
```

### Start Task

```bash
aws dms start-replication-task \
  --replication-task-arn arn:aws:dms:us-east-1:123456789012:task:xxx \
  --start-replication-task-type start-replication
```

## Examples

```bash
# Example 1: Connection failed
# Test connection failed: Communications link failure
# Fix: verify endpoint credentials and network connectivity

# Example 2: Task failed
# ReplicationTask error: Table not found in source
# Fix: update table mapping rules to match source schema
```

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) — RDS database errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
