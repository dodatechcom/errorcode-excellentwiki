---
title: "[Solution] Python boto3 Error — AWS SDK Failures"
description: "Fix Python boto3 errors like ClientError, NoCredentialsError, ParamValidationError, and region errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 426
---

# Python boto3 Error — AWS SDK Failures

boto3 errors occur when AWS credentials are missing, parameters are invalid, regions are misconfigured, or the AWS service returns an error response. These are common in cloud infrastructure and serverless development.

## Common Causes

```python
# NoCredentialsError: AWS credentials not found
import boto3
s3 = boto3.client("s3")
s3.list_buckets()  # no credentials configured

# ClientError: invalid bucket name
s3 = boto3.client("s3", region_name="us-east-1")
s3.create_bucket(Bucket="INVALID_BUCKET_NAME!")

# ParamValidationError: invalid parameter type
s3.put_object(Bucket="my-bucket", Key="file.txt", Body=12345)  # Body must be bytes

# ClientError: access denied
s3 = boto3.client("s3")
s3.delete_object(Bucket="other-account-bucket", Key="file.txt")

# ValueError: region name is invalid
ec2 = boto3.client("ec2", region_name="invalid-region-999")
```

## How to Fix

### Fix 1: Configure AWS Credentials
Set up credentials using environment variables, config files, or IAM roles.
```bash
# Environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1

# Or use AWS CLI
aws configure
```
```python
import boto3

# Explicit credentials (not recommended for production)
session = boto3.Session(
    aws_access_key_id="YOUR_KEY",
    aws_secret_access_key="YOUR_SECRET",
    region_name="us-east-1"
)
s3 = session.client("s3")
```

### Fix 2: Validate Parameters Before Calling AWS
Ensure parameter types and values are correct.
```python
import boto3
import os

s3 = boto3.client("s3")
file_path = "data.txt"

if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        s3.put_object(Bucket="my-bucket", Key="data.txt", Body=f.read())
```

### Fix 3: Handle AWS Service Errors Gracefully
Use try/except to handle specific error codes.
```python
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")
try:
    s3.head_bucket(Bucket="my-bucket")
except ClientError as e:
    error_code = e.response["Error"]["Code"]
    if error_code == "404":
        print("Bucket does not exist")
    elif error_code == "403":
        print("Access denied to bucket")
    else:
        raise
```

### Fix 4: Specify Valid Regions
Use supported AWS region names.
```python
import boto3

# Valid regions
ec2 = boto3.client("ec2", region_name="us-east-1")
s3 = boto3.client("s3", region_name="us-west-2")
```

### Fix 5: Use IAM Roles for EC2/Lambda
Instead of hardcoding credentials, use IAM roles when running on AWS infrastructure.
```python
import boto3

# boto3 automatically picks up IAM role credentials
s3 = boto3.client("s3")
response = s3.list_buckets()
```

## Examples

```python
# S3 file upload with error handling
import boto3
from botocore.exceptions import ClientError, NoCredentialsError
import os

def upload_file(file_path, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)

    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_path, bucket, object_name)
        print(f"Uploaded {file_path} to s3://{bucket}/{object_name}")
        return True
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return False
    except NoCredentialsError:
        print("AWS credentials not available")
        return False
    except ClientError as e:
        print(f"AWS error: {e}")
        return False
```

## Related Errors

- [Python Paramiko Error](/languages/python/python-paramiko-error/)
- [Python redis-py Error](/languages/python/python-redis-py-error/)
- [Python PyMongo Error](/languages/python/python-pymongo-error/)
