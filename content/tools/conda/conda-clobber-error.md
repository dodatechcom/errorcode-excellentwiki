---
title: "[Solution] Conda ClobberError - Fix Files Already Exist During Install"
description: "Fix conda ClobberError when packages try to install files that already exist. Resolve file conflicts between packages and channels safely."
tools: ["conda"]
error-types: ["clobber-error"]
severities: ["error"]
weight: 5
---

This error means two different packages or channels are trying to install files to the same path within your environment. conda blocks this to prevent one package from silently overwriting another.

## What This Error Means

When a package attempts to install a file that already exists from a different package, conda reports:

```
ClobberError: The transaction includes operations which would overwrite
existing files. Cannot proceed.
```

Or:

```
ClobberError: Conda was asked to clobber an already existing path:
/path/to/file
```

This is a safety mechanism. conda will not overwrite files unless you explicitly allow it, because doing so could break the package that originally owned those files.

## Why It Happens

- You are mixing packages from `defaults` and `conda-forge` that both provide the same shared library
- A package was renamed but both old and new versions are being installed
- You are installing a package that conflicts with a system-installed library
- Channel priority is not set to strict, allowing conda to consider overlapping packages
- You are trying to downgrade a package while a newer version is installed and both provide the same files
- A package was rebuilt under a different name but provides identical files

## How to Fix It

### Set strict channel priority

```bash
conda config --set channel_priority strict
conda install <package>
```

This forces conda to prefer one channel consistently, avoiding file overlaps.

### Allow conda to overwrite with clobber flag

```bash
conda install <package> --clobber
```

Use this only when you are certain the overwrite is safe. Check which files will be overwritten first.

### Remove the conflicting package first

```bash
conda remove <conflicting-package>
conda install <package>
```

Remove the package that owns the conflicting files before installing the new one.

### Use only one channel

```bash
conda config --remove channels defaults
conda config --add channels conda-forge
conda install <package>
```

Sticking to one channel eliminates most clobber conflicts.

### Create a clean environment

```bash
conda create -n clean-env python=3.11 <package>
```

Fresh environments avoid conflicts from accumulated package installations.

### Check which package owns a file

```bash
conda list --show-channel-urls | grep <filename>
```

This identifies which channel provided the conflicting file.

## Common Mistakes

- Ignoring clobber errors and forcing installs that break existing packages
- Not setting `channel_priority strict` when mixing defaults and conda-forge
- Using `--clobber` routinely instead of resolving the root cause
- Assuming clobber errors are harmless because the files look similar
- Not checking which package owns a file before allowing an overwrite

## Related Pages

- [Conda Conflict Error]({{< relref "/tools/conda/conda-conflict-error" >}}) -- dependency conflicts
- [Conda Solver Error]({{< relref "/tools/conda/conda-solver-error" >}}) -- solver failures
- [Conda Channel Error]({{< relref "/tools/conda/conda-channel-error" >}}) -- channel configuration issues
