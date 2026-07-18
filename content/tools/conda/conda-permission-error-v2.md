---
title: "[Solution] Conda Permission Error v2 - Fix PermissionError in Conda Environments"
description: "Fix conda PermissionError when creating or modifying environments. Resolve file permission issues in shared and system-level conda installations."
tools: ["conda"]
error-types: ["permission-error"]
severities: ["error"]
weight: 5
---

This error means conda lacks the necessary file system permissions to read, write, or create files within an environment or the package cache. This is common on shared servers and multi-user systems.

## What This Error Means

When conda tries to create directories, extract packages, or modify environment files and lacks permission, you see:

```
PermissionError: [Errno 13] Permission denied: '/home/user/miniconda3/envs/myenv/...'
# or
CondaError: Cannot write to ...
```

This prevents environment creation, package installation, and cleanup operations. The error usually targets specific files or directories rather than all of conda.

## Why It Happens

- The conda installation is owned by root but you are running as a regular user
- Another user created an environment and the files are not world-writable
- A previous `sudo conda install` left root-owned files in the package cache
- Your home directory quota is full on a shared HPC system
- A file or directory has incorrect ownership from a manual copy
- conda is installed in a system directory like `/opt/conda` without user write access

## How to Fix It

### Install conda in your home directory

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
```

This ensures all files are owned by your user.

### Fix ownership after sudo installs

```bash
sudo chown -R $USER:$USER $HOME/miniconda3
```

This reclaims files that root created during a mistaken `sudo conda` run.

### Use --user flag or user-level config

```bash
conda config --set pkgs_dirs $HOME/.conda/pkgs
conda config --set envs_dirs $HOME/.conda/envs
```

This places packages and environments in your home directory.

### Fix shared environment permissions

```bash
chmod -R u+rwx /path/to/shared/env
```

Grant your user access to a shared environment if the admin permits it.

### Check disk quota

```bash
df -h $HOME
quota -s
```

If your quota is full, remove files or ask an administrator for an increase.

### Use a user-specific conda install inside containers

```bash
RUN useradd -m appuser
USER appuser
RUN wget ... && bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
```

Avoid installing conda as root in Docker images.

## Common Mistakes

- Running `sudo conda install` which creates root-owned files in your environment
- Installing conda system-wide without setting proper group permissions
- Ignoring quota warnings on shared computing clusters
- Manually copying environment directories instead of using `conda-pack`
- Not checking ownership after extracting a packed environment

## Related Pages

- [Conda Environment Error]({{< relref "/tools/conda/conda-environment-error" >}}) -- environment creation failures
- [Conda Activate Error]({{< relref "/tools/conda/conda-activate-error" >}}) -- activation problems
- [Conda Disk Space]({{< relref "/tools/conda/conda-disk-space" >}}) -- disk space exhaustion
