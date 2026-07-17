---
title: "[Solution] AWS API Gateway Error"
description: "Fix AWS API Gateway errors. Resolve API Gateway configuration and deployment issues."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "api-gateway", "rest-api", "lambda", "proxy"]
weight: 5
---

An AWS API Gateway error occurs when the API Gateway cannot process requests or integrate with backend services.

## Common Causes

- API stage not deployed
- Integration target (Lambda, HTTP) not configured
- Missing API key or usage plan
- Request/response mapping templates are invalid
- CORS configuration missing

## How to Fix

### Check API Stage

```bash
aws apigateway get-stages --rest-api-id abc123
```

### Deploy API

```bash
aws apigateway create-deployment \
  --rest-api-id abc123 \
  --stage-name prod
```

### Test API

```bash
curl -X GET https://abc123.execute-api.us-east-1.amazonaws.com/prod/my-endpoint
```

### Check Integration

```bash
aws apigateway get-integration \
  --rest-api-id abc123 \
  --resource-id xxx \
  --http-method GET
```

### Enable CORS

```bash
aws apigateway enable-cors \
  --rest-api-id abc123 \
  --resource-id xxx \
  --access-control-allow-headers '{"Header": ["Content-Type"]}' \
  --access-control-allow-methods '{"Method": ["GET","POST"]}' \
  --access-control-allow-origins '{"Origin": ["*"]}'
```

## Examples

```bash
# Example 1: Stage not deployed
# 403: Forbidden
# Fix: deploy API to stage

# Example 2: Lambda integration error
# 500: Internal Server Error
# Fix: check Lambda function logs
```

## Related Errors

- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function error
- [AWS CloudFront Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) — CloudFront error
