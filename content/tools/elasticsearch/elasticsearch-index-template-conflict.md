---
title: "[Solution] Elasticsearch Index Template Conflict Error"
description: "Fix Elasticsearch index template conflict errors. Resolve overlapping templates causing mapping issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Index Template Conflict Error

Elasticsearch index template conflicts occur when multiple templates match the same index pattern and have overlapping or contradictory settings.

## Common Causes

- Multiple templates with overlapping index patterns
- Conflicting mapping definitions between templates
- Template priority ordering is incorrect

## Common Error Messages

- `template_conflict`
- `index_template_mapping_conflict`
- `overlapping_index_templates`

## How to Fix It

### Solution 1: List matching templates

Check which templates match your index:

```bash
curl -X GET "localhost:9200/_index_template/myindex*?pretty"
```

### Solution 2: Resolve priority conflicts

Set explicit priorities to control template application order:

```bash
curl -X PUT "localhost:9200/_index_template/template_a" -H 'Content-Type: application/json' -d '{
  "index_patterns": ["myindex-*"],
  "priority": 100,
  "template": {
    "settings": { "number_of_shards": 2 }
  }
}'
```

### Solution 3: Merge overlapping patterns

Narrow index patterns so templates do not overlap:

```bash
curl -X DELETE "localhost:9200/_index_template/broad_template"
```

## Prevent It

- Use unique, non-overlapping index patterns
- Assign explicit priorities to templates
- Review templates before creating new ones
