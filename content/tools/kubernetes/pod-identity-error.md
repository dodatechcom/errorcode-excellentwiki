---
title: "[Solution] Pod identity / workload identity error"
description: "Fix Kubernetes pod identity and workload identity errors. Resolve authentication failures when pods need to access cloud resources."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Pod Identity / Workload Identity Error

`Failed to get credentials: AccessDenied`

This error occurs when a pod configured with workload identity (IAM roles for service accounts, GCP workload identity, Azure AD pod identity) cannot obtain credentials for cloud resource access.

### Common Causes

- IAM role / service account annotation is missing or incorrect
- OIDC provider is not configured for the cluster
- Trust relationship between cloud IAM and K8s SA is misconfigured
- Service account exists but annotation is missing
- GKE workload identity: K8s SA to GCP SA binding missing

### How to Fix

For AWS EKS IRSA:
```bash
kubectl annotate serviceaccount <sa> eks.amazonaws.com/role-arn=arn:aws:iam::<account>:role/<role>
```

For GKE Workload Identity:
```bash
kubectl annotate serviceaccount <sa> iam.gke.io/gcp-service-account=<gcp-sa>@<project>.iam.gserviceaccount.com
```

For Azure AD Pod Identity:
```bash
kubectl label serviceaccount <sa> aadpodidbinding=<identity-name>
```

### Examples

```bash
# EKS - associate IAM role with service account
kubectl annotate serviceaccount my-sa eks.amazonaws.com/role-arn=arn:aws:iam::123456789:role/my-app-role

# Verify the trust policy
aws iam get-role --role-name my-app-role | jq '.Role.AssumeRolePolicyDocument'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})