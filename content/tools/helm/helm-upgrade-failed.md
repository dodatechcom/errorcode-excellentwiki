---
title: "[Solution] Helm Upgrade Failed — Fix Cannot Rollback"
description: "Fix Helm upgrade failed errors. Resolve rollback failures, release corruption, and version conflicts with step-by-step fixes."
---

## What This Error Means

The `upgrade failed, cannot rollback` error means Helm attempted to upgrade a release but the upgrade failed and Helm could not automatically roll back to the previous version.

A typical error:

```
Error: upgrade failed: Deployment.apps "my-app" is invalid: spec.selector:
Invalid value: "existing label does not match new selector values"
```

Or:

```
Error: cannot rollback, no history. Upgrade failed and rollback also failed
```

## Why It Happens

Upgrade failures occur when:

- **Immutable fields changed**: Some Kubernetes fields (spec.selector in Deployments) cannot be changed after creation.
- **RBAC restrictions**: The Helm service account lacks permissions for the upgrade.
- **Resource conflicts**: Another process modified resources between plan and apply.
- **Values validation failed**: New values do not pass chart validation checks.
- **Hook failures**: Pre-upgrade hooks failed, blocking the upgrade.
- **No previous release**: There is no release to rollback to (first install failed).

## How to Fix It

**Step 1: Check release history**

```bash
helm history my-release
```

**Step 2: Manually rollback to a specific revision**

```bash
helm rollback my-release 2
```

**Step 3: Uninstall and reinstall if rollback is impossible**

```bash
# Remove the release
helm uninstall my-release

# Delete stuck resources
kubectl delete deployment my-release -n default

# Reinstall
helm install my-release my-repo/my-chart --namespace default
```

**Step 4: Fix immutable field issues**

Do not change `spec.selector` in Deployments. Instead, create a new Deployment:

```yaml
# Delete old deployment first
kubectl delete deployment my-app

# Then upgrade with new selector
helm upgrade my-release my-repo/my-chart
```

**Step 5: Use --atomic for safe upgrades**

```bash
helm upgrade my-release my-repo/my-chart --atomic --timeout 600s
```

**Step 6: Force upgrade to override conflicts**

```bash
helm upgrade my-release my-repo/my-chart --force
```

## Common Mistakes

- **Changing immutable fields in upgrades**: Plan resource recreation if selector labels need to change.
- **Not using `--atomic` for critical upgrades**: Always use `--atomic` in production to ensure automatic rollback.
- **Forgetting to check history before rolling back**: Verify the correct revision number with `helm history`.
- **Not testing upgrades in staging first**: Always test `helm upgrade` in a non-production environment.

## Related Pages

- [Helm Release Failed](/tools/helm/helm-release-failed/) — Release installation failures
- [Helm Hooks Error](/tools/helm/helm-hooks-error/) — Hook execution issues
- [Terraform Plan Changed](/tools/terraform/terraform-plan-changed/) — Plan drift before apply
