---
title: "[Solution] Helm Pull Error — Fix Chart Pull Failed / Authentication Required"
description: "Fix Helm pull errors when downloading charts from repositories fails. Configure authentication, fix repository URLs, and handle private registry access."
---

## What This Error Means

Helm pull errors occur when Helm cannot download a chart from a repository. The repository may require authentication, the URL may be incorrect, or the chart may not exist.

A typical error:

```
Error: failed to fetch https://charts.example.com/charts/my-chart-1.0.0.tgz : 401 Unauthorized
```

Or:

```
Error: looks like "https://charts.example.com" is not a valid chart repository or cannot be reached: 404 Not Found
```

## Why It Happens

Chart pull failures happen when:

- **Repository requires authentication**: OCI or HTTP basic auth credentials are missing.
- **Repository URL is incorrect**: The repository was added with a wrong or outdated URL.
- **Chart does not exist**: The chart name or version was misspelled.
- **Network is blocked**: A firewall or proxy prevents access to the repository.
- **Repository index is outdated**: The local cache has stale metadata.
- **OCI registry permissions**: Missing credentials for OCI-based Helm registries.

## How to Fix It

**Step 1: Update the repository**

```bash
helm repo update
```

**Step 2: List available charts**

```bash
helm search repo <chart-name>
helm show chart <repo>/<chart>
```

**Step 3: Authenticate to the repository**

```bash
helm repo add <repo-name> https://charts.example.com --username <user> --password <pass>
```

For OCI registries:

```bash
helm registry login registry.example.com --username <user> --password <pass>
helm pull oci://registry.example.com/charts/my-chart --version 1.0.0
```

**Step 4: Use an auth token**

```bash
helm repo add <repo-name> https://charts.example.com --password <token>
```

**Step 5: Pull with explicit version**

```bash
helm pull <repo>/<chart> --version 1.0.0
```

**Step 6: Check repository configuration**

```bash
helm repo list
helm repo remove <repo> && helm repo add <repo> <correct-url>
```

## Common Mistakes

- **Not running `helm repo update` before pulling**: The local cache may be stale.
- **Forgetting OCI login for OCI-based registries**: OCI registries require `helm registry login` first.
- **Using HTTP instead of HTTPS**: Many registries require HTTPS.
- **Not specifying chart version**: Pulling without a version pulls the latest, which may not exist.

## Related Pages

- [Helm Repository Error](/tools/helm/helm-repository-error/) -- Repository connection issues
- [Helm Chart Not Found](/tools/helm/helm-chart-not-found/) -- Chart resolution failures
- [Helm Values Error](/tools/helm/helm-values-error/) -- Values configuration issues
