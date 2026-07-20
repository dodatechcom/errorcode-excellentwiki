---
title: "[Solution] Jenkins Webhook Payload Invalid"
description: "Fix Jenkins webhook payload validation errors. Resolve webhook data format and processing issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Webhook Payload Invalid

Webhook payloads fail validation when the data format does not match what Jenkins expects.

## How to Fix

```bash
# Ensure Content-Type: application/json
echo '{"ref":"refs/heads/main"}' | python3 -m json.tool
```

Ensure webhook secret matches Jenkins configuration.
