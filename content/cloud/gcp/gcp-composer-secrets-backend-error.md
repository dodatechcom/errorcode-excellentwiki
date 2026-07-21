---
title: "[Solution] GCP Cloud Composer Secrets Backend Error"
description: "Fix Cloud Composer secrets backend errors. Resolve Airflow Fernet key, secrets manager backend, and encryption issues in Composer."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Composer Secrets Backend Error

The Cloud Composer Secrets Backend error occurs when Airflow cannot access or decrypt secrets stored in the configured secrets backend.

## Common Causes

- Fernet key is not configured or has been rotated without updating Composer
- Secret Manager backend is not enabled for the environment
- Service account lacks Secret Manager access
- Secrets backend configuration is incorrect
- Fernet key does not match across workers and scheduler

## How to Fix

### 1. Check secrets backend configuration
```bash
gcloud composer environments describe ENV_NAME \
  --location=REGION \
  --format="yaml(config.softwareConfig.envVariables)"
```

### 2. Enable Secret Manager backend
```bash
gcloud composer environments update ENV_NAME \
  --location=REGION \
  --update-env-vars=AIRFLOW__SECRETS__BACKEND=airflow.providers.google.cloud.secrets.secret_manager.SecretManagerBackend
```

### 3. Grant Secret Manager access
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

### 4. Check Fernet key
```bash
gcloud composer environments describe ENV_NAME \
  --location=REGION \
  --format="yaml(config.softwareConfig.envVariables.AIRFLOW__CORE__FERNET_KEY)"
```

## Examples

### Set secrets backend with key prefix
```bash
gcloud composer environments update ENV_NAME \
  --location=REGION \
  --update-env-vars=\
AIRFLOW__SECRETS__BACKEND=airflow.providers.google.cloud.secrets.secret_manager.SecretManagerBackend,\
AIRFLOW__SECRETS__BACKEND_KWARGS={\"connections_prefix\": \"airflow/connections\",\"variables_prefix\": \"airflow/variables\"}
```

### Verify secrets access
```bash
gcloud secrets list --format="table(name,labels)"
```

## Related Errors

- [GCP Composer Error]({{< relref "/cloud/gcp/gcp-composer-error" >}})
- [GCP Secret Manager Error]({{< relref "/cloud/gcp/gcp-secret-manager-error" >}})
