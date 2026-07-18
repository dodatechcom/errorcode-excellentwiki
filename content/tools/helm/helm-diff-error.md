---
title: "[Solution] Helm Diff Error — Fix helm diff Plugin Not Installed"
description: "Fix Helm diff errors when the helm-diff plugin is missing or fails to compare releases. Install the plugin and configure it for upgrade previews."
---

## What This Error Means

Helm diff errors occur when the helm-diff plugin is not installed, is outdated, or fails to generate a diff between releases. The diff plugin is commonly used in CI/CD to preview changes before applying them.

A typical error:

```
Error: unknown command "diff" for "helm"
Run 'helm --help' for usage.
```

Or:

```
Error: plugin "diff" exited with error
```

## Why It Happens

Diff plugin errors happen when:

- **Plugin not installed**: The helm-diff plugin has not been installed.
- **Plugin version mismatch**: The installed plugin version is incompatible with your Helm version.
- **Missing diff tool**: The plugin depends on `diff` being available on the system PATH.
- **Release does not exist**: Running diff on a release that has never been installed.
- **Insufficient permissions**: The plugin cannot query release history from the cluster.
- **Plugin binary corruption**: The plugin download was interrupted or corrupted.

## How to Fix It

**Step 1: Install the helm-diff plugin**

```bash
helm plugin install https://github.com/databus23/helm-diff
```

**Step 2: List installed plugins**

```bash
helm plugin list
```

**Step 3: Update the plugin**

```bash
helm plugin update diff
```

**Step 4: Use the diff command**

```bash
helm diff upgrade my-app ./chart --values values.yaml
```

**Step 5: Check diff requires a context**

For an initial release, use a dummy previous release:

```bash
helm diff upgrade my-app ./chart --dry-run
```

Or use `--install` to allow diff against nothing:

```bash
helm diff upgrade my-app ./chart --install
```

**Step 6: Verify diff is in PATH**

```bash
which diff
```

## Common Mistakes

- **Not installing the diff plugin before using `helm diff`**: The plugin is not bundled with Helm.
- **Running helm diff on a non-existent release**: Use `--install` flag for new releases.
- **Assuming helm diff works offline**: It queries the cluster for current release state.
- **Not updating the plugin after upgrading Helm**: Plugin versions must match Helm API versions.

## Related Pages

- [Helm Upgrade Failed](/tools/helm/helm-upgrade-failed/) -- Upgrade issues
- [Helm Release Failed](/tools/helm/helm-release-failed/) -- Release failures
- [Helm Template Error](/tools/helm/helm-template-error/) -- Template rendering issues
