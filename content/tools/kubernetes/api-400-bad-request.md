---
title: "[Solution] API 400 Bad Request"
description: "Fix Kubernetes API 400 Bad Request errors. Resolve malformed request failures when interacting with the API server."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## API 400 Bad Request

This HTTP status code occurs when the API server receives a malformed or invalid request.

### Common Causes

- Invalid JSON or YAML body
- Request body too large
- Missing required headers
- Invalid query parameters
- Malformed URL path
- Request timeout

### How to Fix

Check the request body format. Use `--dry-run=server` for validation:
```bash
kubectl apply -f manifest.yaml --dry-run=server
```

Check for special characters or encoding issues in the request.

For curl requests, ensure proper Content-Type header:
```bash
curl -X POST -H "Content-Type: application/json" -d @body.json https://api-server:6443/api/v1/namespaces
```

### Examples

```bash
# Validate manifest
kubectl apply -f deployment.yaml --dry-run=server --validate=true

# Check for encoding issues
file deployment.yaml
# Ensure it's UTF-8 encoded
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})