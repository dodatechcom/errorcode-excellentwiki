---
title: "[Solution] Kubectl Webhook Error - Fix Webhook Admission Review Failed"
description: "Fix Kubernetes webhook admission review failures. Diagnose webhook timeouts, certificate issues, and service unavailability."
tools: ["kubectl"]
error-types: ["webhook-error"]
severities: ["error"]
weight: 5
---

This error means a Kubernetes admission webhook failed to process a request. The webhook server could not be reached, timed out, or returned an error response.

## What This Error Means

When you create, update, or delete a resource and an admission webhook fails, you see:

```
Error from server (InternalError): Internal error occurred:
failed calling webhook "webhook.example.com": ...
# or
admission webhook "validation.example.com" denied the request
# or
context deadline exceeded
```

Admission webhooks intercept API requests before objects are persisted. If the webhook service is down or misconfigured, all matching operations fail.

## Why It Happens

- The webhook service is down or not running
- The webhook's TLS certificate has expired
- The webhook endpoint is not reachable from the API server
- The webhook service is overloaded and timing out
- The MutatingWebhookConfiguration or ValidatingWebhookConfiguration has incorrect namespaceSelector rules
- DNS resolution for the webhook service fails inside the control plane

## How to Fix It

### Check webhook configuration

```bash
kubectl get mutatingwebhookconfigurations
kubectl get validatingwebhookconfigurations
```

Review the webhook configurations and their service references.

### Check webhook service status

```bash
kubectl get svc -n <webhook-namespace> <webhook-service>
kubectl get pods -n <webhook-namespace> -l app=<webhook>
```

Ensure the webhook pods and service are running and ready.

### Check webhook logs

```bash
kubectl logs -n <webhook-namespace> <webhook-pod>
```

Review logs for errors in webhook processing.

### Verify webhook TLS certificates

```bash
kubectl get secret -n <webhook-namespace> <webhook-cert-secret> -o jsonpath='{.data.ca\.crt}' | base64 -d
openssl x509 -in ca.crt -noout -dates
```

Expired certificates cause TLS handshake failures.

### Delete a misconfigured webhook temporarily

```bash
kubectl delete validatingwebhookconfigurations <webhook-name>
```

This removes the webhook temporarily to restore API functionality.

### Check webhook timeout settings

```yaml
webhooks:
  - name: webhook.example.com
    timeoutSeconds: 10
    failurePolicy: Fail
```

Increase `timeoutSeconds` if the webhook is slow, or set `failurePolicy: Ignore` to tolerate failures.

### Verify DNS resolution

```bash
kubectl run debug --image=busybox --rm -it -- nslookup <webhook-service>.<namespace>.svc
```

DNS must resolve correctly for the API server to reach the webhook.

## Common Mistakes

- Deploying a webhook without proper health checks, causing startup failures
- Not rotating TLS certificates before they expire
- Using `failurePolicy: Fail` without considering the impact of webhook outages
- Not testing webhooks in a staging environment before production
- Forgetting that the API server needs network access to the webhook service

## Related Pages

- [Kubectl Connection Refused]({{< relref "/tools/kubectl/kubectl-connection-refused" >}}) -- connectivity issues
- [Kubectl RBAC Error]({{< relref "/tools/kubectl/kubectl-rbac-error" >}}) -- access control
- [Kubectl Node Not Ready]({{< relref "/tools/kubectl/kubectl-node-not-ready" >}}) -- node health
