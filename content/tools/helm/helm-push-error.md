---
title: "[Solution] Helm Push To OCI Registry Failed Error Fix"
description: "Fix 'helm push to OCI registry failed' errors. Resolve chart push issues with OCI registries and authentication."
tools: ["helm"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Helm Push To OCI Registry Failed Error Fix

The helm push to OCI registry failed error occurs when Helm cannot push a chart to an OCI-compatible registry due to authentication, network, or configuration issues.

## What This Error Means

Helm 3 supports OCI registries for chart storage. When pushing charts fails, it is usually due to authentication issues, wrong registry URL, or chart packaging problems.

A typical error:

```
Error: failed to push chart: UNAUTHORIZED: authentication required
```

## Why It Happens

Common causes include:

- **Not logged in** — Registry credentials not provided.
- **Wrong registry URL** — Pushing to wrong endpoint.
- **Chart not packaged** — Chart must be packaged before push.
- **Permission denied** — Account lacks push permissions.
- **Network issues** — Cannot reach registry.
- **TLS issues** — Self-signed certificates not trusted.

## How to Fix It

### Fix 1: Login to registry first

```bash
# RIGHT: Login to OCI registry
helm registry login ghcr.io -u username -p password

# Or use credential helper
helm registry login ghcr.io
```

### Fix 2: Package chart before pushing

```bash
# RIGHT: Package and push
helm package mychart/
helm push mychart-0.1.0.tgz oci://ghcr.io/myorg
```

### Fix 3: Use correct OCI URL format

```bash
# RIGHT: OCI registry URL format
helm push mychart-0.1.0.tgz oci://ghcr.io/myorg/charts
helm push mychart-0.1.0.tgz oci://registry.example.com/team
```

### Fix 4: Handle TLS issues

```bash
# RIGHT: Configure insecure registries
helm push mychart-0.1.0.tgz oci://localhost:5000 --insecure

# Or add CA certificate
helm push mychart-0.1.0.tgz oci://registry.example.com --ca-file ca.crt
```

### Fix 5: Verify chart is valid

```bash
# RIGHT: Lint before push
helm lint mychart/
helm package mychart/
helm push mychart-0.1.0.tgz oci://ghcr.io/myorg
```

## Common Mistakes

- **Pushing unpackaged chart** — Must run `helm package` first.
- **Using docker login instead of helm registry login** — Helm uses different auth.
- **Forgetting OCI support is experimental** — Enable with HELM_EXPERIMENTAL_OCI=1 in Helm 2.

## Related Pages

- [Helm Registry Error](helm-registry-error) — Registry auth issues
- [Helm Render Error](helm-render-error) — Template rendering issues
- [Helm Schema Error](helm-schema-error) — Values schema issues
