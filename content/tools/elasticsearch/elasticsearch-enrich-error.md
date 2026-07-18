---
title: "[Solution] Elasticsearch Enrich Error"
description: "Fix Elasticsearch enrich errors. Learn why this happens and how to resolve it quickly."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Elasticsearch Enrich Error

Elasticsearch enrich errors occur when enrich processors fail to add data from source indices.

## Why This Happens

- Enrich policy not found
- Enrich index missing
- Field mismatch
- Processor error

## Common Error Messages

- `enrich_policy_error`
- `enrich_index_error`
- `enrich_field_error`
- `enrich_processor_error`

## How to Fix It

### Solution 1: Create enrich policy

Define an enrich policy:

```bash
curl -X PUT "localhost:9200/_enrich/policy/my-policy" \
  -H 'Content-Type: application/json' \
  -d '{"match":{"indices":"source-index","match_field":"id","enrich_fields":["name","email"]}}'
```

### Solution 2: Execute enrich policy

Populate the enrich index:

```bash
curl -X POST "localhost:9200/_enrich/policy/my-policy/_execute"
```

### Solution 3: Use enrich processor

Add to ingest pipeline:

```json
{"enrich":{"policy_name":"my-policy","field":"user_id","target_field":"user_info"}}
```


## Common Scenarios

- **Enrich policy not found:** Check the policy name.
- **No data enriched:** Verify the enrich index has data.

## Prevent It

- Create enrich policies
- Execute regularly
- Monitor enrich index
