---
title: "[Solution] Terraform Cloud Error - Fix Terraform Cloud Authentication Failed"
description: "Fix Terraform Cloud authentication failures. Resolve token, workspace, and API key issues for Terraform Cloud and TFCE integration."
tools: ["terraform"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

This error means Terraform cannot authenticate with Terraform Cloud (formerly Terraforce Enterprise). The API token may be invalid, expired, or the workspace configuration is wrong.

## What This Error Means

When Terraform tries to communicate with Terraform Cloud and authentication fails, you see:

```
Error: Failed to authenticate with Terraform Cloud
# or
Error: Unauthorized: authentication required
# or
Error: Error refreshing state: unauthorized
```

Terraform Cloud requires a valid API token and correct workspace association. Authentication failures block all remote operations.

## Why It Happens

- The API token has expired or been revoked
- The token does not have the required scopes or permissions
- The workspace name or organization is misspelled in the backend configuration
- You are using a user token instead of a team token
- The Terraform Cloud instance URL is incorrect
- A network firewall blocks requests to Terraform Cloud

## How to Fix It

### Verify your API token

```bash
curl -H "Authorization: Bearer $TF_TOKEN" \
  https://app.terraform.io/api/v2/account/details
```

A 200 response confirms the token is valid.

### Set the token correctly

```bash
export TF_TOKEN=$(echo "app.terraform.io" | base64)
```

Or create a `~/.terraform.d/credentials.tfrc.json`:

```json
{
  "credentials": {
    "app.terraform.io": {
      "token": "your-api-token-here"
    }
  }
}
```

### Check backend configuration

```hcl
terraform {
  cloud {
    organization = "my-org"
    workspaces {
      name = "my-workspace"
    }
  }
}
```

Ensure the organization and workspace names match exactly.

### Use the correct hostname for TFC/TFE

```hcl
terraform {
  cloud {
    hostname = "terraform.company.com"
    organization = "my-org"
    workspaces { name = "prod" }
  }
}
```

Use `hostname` for Terraform Enterprise instances.

### Check token scopes

```bash
# Create a new token with correct scopes at:
# https://app.terraform.io/app/settings/tokens
```

Team tokens should have the appropriate workspace access level.

### Verify network connectivity

```bash
curl -I https://app.terraform.io
```

Ensure your network allows HTTPS connections to Terraform Cloud.

## Common Mistakes

- Using a personal API token that has expired
- Not base64-encoding the token in the credentials file
- Typo in the organization or workspace name
- Using `TF_CLOUD_TOKEN` environment variable instead of `TF_TOKEN`
- Forgetting that Terraform Cloud uses organization-level tokens, not per-workspace

## Related Pages

- [Terraform Backend Error]({{< relref "/tools/terraform/terraform-backend-error" >}}) -- backend configuration
- [Terraform State Locked]({{< relref "/tools/terraform/terraform-state-locked" >}}) -- state locking
- [Terraform Provider Error]({{< relref "/tools/terraform/terraform-provider-error" >}}) -- provider issues
