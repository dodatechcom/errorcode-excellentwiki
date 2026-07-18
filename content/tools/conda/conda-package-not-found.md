---
title: "[Solution] Conda PackageNotFoundError - Fix Package Not Found in Channel"
description: "Fix conda PackageNotFoundError when a package cannot be found in any configured channel. Search alternatives and configure channels correctly."
tools: ["conda"]
error-types: ["package-not-found"]
severities: ["error"]
weight: 5
---

This error means conda searched all configured channels and could not find a package matching the name you specified. The package may not exist, may be named differently, or may not be available for your platform.

## What This Error Means

When you run `conda install <package>`, conda queries every channel in your configured list. If no channel provides the package, conda reports:

```
PackagesNotFoundError: The following packages are not available from current channels:
  - <package>
```

It may also suggest searching anaconda.org for similarly named packages. This is distinct from an `UnsatisfiableError`, which means the package exists but cannot be installed due to version conflicts.

## Why It Happens

- The package name is misspelled or uses a different naming convention on conda
- The package is only available on PyPI and not yet packaged for conda channels
- The package exists on a channel like `conda-forge` that is not in your configured channels
- The package does not support your current platform or architecture
- You specified a version that was never published to any channel
- A package was recently removed or renamed on the channel

## How to Fix It

### Search for the package on anaconda.org

```bash
anaconda search -t conda <package>
```

This shows all channels that provide the package and available versions.

### Add conda-forge channel

Many community packages are only on conda-forge:

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install <package>
```

### Use pip inside conda as a fallback

```bash
conda activate myenv
pip install <package>
```

This installs from PyPI when the package is not available through conda.

### Check available versions

```bash
conda search <package>
```

This lists all versions across your current channels. If the output is empty, the package is not in your channels.

### Verify the package name

Some packages have different names in conda. For example, `pillow` on PyPI is `pillow` on conda, but `scikit-learn` on PyPI is also `scikit-learn` on conda, while some others differ.

### Search PyPI directly

```bash
pip index versions <package>
```

If the package exists on PyPI but not conda, use pip as a fallback.

## Common Mistakes

- Not adding `conda-forge` as a channel before assuming the package does not exist
- Forgetting that some packages are pip-only and never packaged for conda
- Typo in package name or using a PyPI name that differs from the conda package name
- Pinning a version that was never published to any channel
- Running conda search without `conda-forge` and concluding the package is unavailable

## Related Pages

- [Conda Channel Error]({{< relref "/tools/conda/conda-channel-error" >}}) -- channel configuration problems
- [Conda Solver Error]({{< relref "/tools/conda/conda-solver-error" >}}) -- solver and dependency conflicts
- [Conda Pip Mix Error]({{< relref "/tools/conda/conda-pip-mix-error" >}}) -- mixing pip and conda
