---
title: "[Solution] Elasticsearch Watcher Trigger Error"
description: "Fix Elasticsearch watcher trigger errors. Resolve issues with Watcher failing to execute or schedule alerts."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Watcher Trigger Error

Elasticsearch Watcher trigger errors occur when a watch fails to execute its trigger schedule or encounters errors during its input, condition, or action phases.

## Common Causes

- Watcher license expired or not available
- Invalid cron expression in the trigger schedule
- Input query referencing a non-existent index
- Action webhook endpoint unreachable

## Common Error Messages

- `watcher_trigger_exception`
- `invalid_cron_expression`
- `watch_input_exception`
- `watch_action_exception`

## How to Fix It

### Solution 1: Check watch status

View active watches and their status:

```bash
curl -X GET "localhost:9200/_watcher/watch?pretty"
```

### Solution 2: Validate cron expression

Test your cron schedule:

```bash
curl -X PUT "localhost:9200/_watcher/watch/my_watch" -H 'Content-Type: application/json' -d '{
  "trigger": {
    "schedule": {
      "cron": { "expression": "0 */5 * * * ?", "tz": "UTC" }
    }
  },
  "input": {
    "search": {
      "request": {
        "indices": ["myindex"],
        "body": { "query": { "match_all": {} } }
      }
    }
  },
  "condition": { "script": { "source": "ctx.payload.hits.total > 0" } },
  "actions": {
    "log_it": {
      "logging": { "text": "Watch triggered" }
    }
  }
}'
```

### Solution 3: Execute watch manually

Trigger a watch for testing:

```bash
curl -X POST "localhost:9200/_watcher/watch/my_watch/_execute"
```

## Prevent It

- Validate cron expressions before deploying watches
- Ensure the Watcher feature is available in your license tier
- Test watches manually before relying on scheduled execution
