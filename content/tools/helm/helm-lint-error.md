---
title: "[Solution] Helm Lint Error — Fix Chart Linting Failed / Validation Error"
description: "Fix Helm lint errors when chart validation fails. Resolve YAML syntax issues, missing required fields, and template rendering problems during helm lint."
---

## What This Error Means

Helm lint errors occur when a chart fails validation checks. The `helm lint` command examines Chart.yaml, values files, and templates for common errors.

A typical error:

```
==> Linting .
[ERROR] Chart.yaml: apiVersion is required
[ERROR] values.yaml: cannot unmarshal !!str `truee` into bool
[ERROR] templates/: template: my-chart/templates/deployment.yaml:6: function "nonexistent" not defined
```

## Why It Happens

Linting failures happen when:

- **Chart.yaml missing required fields**: Missing `apiVersion`, `name`, `version`, or `description`.
- **Invalid YAML syntax**: Malformed YAML in Chart.yaml, values.yaml, or template files.
- **Undefined template functions**: Using Sprig or Flow Control functions that do not exist.
- **Invalid version string**: The chart version does not follow semantic versioning.
- **Missing dependencies**: Required dependencies are not in the charts/ directory or not downloaded.
- **Deprecated fields**: Using chart API fields that are no longer supported.

## How to Fix It

**Step 1: Run lint with verbose output**

```bash
helm lint ./my-chart --verbose
```

**Step 2: Validate Chart.yaml**

```yaml
apiVersion: v2
name: my-chart
description: A Helm chart for Kubernetes
version: 0.1.0
appVersion: "1.0.0"
```

**Step 3: Check YAML syntax**

```bash
python3 -c "import yaml; yaml.safe_load(open('Chart.yaml'))"
```

**Step 4: Fix common template errors**

Check for undefined variables:

```yaml
# Wrong
{{ .Values.nonexistent }}

# Correct way with default
{{ .Values.mykey | default "fallback" }}
```

**Step 5: Update dependencies**

```bash
helm dependency update ./my-chart
```

**Step 6: Lint with strict mode**

```bash
helm lint ./my-chart --strict
```

## Common Mistakes

- **Not running `helm lint` before packaging**: Always lint before committing or publishing.
- **Ignoring warnings during lint**: Warnings can become errors with strict mode.
- **Forgetting to update Chart.yaml version after changes**: Version must follow semver.
- **Using deprecated apiVersion v1**: Helm v3 requires apiVersion v2.

## Related Pages

- [Helm Template Error](/tools/helm/helm-template-error/) -- Template rendering issues
- [Helm Values Error](/tools/helm/helm-values-error/) -- Values configuration
- [Helm Chart Not Found](/tools/helm/helm-chart-not-found/) -- Chart resolution failures
