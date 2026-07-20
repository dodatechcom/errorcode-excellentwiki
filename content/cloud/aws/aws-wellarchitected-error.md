---
title: "[Solution] AWS Well-Architected Error — review/lens/milestone failures"
description: "Fix AWS Well-Architected errors. Resolve review, lens, and milestone issues."
error-types: ["api-error"]
severities: ["error"]
weight: 162
---

An AWS Well-Architected Tool error occurs when reviews cannot be created, lens configurations fail, or milestones encounter errors. The Well-Architected Tool helps evaluate workloads against AWS best practices.

## Common Causes

- Workload has not been created in Well-Architected Tool
- Custom lens does not follow JSON schema
- Milestone answers not saved before creating review
- Review period overlap with existing review
- IAM user lacks wellarchitected:* permissions

## How to Fix

### List Workloads

```bash
aws wellarchitected list-workloads \
  --query 'WorkloadSummaries[*].{ID:WorkloadId,Name:WorkloadName,Status:Status}'
```

### Get Workload

```bash
aws wellarchitected get-workload \
  --workload-id workload-xxx
```

### Create Milestone

```bash
aws wellarchitected create-milestone \
  --workload-id workload-xxx \
  --milestone-name "Pre-production"
```

### List Reviews

```bash
aws wellarchitected list-lens-reviews \
  --workload-id workload-xxx
```

### Get Lens Review

```bash
aws wellarchitected get-lens-review \
  --workload-id workload-xxx \
  --lens-arn arn:aws:wellarchitected::aws:lens:wellarchitected
```

## Examples

```bash
# Example 1: Workload not found
# ResourceNotFoundException: Workload not found
# Fix: verify workload ID is correct

# Example 2: Milestone limit exceeded
# ServiceQuotaExceededException: Maximum milestones reached
# Fix: delete older milestones or request increase
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS CloudFormation Error]({{< relref "/cloud/aws/aws-cloudformation-error" >}}) — CloudFormation errors
- [AWS Config Error]({{< relref "/cloud/aws/aws-config-error" >}}) — Config compliance errors
