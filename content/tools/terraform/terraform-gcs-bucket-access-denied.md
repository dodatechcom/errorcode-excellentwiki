---
title: "[Solution] Terraform GCS Bucket Access Denied"
description: "Fix Terraform GCS bucket access denied errors when accessing Google Cloud Storage."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

GCS access denied errors occur when the bucket cannot be accessed:

```
Error: Error creating bucket

googleapi: Error 403: Access Not Configured. Cloud Storage
API has not been used in project before or disabled.
```

## Common Causes

- Cloud Storage API not enabled.
- IAM permissions insufficient.

## How to Fix

**Enable the Cloud Storage API:**

```bash
gcloud services enable storage-api.googleapis.com --project=my-project
```

**Grant required permissions:**

```hcl
resource "google_project_iam_member" "storage_admin" {
  project = var.project_id
  role    = "roles/storage.admin"
  member  = "serviceAccount:${var.service_account_email}"
}
```

## Examples

```hcl
resource "google_storage_bucket" "terraform_state" {
  name          = "${var.project_id}-terraform-state"
  location      = "US"
  force_destroy = false

  versioning {
    enabled = true
  }
}
```
