---
title: "[Solution] AWS Glue Error — job/crawler/catalog/connection failures"
description: "Fix AWS Glue errors. Resolve Glue job, crawler, catalog, and connection issues."
error-types: ["api-error"]
severities: ["error"]
weight: 138
---

An AWS Glue error occurs when ETL jobs fail, crawlers cannot catalog data, or connections to data stores break. AWS Glue provides serverless ETL but requires proper IAM, networking, and schema configuration.

## Common Causes

- Glue job IAM role lacks S3 or JDBC access
- Crawler cannot connect to data store
- ETL script has Python/PySpark errors
- Connection VPC configuration blocks network access
- Data catalog table schema does not match source data

## How to Fix

### List Glue Jobs

```bash
aws glue list-jobs \
  --query 'Jobs[*].{Name:Name,Role:Role,MaxRetries:MaxRetries}'
```

### Get Job Run Status

```bash
aws glue get-job-run \
  --job-name my-etl-job \
  --run-id jr-xxx
```

### Start Crawler

```bash
aws glue start-crawler --name my-crawler
```

### Get Crawler Status

```bash
aws glue get-crawler \
  --name my-crawler \
  --query 'Crawler.State'
```

### Create Connection

```bash
aws glue create-connection \
  --connection-input '{
    "Name": "my-rds-connection",
    "ConnectionType": "JDBC",
    "PhysicalConnectionRequirements": {
      "SubnetId": "subnet-xxx",
      "SecurityGroupIdList": ["sg-xxx"],
      "AvailabilityZone": "us-east-1a"
    }
  }'
```

## Examples

```bash
# Example 1: Job failed
# GlueRuntimeException: S3 access denied
# Fix: add S3 permissions to Glue job IAM role

# Example 2: Crawler failed
# CrawlerFailedException: Cannot connect to data store
# Fix: verify connection VPC settings and security groups
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 data errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
