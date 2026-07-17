---
title: "[Solution] GCP Cloud SQL — connection name invalid"
description: "Fix Cloud SQL connection name invalid. Resolve Cloud SQL connection and proxy issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Cloud SQL connection name invalid error means the Cloud SQL instance connection name used by Cloud SQL Proxy or the application is malformed or points to a non-existent instance.

## What This Error Means

Cloud SQL connections use a connection name in the format `project-id:region:instance-name`. This name is used by Cloud SQL Auth Proxy, App Engine, Cloud Run, and client libraries to establish an authorized connection. An invalid connection name can mean the format is wrong, the instance does not exist, the instance is in a different project, or the caller lacks `cloudsql.instances.connect` permission. The error appears during proxy startup or when the client library attempts to connect.

## Common Causes

- Connection name has wrong format (missing project, region, or instance)
- Instance name is misspelled
- Instance was deleted but the application still references it
- Instance is in a different project than the one being used
- Cloud SQL Admin API not enabled in the project
- Service account lacks `cloudsql.instances.connect` permission
- Instance is in STOPPED state

## How to Fix

### Verify Instance Exists

```bash
gcloud sql instances describe my-instance --format="value(connectionName)"
```

### Check Connection Name Format

```bash
# Correct format: project-id:region:instance-name
echo "my-project:us-central1:my-instance"
```

### List All Instances

```bash
gcloud sql instances list \
  --format="table(name,region,connectionName,status)"
```

### Check Instance Status

```bash
gcloud sql instances describe my-instance \
  --query='state'
```

### Enable Cloud SQL Admin API

```bash
gcloud services enable sqladmin.googleapis.com --project=my-project
```

### Fix Cloud SQL Proxy Connection

```bash
# Correct usage
cloud-sql-proxy my-project:us-central1:my-instance

# Not: cloud-sql-proxy my-instance
# Not: cloud-sql-proxy us-central1:my-instance
```

### Grant Connection Permission

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="serviceAccount:my-sa@my-project.iam.gserviceaccount.com" \
  --role="roles/cloudsql.client"
```

### Test Connection

```bash
gcloud sql connect my-instance --user=admin --database=mydb
```

### Check Instance is Running

```bash
gcloud sql instances describe my-instance \
  --format="value(state)"
# Should show RUNNABLE
```

## Related Errors

- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error-v2" >}}) — permission denied
- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error-v2" >}}) — MySQL connection failed
- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error-v2" >}}) — firewall blocked
