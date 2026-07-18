---
title: "[Solution] Conda-Forge Channel Not Found Error — How to Fix"
description: "Fix conda-forge channel not found errors. Add conda-forge to your channels, resolve channel priority issues, and access missing packages."
tools: ["conda"]
error-types: ["forge-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means conda cannot find the conda-forge channel or a specific package within it. The channel may not be configured, its repodata cache may be stale, or channel priority settings may be blocking access.

## Why It Happens

- conda-forge is not added to your channel list in `.condarc`
- The conda-forge repodata cache is stale and does not reflect available packages
- Channel priority is set to `strict` and conda-forge is listed after `defaults`
- Network issues prevent conda from fetching conda-forge repodata
- The package you are looking for was never published to conda-forge
- SSL errors block the connection to conda-forge servers

## Common Error Messages

```
PackagesNotFoundError: The following packages are not available from
current channels:
  - package-name
```

```
ResolvePackageNotFound:
  - package-name
```

```
ChannelNotValid: The channel 'conda-forge' is not valid.
```

```
CondaHTTPError: HTTP 000 CONNECTION FAILED for url
<https://conda.anaconda.org/conda-forge/linux-64/repodata.json>
```

## How to Fix It

### 1. Add conda-forge to Your Channels

```bash
conda config --add channels conda-forge
```

Verify it was added:

```bash
conda config --show channels
```

The output should show `conda-forge` before `defaults`.

### 2. Set Channel Priority to Strict

```bash
conda config --set channel_priority strict
```

This prevents conda from mixing packages across channels and ensures conda-forge is preferred when available.

### 3. Clean and Refresh Repodata

```bash
conda clean --all
conda search -c conda-forge package-name
```

This forces conda to re-download repodata from conda-forge.

### 4. Search for the Package on conda-forge

```bash
conda search -c conda-forge package-name
```

If the package is not found, check [anaconda.org](https://anaconda.org/conda-forge/package-name) directly.

### 5. Install Directly from conda-forge

```bash
conda install -c conda-forge package-name
```

### 6. Configure Your .condarc Permanently

Edit `~/.condarc` to ensure conda-forge is always available:

```yaml
channels:
  - conda-forge
  - defaults

channel_priority: strict
```

### 7. Fix Network Issues with conda-forge

```bash
# Test connection to conda-forge
curl -I https://conda.anaconda.org/conda-forge/linux-64/repodata.json

# If blocked, configure proxy
conda config --set proxy_servers.https http://proxy:8080
```

## Common Scenarios

**Package exists on PyPI but not in conda-forge.** Some packages are only available via pip. Install with pip inside the conda environment as a last resort:

```bash
conda activate myenv
pip install package-name
```

**conda-forge and defaults conflict.** Packages from different channels may have incompatible versions. Use strict channel priority to avoid mixing:

```bash
conda config --set channel_priority strict
conda config --remove channels defaults  # use only conda-forge
```

**Repodata is stale after a new package release.** conda caches repodata for several hours. Force a refresh:

```bash
conda clean -i
conda install -c conda-forge package-name
```

## Prevent It

1. Always add conda-forge as your primary channel with strict priority: `conda config --add channels conda-forge && conda config --set channel_priority strict`
2. Run `conda clean --all` periodically to ensure repodata stays current
3. Prefer conda-forge over defaults for scientific packages — conda-forge has faster updates and better maintained builds
