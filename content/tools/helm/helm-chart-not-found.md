---
title: "[Solution] Helm Chart Not Found — Fix Chart Resolution"
description: "Fix Helm chart not found errors. Resolve repository issues, chart names, and version constraints with step-by-step solutions."
---

## What This Error Means

The `chart not found` error means Helm cannot locate the chart specified in the install or upgrade command. This can be a missing repository, incorrect chart name, or version that does not exist.

A typical error:

```
Error: chart "my-chart" matching version not found in my-repo (try "helm search repo my-chart")
```

Or:

```
Error: failed to download "my-repo/my-chart" (hint: running `helm repo update` may help)
```

## Why It Happens

Chart not found errors occur when:

- **Repository not added**: The Helm repository containing the chart was never added.
- **Repository index is stale**: The local repository index is outdated and does not know about newer chart versions.
- **Chart name wrong**: Typo in the chart name or repository prefix.
- **Version does not exist**: The specified version was never published.
- **Private repository access**: The chart is in a private repository without authentication.
- **Repository URL changed**: The chart repository URL was updated and local config is stale.

## How to Fix It

**Step 1: Search for the chart**

```bash
helm search repo my-chart
helm search hub my-chart
```

**Step 2: Update repository index**

```bash
helm repo update
```

**Step 3: Add the repository if missing**

```bash
helm repo add my-repo https://charts.example.com
helm repo update
```

**Step 4: Install without version to get latest**

```bash
helm install my-app my-repo/my-chart
```

**Step 5: Check available versions**

```bash
helm search repo my-chart --versions
```

**Step 6: Authenticate for private repositories**

```bash
# Using basic auth
helm repo add private-repo https://charts.example.com --username user --password pass

# Using OCI registry
helm registry login registry.example.com --username user --password pass
```

## Common Mistakes

- **Forgetting `helm repo update`**: Always update repos before installing or upgrading charts.
- **Wrong repository prefix**: Ensure you use the correct `repo-name/chart-name` format.
- **Not checking version availability**: Verify the version exists with `helm search repo --versions`.
- **Using outdated Helm documentation**: Chart names and versions change. Always search first.

## Related Pages

- [Helm Repository Error](/tools/helm/helm-repository-error/) — Repository configuration issues
- [Helm Values Error](/tools/helm/helm-values-error/) — Values file parsing errors
- [Terraform Module Not Found](/tools/terraform/terraform-module-not-found/) — Module resolution failures
