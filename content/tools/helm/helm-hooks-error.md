---
title: "[Solution] Helm Hooks Error — Fix Hook Execution Failed"
description: "Fix Helm hook execution failed errors. Resolve pre/post-install hooks, hook weights, and timeout issues with practical solutions."
---

## What This Error Means

Hook execution errors occur when Helm fails to run a hook resource during release operations. Helm hooks are Kubernetes resources annotated to run at specific points in the release lifecycle (pre-install, post-install, pre-upgrade, etc.).

A typical error:

```
Error: hook "pre-install" failed: timed out waiting for the condition
```

Or:

```
Error: release my-app failed: pre-install hooks failed: pods "my-app-pre-install"
is forbidden: exceeded quota
```

## Why It Happens

Hook errors occur when:

- **Hook resource fails to complete**: The hook pod or job fails, times out, or is never scheduled.
- **Hook timeout exceeded**: The hook takes longer than the configured timeout.
- **RBAC restrictions**: The hook resource lacks permissions to perform its operations.
- **Resource quota exceeded**: Cluster resource quotas prevent the hook from running.
- **Hook resource already exists**: A hook was not cleaned up from a previous release.
- **Incorrect hook annotations**: The hook annotation is misspelled or uses the wrong lifecycle phase.

## How to Fix It

**Step 1: Check hook annotations**

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: my-pre-install-job
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "0"
    "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
```

**Step 2: Increase hook timeout**

```bash
helm install my-app my-repo/my-chart --timeout 600s
```

Or in values:

```yaml
hooks:
  timeout: 600
```

**Step 3: Delete stuck hook resources**

```bash
kubectl get jobs --all-namespaces | grep pre-install
kubectl delete job my-app-pre-install -n default
```

**Step 4: Use hook-delete-policy properly**

```yaml
annotations:
  "helm.sh/hook": pre-install,pre-upgrade
  "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded,hook-failed
```

**Step 5: Debug hooks with dry run**

```bash
helm install my-app my-repo/my-chart --dry-run --debug
```

## Common Mistakes

- **Not specifying hook-delete-policy**: Hooks are not automatically deleted and can block future releases.
- **Using wrong hook weight**: Negative weights run first; higher weights run later. Order matters.
- **Setting timeout too low**: Complex hooks (migrations, backups) need longer timeouts.
- **Forgetting hooks run on every upgrade**: If the hook should only run on install, use only `pre-install`.

## Related Pages

- [Helm Release Failed](/tools/helm/helm-release-failed/) — Release installation failures
- [Helm Upgrade Failed](/tools/helm/helm-upgrade-failed/) — Upgrade and rollback issues
- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) — Task execution failures
