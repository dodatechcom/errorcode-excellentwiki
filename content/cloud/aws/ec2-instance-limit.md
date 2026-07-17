---
title: "EC2 Instance Limit Exceeded"
description: "InstanceLimitExceeded - You have requested more instances than your current instance limit"
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `InstanceLimitExceeded` error occurs when you attempt to launch more EC2 instances of a specific type than your AWS account allows. AWS enforces per-region, per-instance-type limits on running instances.

## Common Causes

- Launching instances exceeds the default account quota for a given instance type
- Previously terminated instances still count toward the limit in some scenarios
- The limit was recently lowered by AWS Support
- Requesting a burst of instances simultaneously

## How to Check Current Limits

```bash
aws ec2 describe-instance-type-offerings \
  --location-type availability-zone \
  --filters Name=instance-type,Values=m5.large
```

Request a limit increase:

```bash
aws service-quotas request-service-quota-increase \
  --service-code ec2 \
  --quota-code L-1216C47A \
  --desired-value 100 \
  --region us-east-1
```

## Examples

- Trying to launch 50 `m5.large` instances in `us-east-1` when the account limit is 30
- Auto Scaling group attempts to scale beyond the instance type quota

## Related Errors

- [S3 Access Denied]({{< relref "/cloud/aws/s3-access-denied" >}})
- [Azure Resource Not Found]({{< relref "/cloud/azure/resource-not-found" >}})
- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded" >}})
