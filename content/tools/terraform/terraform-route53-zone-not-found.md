---
title: "[Solution] Terraform Route53 Zone Not Found"
description: "Fix Terraform Route53 zone not found errors when referencing a non-existent hosted zone."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Route53 zone not found errors occur when the DNS zone doesn't exist:

```
Error: Error reading Route53 Zone

HostedZoneNotFound: The specified hosted zone does not exist.
```

## Common Causes

- Zone was deleted.
- Wrong zone ID.

## How to Fix

**Create the zone in Terraform:**

```hcl
resource "aws_route53_zone" "main" {
  name = "example.com"
}
```

**Use data source for existing zone:**

```hcl
data "aws_route53_zone" "main" {
  name         = "example.com"
  private_zone = false
}
```

## Examples

```hcl
resource "aws_route53_zone" "main" {
  name    = "example.com"
  comment = "Managed by Terraform"
}

resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "www.example.com"
  type    = "A"
  ttl     = 300
  records = [aws_eip.web.public_ip]
}
```
