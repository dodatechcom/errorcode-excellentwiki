---
title: "[Solution] boto3 NoCredentialsError Fix"
description: "Fix boto3 NoCredentialsError. Configure AWS credentials via environment variables, IAM roles, or AWS config files."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# boto3 NoCredentialsError Fix

A `botocore.exceptions.NoCredentialsError` is raised when boto3 cannot find AWS credentials to authenticate API requests.

## What This Error Means

Common messages:

- `botocore.exceptions.NoCredentialsError: Unable to locate credentials`
- `NoCredentialsError: The credential process returned an invalid JSON`
- `NoCredentialError: No credentials were configured`

AWS SDK attempted to find credentials in the standard credential chain but failed. This means neither environment variables, config files, nor IAM roles provided valid credentials.

## Common Causes

```python
import boto3

# Cause 1: No credentials configured at all
s3 = boto3.client("s3")
s3.list_buckets()  # NoCredentialsError

# Cause 2: Wrong environment variable names
import os
os.environ["AWS_ACCESS_KEY"] = "..."  # Wrong — should be AWS_ACCESS_KEY_ID

# Cause 3: Expired or revoked credentials
# Credentials set but expired

# Cause 4: Running outside EC2 without instance profile
# IAM role not attached to EC2 instance
```

## How to Fix

### Fix 1: Set environment variables

```bash
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
export AWS_DEFAULT_REGION="us-east-1"
```

### Fix 2: Use AWS CLI credentials

```bash
aws configure
# Enter Access Key ID, Secret Access Key, Region, Output format
```

### Fix 3: Use IAM roles (EC2/EKS/Lambda)

```python
import boto3

# boto3 automatically uses IAM role credentials
s3 = boto3.client("s3")
s3.list_buckets()
```

### Fix 4: Use AWS profile

```bash
# ~/.aws/credentials
[myprofile]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

```python
import boto3

session = boto3.Session(profile_name="myprofile")
s3 = session.client("s3")
```

### Fix 5: Assume an IAM role

```python
import boto3

sts = boto3.client("sts")
credentials = sts.assume_role(
    RoleArn="arn:aws:iam::123456789012:role/MyRole",
    RoleSessionName="my-session",
)["Credentials"]

s3 = boto3.client(
    "s3",
    aws_access_key_id=credentials["AccessKeyId"],
    aws_secret_access_key=credentials["SecretAccessKey"],
    aws_session_token=credentials["SessionToken"],
)
```

### Fix 6: Validate credentials before use

```python
import boto3
from botocore.exceptions import NoCredentialsError

try:
    sts = boto3.client("sts")
    identity = sts.get_caller_identity()
    print(f"Authenticated as: {identity['Arn']}")
except NoCredentialsError:
    print("No valid AWS credentials found")
```

## Related Errors

- {{< relref "importerror-boto3" >}} — boto3 import or installation issue.
- {{< relref "connectionrefusederror" >}} — Connection refused to AWS endpoint.
