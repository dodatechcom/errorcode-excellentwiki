---
title: "[Solution] GCP Cloud Run VPC Connector Error"
description: "Fix Cloud Run VPC connector errors. Resolve Serverless VPC Access, connectivity, and network access issues in Google Cloud Run."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Run VPC Connector Error

The Cloud Run VPC Connector error occurs when Cloud Run services cannot access VPC resources through a Serverless VPC Access connector.

## Common Causes

- VPC connector is not in the same region as the Cloud Run service
- Connector is in a STOPPED or ERROR state
- Firewall rules block connector traffic
- Connector subnet does not have enough IP addresses
- Cloud Run egress setting is not configured for VPC

## How to Fix

### 1. Check connector status
```bash
gcloud compute networks vpc-access connectors describe CONNECTOR_NAME \
  --region=REGION
```

### 2. Create VPC connector
```bash
gcloud compute networks vpc-access connectors create CONNECTOR_NAME \
  --network=VPC_NAME \
  --region=REGION \
  --range=10.8.0.0/28
```

### 3. Deploy Cloud Run with VPC connector
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE \
  --vpc-connector=CONNECTOR_NAME \
  --region=REGION
```

### 4. Set VPC egress
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE \
  --vpc-connector=CONNECTOR_NAME \
  --vpc-egress=all-traffic \
  --region=REGION
```

## Examples

### Check connector health
```bash
gcloud compute networks vpc-access connectors describe my-connector \
  --region=us-central1 \
  --format="yaml(state,ipCidrRange,network)"
```

### Deploy with private IP access
```bash
gcloud run deploy my-service \
  --image=gcr.io/my-project/my-image \
  --vpc-connector=my-connector \
  --vpc-egress=all-traffic \
  --region=us-central1
```

## Related Errors

- [GCP Cloud Run Error]({{< relref "/cloud/gcp/gcp-cloud-run-error" >}})
- [GCP VPC Error]({{< relref "/cloud/gcp/gcp-vpc-error" >}})
