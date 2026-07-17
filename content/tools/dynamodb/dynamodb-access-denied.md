---
title: "[Solution] DynamoDB AccessDeniedException - Fix IAM Permissions"
description: "Fix DynamoDB AccessDeniedException by verifying IAM roles and attached policies, matching resource ARN patterns correctly, and checking VPC endpoint policy rest"
tools: ["dynamodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A DynamoDB `AccessDeniedException` occurs when an IAM principal (user, role, or service) attempts a DynamoDB operation without the required permissions. The error has HTTP status code 403 and indicates the request was authenticated but not authorized.

## What This Error Means

DynamoDB integrates with IAM for access control. Every API call must be authorized by an IAM policy attached to the caller. The `AccessDeniedException` means the IAM policy does not grant the specific action on the target resource. The error message may include the missing permission.

Unlike `ValidationException` (bad request parameters) or `ResourceNotFoundException` (table does not exist), this error is purely an authorization failure.

## Why It Happens

- IAM role or user lacks the required DynamoDB permissions
- Resource-level permissions do not match the target table or index
- Session token has expired or is invalid
- VPC endpoint policy is blocking DynamoDB access
- SCP (Service Control Policy) at the organization level is denying access
- IAM policy condition does not match the request context
- Cross-account access without proper role assumption

## How to Fix It

### 1. Check IAM Permissions

```bash
# Check what policies are attached to the role
aws iam list-attached-role-policies --role-name my-role
aws iam list-role-policies --role-name my-role
```

### 2. Add DynamoDB Permissions

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem",
                "dynamodb:Query",
                "dynamodb:Scan"
            ],
            "Resource": [
                "arn:aws:dynamodb:us-east-1:123456789012:table/my-table",
                "arn:aws:dynamodb:us-east-1:123456789012:table/my-table/index/*"
            ]
        }
    ]
}
```

### 3. Test with IAM Policy Simulator

```bash
aws iam simulate-principal-policy \
    --policy-source-arn arn:aws:iam::123456789012:role/my-role \
    --action-names dynamodb:GetItem \
    --resource-arns arn:aws:dynamodb:us-east-1:123456789012:table/my-table
```

### 4. Check VPC Endpoint Policy

```json
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "dynamodb:*",
            "Resource": "*"
        }
    ]
}
```

### 5. Verify Resource ARN Matches

```python
import boto3

# The resource ARN must match exactly
# This policy only allows access to "my-table", not "my-table-staging"
table_arn = "arn:aws:dynamodb:us-east-1:123456789012:table/my-table"
```

### 6. Check for IAM Conditions

```json
{
    "Effect": "Allow",
    "Action": "dynamodb:*",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "dynamodb:LeadingKeys": "${aws:username}"
        }
    }
}
```

## Common Mistakes

- Using `Resource: *` in a deny statement that blocks all DynamoDB access
- Not including `dynamodb:Scan` or `dynamodb:Query` when only granting `dynamodb:GetItem`
- Forgetting that IAM policy evaluation uses an implicit deny and explicit deny model
- Not checking if a SCP or permission boundary is restricting access

## Related Pages

- [DynamoDB ValidationException](/tools/dynamodb/dynamodb-validation-error)
- [DynamoDB Table Not Found](/tools/dynamodb/dynamodb-table-not-found)
- [DynamoDB Global Table Error](/tools/dynamodb/dynamodb-global-table-error)
