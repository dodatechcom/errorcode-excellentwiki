---
title: "[Solution] AWS Certificate Manager Error — cert validation/renewal failures"
description: "Fix AWS ACM errors. Resolve certificate validation, renewal, and import issues."
error-types: ["api-error"]
severities: ["error"]
weight: 125
---

An AWS ACM error occurs when certificate validation fails, auto-renewal breaks, or imported certificates expire unexpectedly. ACM manages TLS/SSL certificates but DNS/email validation must be correctly configured.

## Common Causes

- DNS CNAME record not created or incorrect
- Email validation not confirmed
- Domain ownership not verified
- Certificate nearing expiration without renewal
- Imported certificate private key mismatch

## How to Fix

### List Certificates

```bash
aws acm list-certificates \
  --query 'CertificateSummaryList[*].{ARN:CertificateArn,Domain:DomainName,Status:Status}'
```

### Get Certificate Details

```bash
aws acm describe-certificate \
  --certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/xxx
```

### Request Certificate

```bash
aws acm request-certificate \
  --domain-name example.com \
  --validation-method DNS
```

### Get Validation Records

```bash
aws acm describe-certificate \
  --certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/xxx \
  --query 'Certificate.DomainValidationOptions[*].ResourceRecord'
```

### Import Certificate

```bash
aws acm import-certificate \
  --certificate fileb://cert.pem \
  --private-key fileb://key.pem \
  --certificate-chain fileb://chain.pem
```

## Examples

```bash
# Example 1: Validation pending
# Status: PENDING_VALIDATION
# Fix: create the DNS CNAME record shown in validation options

# Example 2: Renewal failed
# RenewalStatus: FAILED
# Fix: verify DNS validation records are still correct
```

## Related Errors

- [AWS Route53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) — Route53 DNS errors
- [AWS CloudFront Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) — CloudFront errors
- [AWS ELB Error]({{< relref "/cloud/aws/aws-elb-error" >}}) — ALB HTTPS errors
