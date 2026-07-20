---
title: "[Solution] MutatingWebhookConfiguration failed"
description: "Fix Kubernetes MutatingWebhookConfiguration failures. Resolve errors when a mutating admission webhook cannot process requests."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## MutatingWebhookConfiguration Failed

`Internal error occurred: failed calling webhook "<webhook>": Post "<url>": context deadline exceeded`

This error occurs when the API server cannot reach the mutating webhook service or the webhook takes too long to respond.

### Common Causes

- Webhook service is down or slow
- Webhook timeout too short (default 10s)
- Webhook is modifying resources in a way that triggers an infinite loop
- TLS certificate validation failure
- Webhook returns unexpected content type

### How to Fix

Check webhook configuration:
```bash
kubectl get mutatingwebhookconfiguration <name> -o yaml
```

Check the webhook service connectivity:
```bash
kubectl run test-$RANDOM --image=busybox -it --rm -- wget -O- https://webhook-service:443
```

Temporarily disable the webhook for debugging:
```bash
kubectl patch mutatingwebhookconfiguration <name> --type=json -p='[{"op": "replace", "path": "/webhooks/0/failurePolicy", "value": "Ignore"}]'
```

### Examples

```bash
# Check webhook failure policy
kubectl get mutatingwebhookconfiguration <name> -o yaml | grep failurePolicy
# FailurePolicy: Fail

# Change to Ignore for debugging
kubectl patch mutatingwebhookconfiguration <name> --type=json -p='[{"op": "replace", "path": "/webhooks/0/failurePolicy", "value": "Ignore"}]'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})