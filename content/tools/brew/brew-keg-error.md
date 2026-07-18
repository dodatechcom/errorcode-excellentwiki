---
title: "[Solution] Brew Keg Error — Fix Keg Not Linked or Already Linked"
description: "Fix Homebrew keg linking errors when a formula is installed but not linked, or another version is already linked. Resolve conflicts and force link correctly."
tools: ["brew"]
error-types: ["link-error"]
severities: ["error"]
weight: 5
---

This error means Homebrew cannot link a formula's keg into the main Cellar prefix because of conflicts with an existing installation or missing prerequisite files.

## What This Error Means

After installing a formula, Homebrew links the files from the versioned keg directory into `/usr/local/` (or `/opt/homebrew/`). When linking fails:

```
Error: The `brew link` step did not complete successfully
Error: Could not symlink bin/<binary>
Target /usr/local/bin/<binary> already exists. You may want to remove it.
```

Or:

```
Warning: <formula> is already installed, it's just not linked
You can `brew link <formula>` to link it
```

## Why It Happens

- A previous version of the formula is already linked, blocking the new version
- Another formula or external tool has a file with the same name in the target path
- The target directory is not writable by the current user
- Homebrew was installed as root and the prefix has wrong ownership
- The formula was installed but `brew link` was skipped or failed
- A manual install placed files in /usr/local/bin that conflict with brew links

## How to Fix It

### Try Force Linking

```bash
brew link --overwrite <formula>
```

### Unlink the Previous Version First

```bash
brew unlink <formula>
brew link <formula>
```

### Check What Files Are Blocking

```bash
brew link --dry-run <formula>
ls -la /usr/local/bin/<conflicting-file>
```

### Remove the Conflicting File Manually

```bash
mv /usr/local/bin/<conflicting-file> /usr/local/bin/<conflicting-file>.bak
brew link <formula>
```

### Fix Prefix Ownership

```bash
sudo chown -R $(whoami) /usr/local
brew link <formula>
```

### Use keg-only Formulae

Some formulae are keg-only and intentionally not linked. Use them by adding to PATH:

```bash
# Formula is keg-only
$(brew --prefix <formula>)/bin/<binary>
```

Or link explicitly with `--force`:

```bash
brew link --force <formula>
```

## Common Mistakes

- Running `brew link --overwrite` without checking what files will be overwritten
- Not understanding keg-only formulae that should not be linked
- Manually deleting files in /usr/local without checking if they belong to other formulae
- Ignoring the `brew link` step after a successful installation

## Related Pages

- [Brew Install Error]({{< relref "/tools/brew/brew-install-error" >}}) -- install failures
- [Brew Permission Error]({{< relref "/tools/brew/brew-permission-error" >}}) -- permission issues
- [Brew Dependency Error]({{< relref "/tools/brew/brew-dependency-error" >}}) -- dependency issues
