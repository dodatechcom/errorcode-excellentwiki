---
title: "[Solution] Terraform GCP Project Not Found"
description: "Fix Terraform GCP project not found errors when the specified GCP project doesn't exist."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

GCP project not found errors occur when the project doesn't exist:

```
Error: Error reading Project "my-project"

googleapi: Error 403: The caller does not have permission,
project not found or access denied.
```

## Common Causes

- Project ID is incorrect.
- Project was deleted.
- IAM permissions insufficient.

## How to Fix

**Verify project exists:**

```bash
gcloud projects describe my-project
```

**Check permissions:**

```bash
gcloud projects get-iam-policy my-project
```

**Create the project in Terraform:**

```hcl
resource "google_project" "main" {
  name            = "My Project"
  project_id      = "my-project-123"
  billing_account = var.billing_account
}
```

## Examples

```hcl
provider "google" {
  project = "my-project-123"
  region  = "us-central1"
}
```
