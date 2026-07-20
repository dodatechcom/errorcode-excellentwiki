---
title: "[Solution] cert-manager certificate issuance failed"
description: "Fix cert-manager certificate issuance failures in Kubernetes. Resolve TLS certificate provisioning errors."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## cert-manager Certificate Failed

`Certificate <name> failed: <error>`

This error occurs when cert-manager cannot issue a TLS certificate from the configured issuer.

### Common Causes

- ACME issuer cannot validate the domain (HTTP-01 or DNS-01)
- Ingress not configured for HTTP-01 challenge
- DNS provider credentials incorrect for DNS-01
- Certificate request exceeds rate limits (Let's Encrypt)

### How to Fix

Check certificate status:
```bash
kubectl describe certificate <name>
kubectl describe certificaterequest <name>
```

Check issuer:
```bash
kubectl describe issuer <name>
kubectl describe clusterissuer <name>
```

### Examples

```bash
# Check certificate
kubectl describe certificate my-cert
#  Reason: Failed
#  Message: Failed to complete ACME challenge

# Check challenges
kubectl get challenges
kubectl describe challenge my-cert-xxx
#  Type: dns-01
#  Status: pending
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})