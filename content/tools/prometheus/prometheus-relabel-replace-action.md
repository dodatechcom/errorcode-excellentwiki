---
title: "[Solution] Prometheus Relabel Replace Action Error"
description: "How to fix Prometheus relabel replace action not producing expected output"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replacement string referencing non-existent capture groups
- Source labels not producing expected values
- Regex not matching the input
- Replacement using wrong group index

## How to Fix

Use correct replacement syntax:

```yaml
relabel_configs:
  - source_labels: [__address__]
    regex: '(.*):(.*)'
    target_label: host
    replacement: '${1}'
    action: replace
```

Valid capture group references:

```yaml
replacement: '${1}'        # First capture group
replacement: '${2}'        # Second capture group
replacement: '${1}:${2}'   # Combine groups
replacement: '${0}'        # Entire match
replacement: 'prefix_${1}' # Static prefix + group
```

Test regex and replacement:

```bash
echo "web-01:8080" | sed -E 's/(.*):(.*)/host= port=/'
# Output: host=web-01 port=8080
```

## Examples

```bash
# Test replacement
echo "10.0.1.5:9090" | sed -E 's/([0-9]+\.[0-9]+\.[0-9]+)\.([0-9]+)/.0/'

# Check applied labels
curl -s 'http://localhost:9090/api/v1/query?query=up' | jq '.data.result[0].metric'
```
