---
title: "[Solution] Helm Template Error — Fix Template Rendering"
description: "Fix Helm template rendering errors. Resolve Go template syntax issues, missing values, and undefined functions with practical fixes."
---

## What This Error Means

Template rendering errors occur when Helm cannot process the Go templates in chart files. Syntax errors, undefined variables, or missing helper functions cause these errors during `helm template`, `helm install`, or `helm upgrade`.

A typical error:

```
Error: template: my-chart/templates/deployment.yaml:15:34: executing
"my-chart/templates/deployment.yaml" at <.Values.app.port>: can't evaluate
field app in type interface {}
```

Or:

```
Error: template: my-chart/templates/configmap.yaml:22: function "toYaml" not defined
```

## Why It Happens

Template errors occur when:

- **Undefined values**: Templates reference `.Values.xxx` that is not defined in values.yaml or user overrides.
- **Wrong template syntax**: Go template syntax errors such as unclosed braces or wrong function calls.
- **Missing helper templates**: The template references a partial or include that does not exist.
- **Incorrect function usage**: Using a Helm function with wrong arguments or wrong types.
- **Nil pointer dereference**: Accessing a property of a nil value without checking.
- **Encoding issues**: Non-ASCII characters or BOM in template files.

## How to Fix It

**Step 1: Render templates locally to debug**

```bash
helm template my-release my-repo/my-chart -f values.yaml
```

**Step 2: Check the specific template file**

Look at the line number in the error and inspect the template:

```yaml
# Check for undefined values
{{ .Values.app.port }}

# Fix: Add default or check
{{ .Values.app.port | default 8080 }}
```

**Step 3: Use `--debug` to see rendered output**

```bash
helm template my-release my-repo/my-chart --debug
```

**Step 4: Verify values.yaml has all required fields**

Compare template references against values.yaml:

```bash
# Find all .Values references
grep -r "\.Values\." my-chart/templates/
```

**Step 5: Fix common Go template issues**

```yaml
# WRONG - accessing nil
{{ .Values.app.name }}

# CORRECT - check if defined
{{ if .Values.app }}{{ .Values.app.name }}{{ end }}

# WRONG - incorrect indentation with toYaml
{{ toYaml .Values.labels }}

# CORRECT
{{- toYaml .Values.labels | nindent 4 }}
```

**Step 6: Use raw templates for non-Kubernetes YAML**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-config
data:
  config.yaml: |-
    {{- .Values.config | toYaml | nindent 4 }}
```

## Common Mistakes

- **Not testing with `helm template` before deploying**: Always render templates locally to catch errors.
- **Using wrong indentation with `nindent`**: `nindent` adds a newline and indentation. Use `indent` if you do not want the newline.
- **Forgetting to define default values**: Always provide sensible defaults in `values.yaml` for optional values.
- **Mixing `{{` and `{{-`**: Use `{{-` to trim whitespace before the expression.

## Related Pages

- [Helm Values Error](/tools/helm/helm-values-error/) — Values file parsing issues
- [Helm Chart Not Found](/tools/helm/helm-chart-not-found/) — Chart resolution failures
- [Ansible Syntax Error](/tools/ansible/ansible-syntax-error/) — Playbook syntax issues
