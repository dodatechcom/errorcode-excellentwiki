---
title: "[Solution] AWS AppSync Error — resolver/data-source/API-key failures"
description: "Fix AWS AppSync errors. Resolve resolver, data source, and API key issues."
error-types: ["api-error"]
severities: ["error"]
weight: 149
---

An AWS AppSync error occurs when GraphQL resolvers fail, data sources are inaccessible, or API key authentication breaks. AppSync provides managed GraphQL but requires proper resolver and data source configuration.

## Common Causes

- Resolver mapping template has syntax errors
- Data source Lambda function does not exist
- API key expired or not enabled
- VPC data source connection timeout
- Conflict detection/resolution not configured

## How to Fix

### List APIs

```bash
aws appsync list-graphql-apis \
  --query 'graphqlApis[*].{ID:id,Name:name,Endpoint:apiUrl}'
```

### Get API Details

```bash
aws appsync get-graphql-api \
  --api-id my-api-id
```

### List Resolvers

```bash
aws appsync list-resolvers \
  --api-id my-api-id \
  --type-name Query
```

### Create API Key

```bash
aws appsync create-api-key \
  --api-id my-api-id \
  --description "CI/CD key" \
  --expires $(date -u -d '+90 days' +%s)
```

### Create Data Source

```bash
aws appsync create-data-source \
  --api-id my-api-id \
  --name my-lambda-ds \
  --type AWS_LAMBDA \
  --service-role-arn arn:aws:iam::123456789012:role/AppSyncLambdaRole \
  --lambda-config lambda-function-arn=arn:aws:lambda:us-east-1:123456789012:function:my-function
```

## Examples

```bash
# Example 1: Resolver failed
# MappingTemplate: Syntax error in VTL template
# Fix: validate VTL mapping template syntax

# Example 2: API key expired
# AuthenticationException: API key has expired
# Fix: create new API key with future expiration
```

## Related Errors

- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS DynamoDB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) — DynamoDB table errors
