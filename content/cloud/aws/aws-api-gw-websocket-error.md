---
title: "[Solution] AWS API Gateway WebSocket Error — disconnect/timeout failures"
description: "Fix AWS API Gateway WebSocket errors. Resolve WebSocket disconnect, timeout, and connection issues."
error-types: ["api-error"]
severities: ["error"]
weight: 113
---

An AWS API Gateway WebSocket error occurs when WebSocket connections drop unexpectedly, route integrations time out, or message delivery fails. WebSocket APIs require proper route configuration and connection management.

## Common Causes

- $connect route integration timeout
- Idle connection timeout reached (default 10 minutes)
- IAM or Lambda authorizer failing on $connect
- Message payload too large (128 KB limit)
- Disconnect route not configured

## How to Fix

### Check WebSocket API Routes

```bash
aws apigatewayv2 get-routes \
  --api-id my-api-id
```

### List Active Connections

```bash
aws apigatewayv2 get-connections \
  --api-id my-api-id
```

### Update Route Integration

```bash
aws apigatewayv2 update-route \
  --api-id my-api-id \
  --route-id route-xxx \
  --route-key '$connect' \
  --target integrations/integ-xxx
```

### Check Integration Response

```bash
aws apigatewayv2 get-integration \
  --api-id my-api-id \
  --integration-id integ-xxx
```

### Update Stage Settings

```bash
aws apigatewayv2 update-stage \
  --api-id my-api-id \
  --stage-name production \
  --default-route-settings ThrottlingBurstLimit=500,ThrottlingRateLimit=1000
```

## Examples

```bash
# Example 1: Connection timeout
# GONE: Connection timed out
# Fix: implement ping/pong to keep connection alive

# Example 2: Route not found
# NotFoundException: Route not found
# Fix: add $connect and $disconnect routes
```

## Related Errors

- [AWS API Gateway Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) — REST API Gateway errors
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
