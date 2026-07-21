---
title: "[Solution] GCP Function Invocation Error"
description: "GCFunctionInvocationError for invocation."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Function Invocation Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Function timed out (max 9 min for v1, 60 min for v2)
- Out of memory (> 2 GB v1)
- Code error (unhandled exception)

## How to Fix

### Invoke function

```bash
gcloud functions call myFunction
```

## Examples

- Example scenario: function timed out (max 9 min for v1, 60 min for v2)
- Example scenario: out of memory (> 2 gb v1)
- Example scenario: code error (unhandled exception)

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
