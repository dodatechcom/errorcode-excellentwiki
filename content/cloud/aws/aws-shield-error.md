---
title: "[Solution] AWS Shield Advanced Error — protection/DRT failures"
description: "Fix AWS Shield Advanced errors. Resolve Shield Advanced protection, DRT, and mitigation issues."
error-types: ["api-error"]
severities: ["error"]
weight: 116
---

An AWS Shield Advanced error occurs when DRT access is not configured, protections fail to apply, or mitigation requests encounter permission issues. Shield Advanced provides DDoS protection but requires proper setup.

## Common Causes

- DRT (DDoS Response Team) not authorized
- Shield Advanced not enabled for the account
- Resource type not supported for protection
- Emergency contacts not configured
- Protection ARN not found or already deleted

## How to Fix

### Check Shield Subscription

```bash
aws shield get-subscription-state \
  --subscription-arn arn:aws:shield::123456789012:subscription/xxx
```

### List Protections

```bash
aws shield list-protections \
  --query 'Protections[*].{ID:Id,Name:Name,ResourceArn:ResourceArn}'
```

### Authorize DRT Access

```bash
aws shield authorize-drt-access \
  --subscription-arn arn:aws:shield::123456789012:subscription/xxx \
  --role-arn arn:aws:iam::123456789012:role/ShieldDRTAccess
```

### Create Protection

```bash
aws shield create-protection \
  --name my-alb-protection \
  --resource-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-alb/xxx
```

### Set Emergency Contacts

```bash
aws shield update-emergency-contact-settings \
  --emergency-contact-list EmailAddress=security@company.com
```

## Examples

```bash
# Example 1: DRT not authorized
# ForbiddenException: DRT access not authorized
# Fix: run authorize-drt-access with correct IAM role

# Example 2: Protection not found
# ResourceNotFoundException: Protection not found
# Fix: verify protection ARN or create new protection
```

## Related Errors

- [AWS WAF Error]({{< relref "/cloud/aws/aws-waf-error" >}}) — WAF rule/ACL errors
- [AWS CloudFront Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) — CloudFront distribution errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
