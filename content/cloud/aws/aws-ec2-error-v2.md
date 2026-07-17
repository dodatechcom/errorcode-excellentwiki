---
title: "[Solution] AWS EC2 — InstanceLimitExceeded"
description: "Fix AWS EC2 InstanceLimitExceeded. Resolve instance launch quota exceeded errors."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An EC2 InstanceLimitExceeded error means you have reached the maximum number of instances allowed for a given instance type in the requested region. AWS account-level limits prevent launching additional instances.

## What This Error Means

AWS imposes default limits on EC2 instances per account, per region, and per instance family. When you request `RunInstances` and your existing running + pending instances meet or exceed the limit, AWS returns `InstanceLimitExceeded`. This is an account-level constraint, not a technical failure — the infrastructure is available but your quota is exhausted.

## Common Causes

- Too many instances of the same type already running in the region
- Default vCPU or instance limits reached for the instance family
- Failed instance launches consuming quota without releasing it
- Launching in an Availability Zone with insufficient capacity
- Reserved instance quota applied separately from on-demand
- Stopped instances still counting against the limit

## How to Fix

### Check Current Limits

```bash
aws service-quotas get-service-quota \
  --service-code ec2 \
  --quota-code L-1216C47A \
  --region us-east-1
```

### Check Running Instances

```bash
aws ec2 describe-instances \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name]' \
  --output table
```

### Request Quota Increase

```bash
aws service-quotas request-service-quota-increase \
  --service-code ec2 \
  --quota-code L-1216C47A \
  --desired-value 200 \
  --region us-east-1
```

### Terminate Unused Instances

```bash
# Find stopped instances
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=stopped" \
  --query 'Reservations[*].Instances[*].InstanceId' \
  --output text

# Terminate old instances
aws ec2 terminate-instances --instance-ids i-xxx i-yyy
```

### Use Different Instance Type

```bash
# Launch a different instance family
aws ec2 run-instances \
  --instance-type t3.medium \
  --image-id ami-xxx
```

### Check Quota per Region

```bash
aws service-quotas list-service-quotas \
  --service-code ec2 \
  --region us-east-1 \
  --query 'Quotas[?contains(QuotaName,`On-Demand`)].[QuotaName,Value]'
```

## Related Errors

- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error-v2" >}}) — Lambda runtime error
- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error-v2" >}}) — ECS container error
- [AWS EKS Error]({{< relref "/cloud/aws/aws-eks-error-v2" >}}) — EKS health check failed
