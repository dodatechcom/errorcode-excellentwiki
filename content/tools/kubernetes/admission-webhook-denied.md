---
title: "[Solution] Admission webhook denied the request"
description: "Fix Kubernetes admission webhook denial errors. Resolve resource creation failures rejected by admission webhooks."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Admission Webhook Denied

`admission webhook "<webhook>" denied the request: <reason>`

This error occurs when an admission webhook (ValidatingWebhookConfiguration or MutatingWebhookConfiguration) rejects a resource creation or update.

### Common Causes

- Webhook validation rules are not satisfied
- Mutating webhook modifies the resource in an invalid way
- Webhook endpoint is unreachable causing timeouts
- Multiple webhooks conflict with each other

### How to Fix

Check the webhook error message for details about what was rejected.

List webhooks:
```bash
kubectl get validatingwebhookconfigurations
kubectl get mutatingwebhookconfigurations
```

Check webhook service status:
```bash
kubectl get pods -n <webhook-namespace>
kubectl get service -n <webhook-namespace>
```

### Examples

```bash
# List admission webhooks
kubectl get validatingwebhookconfigurations
# my-webhook   ValidatingWebhookConfiguration

# Check webhook logs
kubectl logs -n webhook-ns deployment/webhook
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})