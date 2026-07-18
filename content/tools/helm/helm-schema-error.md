---
title: "[Solution] Helm Values Schema Validation Failed Error Fix"
description: "Fix 'values schema validation failed' errors in Helm. Create and debug JSON Schema files for chart values validation."
tools: ["helm"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Helm Values Schema Validation Failed Error Fix

The values schema validation failed error occurs when provided values do not match the JSON Schema defined in values.schema.json.

## What This Error Means

Helm charts can include a values.schema.json file that validates input values. When values do not match the schema (wrong types, missing required fields, invalid patterns), Helm rejects them.

A typical error:

```
Error: values don't meet the specifications of the schema(s) 
in the following schema(s):
values.schema.json:
  - replicas: integer is required
```

## Why It Happens

Common causes include:

- **Wrong value type** — String provided where integer expected.
- **Missing required field** — Required value not provided.
- **Value out of range** — Number outside allowed minimum/maximum.
- **Pattern mismatch** — String does not match regex pattern.
- **Schema file wrong** — values.schema.json has errors.
- **Enum mismatch** — Value not in allowed list.

## How to Fix It

### Fix 1: Check schema requirements

```bash
# RIGHT: View schema
cat values.schema.json | jq .

# Lint chart to check schema
helm lint mychart/ -f my-values.yaml
```

### Fix 2: Create proper values schema

```json
{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["image", "replicas"],
  "properties": {
    "image": {
      "type": "string",
      "pattern": "^[a-z]+:[a-z0-9]+$"
    },
    "replicas": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10
    },
    "resources": {
      "type": "object",
      "properties": {
        "cpu": { "type": "string" },
        "memory": { "type": "string" }
      }
    }
  }
}
```

### Fix 3: Provide correct values

```yaml
# values.yaml (defaults)
image: nginx:latest
replicas: 3

# my-values.yaml (overrides)
replicas: 5
resources:
  cpu: "100m"
  memory: "128Mi"
```

### Fix 4: Skip validation temporarily

```bash
# RIGHT: Skip schema validation (temporary)
helm install myrelease mychart/ --skip-schema-validation
```

### Fix 5: Debug schema errors

```bash
# RIGHT: Validate with helm
helm template myrelease mychart/ -f values.yaml

# Check specific error
helm lint mychart/ -f values.yaml
```

## Common Mistakes

- **Not providing values.schema.json** — Schema validation only works with schema file.
- **Schema too strict** — Use additionalProperties: false carefully.
- **Forgetting that defaults must also match schema** — defaults in values.yaml must be valid.

## Related Pages

- [Helm Render Error](helm-render-error) — Template rendering issues
- [Helm Notation Error](helm-notation-error) — Secrets issues
- [Helm CRDs Error](helm-crds-error) — CRD installation issues
