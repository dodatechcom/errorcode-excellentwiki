---
title: "[Solution] x509 certificate error"
description: "Fix kubectl x509 certificate error. Resolve TLS certificate verification failures when connecting to the API server."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## x509 Certificate Error

`Unable to connect to the server: x509: certificate is valid for <names>, not <current-name>`

This error occurs when the API server's TLS certificate does not match the hostname or IP address used to connect.

### Common Causes

- Connecting via IP address but certificate only has DNS names
- Connecting via wrong DNS name
- Certificate has expired
- Using a self-signed certificate without the correct CA

### How to Fix

Use the correct server URL from the certificate:
```bash
openssl s_client -connect <server>:6443 -showcerts </dev/null 2>/dev/null | openssl x509 -text | grep DNS
```

Update kubeconfig with the correct server address:
```bash
kubectl config set-cluster <cluster> --server=https://<correct-dns>:6443
```

### Examples

```bash
# Check certificate DNS names
openssl s_client -connect api.example.com:6443 -showcerts </dev/null 2>/dev/null | openssl x509 -text | grep "DNS:"
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})