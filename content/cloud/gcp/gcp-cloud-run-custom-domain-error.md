---
title: "[Solution] GCP Cloud Run Custom Domain Error"
description: "Fix Cloud Run custom domain errors. Resolve domain mapping, SSL certificates, and custom domain configuration issues in Google Cloud Run."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Run Custom Domain Error

The Cloud Run Custom Domain error occurs when custom domain mappings fail to configure or SSL certificates cannot be provisioned.

## Common Causes

- DNS records are not properly configured
- Domain is not verified in Google Search Console
- SSL certificate provisioning is pending
- Domain mapping conflicts with existing mappings
- Cloud Run API is not enabled

## How to Fix

### 1. Verify domain ownership
```bash
gcloud domains verify DOMAIN_NAME
```

### 2. Create domain mapping
```bash
gcloud run domain-mappings create \
  --service=SERVICE_NAME \
  --domain=DOMAIN_NAME \
  --region=REGION
```

### 3. Check mapping status
```bash
gcloud run domain-mappings describe DOMAIN_NAME \
  --region=REGION --format="yaml(status)"
```

### 4. Create DNS records
```bash
gcloud run domain-mappings describe DOMAIN_NAME \
  --region=REGION --format="yaml(status.resourceRecords)"
```

## Examples

### Verify DNS configuration
```bash
dig DOMAIN_NAME A
dig DOMAIN_NAME CNAME
```

### Check SSL certificate status
```bash
gcloud run domain-mappings describe DOMAIN_NAME \
  --region=REGION --format="yaml(status.conditions)"
```

## Related Errors

- [GCP Cloud Run Service]({{< relref "/cloud/gcp/gcp-cloud-run-service" >}})
- [GCP Cloud DNS Error]({{< relref "/cloud/gcp/gcp-cloud-dns-error" >}})
