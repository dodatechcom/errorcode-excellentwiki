---
title: "AWS ThrottlingException / RequestLimitExceeded"
description: "ThrottlingException / RequestLimitExceeded — Fix AWS API rate limiting errors."
error-types: ["quota-error"]
severities: ["error"]
weight: 5
---

The `ThrottlingException` or `RequestLimitExceeded` error occurs when you exceed the AWS API request rate limit for a service. AWS enforces per-account and per-API throttling to ensure fair usage.

## Common Causes

- Application sends too many concurrent API requests
- Missing or insufficient retry logic with backoff
- Batch operations not using efficient APIs (e.g., individual calls vs. batch calls)
- Lambda functions making repeated API calls without caching

## How to Fix

Implement exponential backoff with jitter:

```python
import time
import random

def call_with_backoff(func, max_retries=5):
    for attempt in range(max_retries):
        try:
            return func()
        except ClientError as e:
            if e.response['Error']['Code'] in ('ThrottlingException', 'RequestLimitExceeded'):
                wait = (2 ** attempt) + random.uniform(0, 1)
                print(f"Throttled, retrying in {wait:.1f}s...")
                time.sleep(wait)
            else:
                raise
    raise Exception("Max retries exceeded")
```

Use AWS SDK built-in retry configuration:

```bash
# Configure AWS CLI retry settings
aws configure set default.retry_mode adaptive
aws configure set default.max_attempts 10
```

Enable request level throttling in your application:

```bash
# Check current service quotas
aws service-quotas get-service-quota \
  --service-code iam \
  --quota-code L-FE177D64 \
  --region us-east-1
```

## Examples

- Lambda function making 1000+ `dynamodb:GetItem` calls per second
- EC2 instance polling `ec2:DescribeInstances` every 100ms
- CI/CD pipeline running parallel CloudFormation stack updates

## Related Errors

- [AWS Quota Exceeded]({{< relref "/cloud/aws/ec2-quota" >}}) — EC2 instance limits exceeded.
- [AWS AccessDenied]({{< relref "/cloud/aws/access-denied" >}}) — API authorization failures.
- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded2" >}}) — GCP equivalent.
