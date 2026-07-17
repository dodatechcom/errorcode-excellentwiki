---
title: "[Solution] Python ImportError: boto3 bedrock not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: boto3 bedrock not found. Install boto3 and configure AWS Bedrock access."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: boto3 bedrock not found — ModuleNotFoundError Fix

This error occurs when trying to use AWS Bedrock with boto3 but boto3 is not installed or Bedrock access is not configured.

## What This Error Means

AWS Bedrock is accessed through boto3. The error can mean boto3 is not installed or the Bedrock runtime module is not available.

## Common Causes

```python
# Cause 1: boto3 not installed
import boto3  # ModuleNotFoundError

# Cause 2: Bedrock access not configured
# AWS credentials not set up

# Cause 3: Region doesn't support Bedrock
```

## How to Fix

### Fix 1: Install boto3

```bash
pip install boto3
```

### Fix 2: Configure AWS credentials

```bash
aws configure
# Or set environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

### Fix 3: Use Bedrock Runtime

```python
import boto3

bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

response = bedrock_runtime.invoke_model(
    modelId='anthropic.claude-v2',
    body=b'{"prompt": "Hello"}'
)
```

## Related Errors

- {{< relref "importerror-boto3" >}} — ImportError: boto3
- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-anthropic" >}} — ImportError: anthropic
