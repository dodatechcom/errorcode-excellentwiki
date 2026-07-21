---
title: "[Solution] GCP Cloud SQL Connection Refused"
description: "Fix Cloud SQL connection refused errors in GCP. Learn to resolve connectivity, authentication, and network issues with step-by-step solutions."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud SQL Connection Refused

The Cloud SQL Connection Refused error occurs when an application cannot establish a connection to a Cloud SQL instance, often due to network, authentication, or configuration issues.

## Common Causes

- The Cloud SQL instance is stopped or does not exist
- The application is not using the correct IP address or private IP
- Authorized networks do not include the client IP range
- The Cloud SQL Admin API is not enabled in the project
- SSL/TLS certificate requirements are not met
- The Cloud SQL Auth Proxy is not running

## How to Fix

### 1. Verify instance status
```bash
gcloud sql instances describe INSTANCE_NAME --format="value(state)"
```

### 2. Check authorized networks
```bash
gcloud sql instances patch INSTANCE_NAME \
  --assign-ip \
  --no-require-ssl
```

### 3. Add authorized network
```bash
gcloud sql instances patch INSTANCE_NAME \
  --authorized-networks=203.0.113.0/24
```

### 4. Start Cloud SQL Auth Proxy
```bash
cloud-sql-proxy INSTANCE_CONNECTION_NAME \
  --port=5432 \
  --credentials-file=service-account.json
```

### 5. Enable Cloud SQL Admin API
```bash
gcloud services enable sqladmin.googleapis.com --project=PROJECT_ID
```

## Examples

### Connect using Cloud SQL Auth Proxy
```bash
cloud-sql-proxy my-project:us-central1:my-instance --port=5432 &
psql -h 127.0.0.1 -p 5432 -U postgres -d mydb
```

### Test connectivity with gcloud
```bash
gcloud sql connect INSTANCE_NAME --user=postgres
```

## Related Errors

- [GCP Cloud SQL Error]({{< relref "/cloud/gcp/gcp-cloud-sql-error" >}})
- [GCP Connection Error CloudSQL]({{< relref "/cloud/gcp/gcp-connection-error-(cloudsql)" >}})
