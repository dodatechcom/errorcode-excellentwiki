---
title: "[Solution] Grafana Annotation Error"
description: "Fix Grafana annotation errors. Learn why this happens and how to resolve it quickly."
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Grafana Annotation Error

Grafana annotation errors occur when annotations fail to display, query, or create correctly.

## Why This Happens

- Annotation not found
- Query failed
- Permission denied
- Annotation limit exceeded

## Common Error Messages

- `annotation_not_found`
- `annotation_query_error`
- `annotation_permission_error`
- `annotation_limit_error`

## How to Fix It

### Solution 1: Add annotations

Create annotations via API or UI:

```bash
curl -X POST http://grafana:3000/api/annotations \
  -H "Content-Type: application/json" \
  -d '{"text":"Deploy v1.2.3"}'
```

### Solution 2: Query annotations

Use the Annotations view in dashboards.

### Solution 3: Check permissions

Verify annotation permissions in settings.


## Common Scenarios

- **Annotation not showing:** Check the time range and filter.
- **Cannot create:** Verify you have Editor or Admin role.

## Prevent It

- Use tags for filtering
- Set annotation limits
- Document annotation policies
