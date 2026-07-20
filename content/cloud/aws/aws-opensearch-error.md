---
title: "[Solution] AWS OpenSearch Error — domain/index/cluster health failures"
description: "Fix AWS OpenSearch errors. Resolve domain, index, and cluster health issues."
error-types: ["api-error"]
severities: ["error"]
weight: 135
---

An AWS OpenSearch error occurs when domains fail to create, indexes become red, or cluster health degrades. OpenSearch (formerly Elasticsearch) provides search and analytics but requires careful cluster management.

## Common Causes

- Domain instance type has insufficient storage or memory
- Index shards exceed cluster capacity
- VPC configuration blocks OpenSearch API access
- Fine-grained access control policy misconfigured
- Domain endpoint DNS not resolving

## How to Fix

### Check Domain Status

```bash
aws opensearch describe-domains \
  --domain-names my-domain \
  --query 'DomainStatusList[*].{Domain:DomainName,Status:Processing,Endpoint:Endpoint}'
```

### Get Cluster Health

```bash
aws opensearch get-compatible-versions \
  --domain-name my-domain
```

### List Indices

```bash
aws opensearch list-versions \
  --max-items 5
```

### Create Domain

```bash
aws opensearch create-domain \
  --domain-name my-domain \
  --instance-type t3.small.search \
  --instance-count 2 \
  --ebs-options EBSEnabled=true,VolumeType=gp3,VolumeSize=100
```

### Update Access Policy

```bash
aws opensearch update-domain-config \
  --domain-name my-domain \
  --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789012:root"},"Action":"es:*","Resource":"arn:aws:es:us-east-1:123456789012:domain/my-domain/*"}]}'
```

## Examples

```bash
# Example 1: Cluster red health
# ClusterHealth: red
# Fix: check for unassigned shards and increase instance type

# Example 2: Access denied
# AccessDeniedException: Fine-grained access control denied
# Fix: update access policy to include your IP or IAM role
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
