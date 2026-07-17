---
title: "[Solution] DynamoDB Table Not Found - Fix ResourceNotFoundException"
description: "Fix DynamoDB ResourceNotFoundException by verifying the exact table name spelling, confirming the correct AWS region and account ID, and checking stack status"
tools: ["dynamodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A DynamoDB `ResourceNotFoundException` occurs when a request references a table or index that does not exist. The error has HTTP status code 400 and the AWS error code is `ResourceNotFoundException`.

## What This Error Means

DynamoDB cannot find the specified table in the requested region and account. This is distinct from `AccessDeniedException` (where the table exists but you lack permission) and `ValidationException` (where the request is malformed). The table may have been deleted, never created, or the request is targeting the wrong region.

## Why It Happens

- Table was deleted in a previous deployment
- Table name is misspelled or has different casing
- Request targets the wrong AWS region
- Request targets the wrong AWS account
- Table is in a different account and cross-account access is not configured
- Table name in the code does not match the name in DynamoDB
- CDK or CloudFormation stack deleted the table

## How to Fix It

### 1. List Tables in the Target Region

```bash
aws dynamodb list-tables --region us-east-1
```

### 2. Verify Table Details

```bash
aws dynamodb describe-table --table-name my-table --region us-east-1
```

### 3. Check the Region in the Client

```python
import boto3

# Ensure the client targets the correct region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('my-table')
```

### 4. Check the Account

```python
# Verify the current account
sts = boto3.client('sts')
identity = sts.get_caller_identity()
print(f"Account: {identity['Account']}")
```

### 5. Create the Table if Missing

```python
dynamodb = boto3.client('dynamodb')

try:
    dynamodb.describe_table(TableName='my-table')
except dynamodb.exceptions.ResourceNotFoundException:
    dynamodb.create_table(
        TableName='my-table',
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'}
        ],
        BillingMode='PAY_PER_REQUEST'
    )
```

### 6. Check CloudFormation or CDK Stack Status

```bash
aws cloudformation describe-stacks --stack-name my-stack
# Look for table resources and their status
```

## Common Mistakes

- Hardcoding table names instead of using CloudFormation outputs or SSM parameters
- Not specifying the region in the boto3 client when running in a different default region
- Assuming table names are the same across staging and production environments
- Not handling `ResourceNotFoundException` in application code during first-time deployment
- Not using an infrastructure-as-code tool to manage table lifecycle and avoid drift

## Related Pages

- [DynamoDB ValidationException](/tools/dynamodb/dynamodb-validation-error)
- [DynamoDB Access Denied](/tools/dynamodb/dynamodb-access-denied)
- [DynamoDB Backup Error](/tools/dynamodb/dynamodb-backup-error)
