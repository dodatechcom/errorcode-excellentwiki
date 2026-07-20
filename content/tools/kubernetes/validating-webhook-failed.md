---
title: "[Solution] ValidatingWebhookConfiguration failed"
description: "Fix Kubernetes ValidatingWebhookConfiguration failures. Resolve errors when a validating admission webhook cannot process requests."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## ValidatingWebhookConfiguration Failed

`Internal error occurred: failed calling webhook "<webhook>": Post "<url>": dial tcp: lookup <service>: i/o timeout`

This error occurs when the API server cannot reach the validating webhook service.

### Common Causes

- Webhook service is not running
- Webhook service endpoint is misconfigured
- Network policy blocking traffic
- TLS certificate error
- Webhook service is in a different namespace
- Webhook timeout (default 10s) too short

### How to Fix

Check webhook configuration:
```bash
kubectl get validatingwebhookconfiguration <name> -o yaml
```

Verify the webhook service exists:
```bash
kubectl get service -n <namespace>
kubectl get endpoints -n <namespace>
```

Check the webhook pod logs:
```bash
kubectl logs -n <namespace> deployment/<webhook-name>
```

### Examples

```bash
# Check webhook service endpoints
kubectl get endpoints -n webhook-ns webhook-service
# No endpoints

# Restart webhook deployment
kubectl rollout restart -n webhook-ns deployment/webhook
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})