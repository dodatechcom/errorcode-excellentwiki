---
title: "[Solution] Webhook service not found"
description: "Fix Kubernetes webhook service not found errors. Resolve admission webhook failures when the backing service is missing."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Webhook Service Not Found

`failed calling webhook "<webhook>": Post "https://<service>.<namespace>.svc:443/<path>": dial tcp: lookup <service> on <dns>: no such host`

This error occurs when a ValidatingWebhookConfiguration or MutatingWebhookConfiguration references a service that does not exist.

### Common Causes

- Webhook service has not been deployed yet
- Service name in the webhook config is misspelled
- Webhook service is in a different namespace
- Webhook service was deleted but config remains
- Service port mismatch

### How to Fix

Check the webhook configuration for the service reference:
```bash
kubectl get validatingwebhookconfiguration <name> -o yaml
kubectl get mutatingwebhookconfiguration <name> -o yaml
```

Verify the service exists:
```bash
kubectl get svc -n <namespace>
kubectl describe svc <name> -n <namespace>
```

### Examples

```bash
# Find the referenced service
kubectl get validatingwebhookconfiguration <name> -o jsonpath='{.webhooks[0].clientConfig.service}'
# {"name":"webhook-service","namespace":"webhook-ns"}

# Verify service exists
kubectl get svc -n webhook-ns webhook-service
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})