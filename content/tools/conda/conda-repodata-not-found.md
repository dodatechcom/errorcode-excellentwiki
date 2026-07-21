---
title: "[Solution] Conda Repodata Not Found -- Fix Missing Channel Metadata"
description: "Fix conda repodata not found errors when channel metadata files are missing. Refresh channel indices."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda cannot find the `repodata.json` metadata file for a configured channel. The channel index is unavailable.

## Common Causes

- The channel URL is incorrect
- The channel is down or has been moved
- The cache has stale metadata pointing to a removed channel
- Network issues prevent fetching metadata

## How to Fix

### 1. Update Channel Index

```bash
conda update conda
conda clean --index-cache
```

### 2. Check Channel URL

```bash
conda config --show channels
curl -I https://repo.anaconda.com/pkgs/main
```

### 3. Remove Stale Channel

```bash
conda config --remove channels stale-channel
```

### 4. Add Correct Channel

```bash
conda config --add channels conda-forge
```

## Examples

```bash
$ conda install numpy
ChannelNotValidError: repodata.json not found for channel

$ conda config --show channels
channels:
  - https://old-mirror.example.com/pkgs/main

$ conda config --remove channels https://old-mirror.example.com/pkgs/main
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
```
