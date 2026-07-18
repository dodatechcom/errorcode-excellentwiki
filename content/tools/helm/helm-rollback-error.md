---
title: "[Solution] Helm Rollback Error — Fix Rollback Failed / Revision Not Found"
description: "Fix Helm rollback errors when reverting a release fails. Resolve revision not found issues, missing release history, and failed rollback operations."
---

## What This Error Means

Helm rollback errors occur when reverting a release to a previous revision fails. Helm cannot find the requested revision or the rollback operation itself fails.

A typical error:

```
Error: release "my-app" not found
```

Or:

```
Error: rollback "my-app" failed: revision "2" not found
```

## Why It Happens

Rollback failures happen when:

- **Revision does not exist**: The requested revision number is out of range of available revisions.
- **Release not found**: The release name is incorrect or was already deleted.
- **Max history exceeded**: Helm's `--history-max` setting truncated old revisions.
- **Release in pending state**: The release is stuck in pending-install or pending-upgrade.
- **Storage backend unavailable**: Secrets or ConfigMaps storing release data are missing.
- **Current revision is the same as the target**: You are trying to roll back to the currently deployed revision.

## How to Fix It

**Step 1: List available revisions**

```bash
helm history my-app
```

**Step 2: Check the release status**

```bash
helm status my-app
```

**Step 3: Roll back to a specific revision**

```bash
helm rollback my-app 1
```

**Step 4: Roll back with wait**

```bash
helm rollback my-app 1 --wait --timeout 5m
```

**Step 5: Use --force for failing releases**

```bash
helm rollback my-app 1 --force
```

**Step 6: Increase history max to preserve revisions**

```bash
helm upgrade my-app ./chart --history-max 10
```

**Step 7: Check for deleted release secrets**

```bash
kubectl get secrets -l name=my-app,owner=helm
```

## Common Mistakes

- **Not checking available revisions with `helm history` before rolling back**: Always verify the revision exists.
- **Trying to roll back to the current revision**: Use a different revision number.
- **Not using `--force` for releases in FAILED state**: Failed releases require force to roll back.
- **Setting `--history-max` too low**: Old revisions are pruned and become unavailable for rollback.

## Related Pages

- [Helm Release Failed](/tools/helm/helm-release-failed/) -- Release installation failures
- [Helm Upgrade Failed](/tools/helm/helm-upgrade-failed/) -- Upgrade and rollback issues
- [Helm Values Error](/tools/helm/helm-values-error/) -- Values configuration issues
