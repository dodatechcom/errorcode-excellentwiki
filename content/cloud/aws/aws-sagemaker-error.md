---
title: "[Solution] AWS SageMaker Error — notebook/training/endpoint failures"
description: "Fix AWS SageMaker errors. Resolve notebook, training job, and endpoint issues."
error-types: ["api-error"]
severities: ["error"]
weight: 163
---

An AWS SageMaker error occurs when notebook instances fail to start, training jobs abort, or endpoints cannot serve predictions. SageMaker provides managed ML but requires correct instance and IAM configuration.

## Common Causes

- Notebook instance type not available in region
- Training job fails with script errors
- Endpoint instance type insufficient for model
- S3 training data path inaccessible
- IAM role lacks S3 or SageMaker permissions

## How to Fix

### List Notebook Instances

```bash
aws sagemaker list-notebook-instances \
  --query 'NotebookInstances[*].{Name:NotebookInstanceName,Status:NotebookInstanceStatus}'
```

### Start Notebook Instance

```bash
aws sagemaker start-notebook-instance \
  --notebook-instance-name my-notebook
```

### Describe Training Job

```bash
aws sagemaker describe-training-job \
  --training-job-name my-training-job
```

### Create Endpoint

```bash
aws sagemaker create-endpoint-config \
  --endpoint-config-name my-endpoint-config \
  --production-variants VariantName=AllTraffic,ModelName=my-model,InstanceType=ml.t2.medium,InitialInstanceCount=1
```

### Invoke Endpoint

```bash
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name my-endpoint \
  --content-type application/json \
  --body '{"features": [1, 2, 3]}' \
  response.json
```

## Examples

```bash
# Example 1: Notebook instance failed
# ResourceLimitExceeded: Instance type not available
# Fix: try different instance type or region

# Example 2: Training job failed
# ValidationException: S3 path does not exist
# Fix: verify training data S3 path and IAM access
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 data errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
