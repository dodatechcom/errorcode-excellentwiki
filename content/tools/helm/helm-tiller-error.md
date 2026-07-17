---
title: "[Solution] Helm Tiller Error — Fix Tiller Connection Refused"
description: "Fix Helm Tiller connection refused errors. Resolve Tiller installation, RBAC permissions, and Helm 2 to 3 migration issues."
---

## What This Error Means

The Tiller connection error is specific to Helm 2, where Tiller (the server-side component) runs inside the Kubernetes cluster. This error means kubectl/Helm cannot connect to the Tiller pod.

A typical error:

```
Error: could not find a ready tiller pod
```

Or:

```
Error: install: connection refused to Tiller server at 127.0.0.1:44134
```

**Note**: Helm 3 removed Tiller entirely. If you are using Helm 3, this error should not occur. Consider upgrading from Helm 2 to Helm 3.

## Why It Happens

Tiller errors occur when:

- **Tiller is not installed**: The `helm init` command was never run.
- **Tiller pod is not running**: The Tiller deployment was deleted or crashed.
- **RBAC permissions**: Tiller lacks the ClusterRole or ServiceAccount needed to manage resources.
- **Namespace mismatch**: Tiller is installed in a different namespace than the one being managed.
- **Helm version mismatch**: Client and server (Tiller) versions are incompatible.

## How to Fix It

**Step 1: Upgrade to Helm 3 (recommended)**

Helm 3 is the current stable version and does not require Tiller:

```bash
# Install Helm 3
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Migrate releases from Helm 2
helm 2to3 convert my-release
```

**Step 2: Install Tiller (Helm 2 only)**

```bash
helm init --service-account tiller --history-max 200
```

**Step 3: Configure Tiller RBAC (Helm 2 only)**

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tiller
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: tiller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: tiller
    namespace: kube-system
```

**Step 4: Verify Tiller is running**

```bash
kubectl get pods -n kube-system | grep tiller
```

**Step 5: Set Tiller namespace**

```bash
helm --tiller-namespace kube-system install my-app my-repo/my-chart
```

## Common Mistakes

- **Still using Helm 2**: Migrate to Helm 3 as soon as possible. Helm 2 is no longer maintained.
- **Not setting `--history-max`**: This prevents Tiller from accumulating too many release records.
- **Using cluster-admin for Tiller**: Create a dedicated service account with minimal permissions.
- **Forgetting namespace after installing Tiller in a custom namespace**: Always specify `--tiller-namespace` if not using default.

## Related Pages

- [Helm Release Failed](/tools/helm/helm-release-failed/) — Release installation failures
- [Kubectl Permission Error](/tools/kubectl/kubectl-permission-error/) — RBAC authorization errors
- [Terraform Provider Error](/tools/terraform/terraform-provider-error/) — Provider configuration issues
