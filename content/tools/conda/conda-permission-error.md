---
title: "[Solution] Conda Permission Error — Fix Access Denied Installing Packages"
description: "Fix conda permission denied errors when installing or updating packages in shared environments. Fix ownership without using sudo conda install commands."
tools: ["conda"]
error-types: ["permission-error"]
severities: ["error"]
weight: 5
---

This error means conda cannot write to the environment directory or the package cache because the current user lacks the required file permissions.

## What This Error Means

conda needs to write extracted package files into the environment's `lib/`, `bin/`, and `share/` directories. If those directories are owned by a different user, conda raises:

```
PermissionError

[Errno 13] Permission denied: '/home/user/miniconda3/envs/myenv/lib/python3.11/site-packages/...'
```

Or:

```
CondaError

The target prefix is the base prefix. Aborting.
```

## Why It Happens

- The environment was created with `sudo conda create` and is now owned by root
- A shared `miniconda` installation is used by multiple users without proper group permissions
- Package cache files were created by root and normal users cannot overwrite them
- The filesystem mounted the conda directory as read-only
- A running process has a lock on a file conda needs to update

## How to Fix It

### Fix Ownership of Your Environment

```bash
sudo chown -R $(whoami) ~/miniconda3/envs/myenv
```

### Fix Ownership of the Entire Conda Installation

If you accidentally ran `sudo conda install`:

```bash
sudo chown -R $(whoami) ~/miniconda3
```

### Use `--user` Prefix Instead of Root

```bash
conda create --prefix ~/myenvs/project python=3.11
```

This creates the environment in a directory you own.

### Fix Package Cache Permissions

```bash
conda clean --all
sudo chown -R $(whoami) ~/miniconda3/pkgs
```

### Use a System-Wide Installation Correctly

For multi-user installations, set proper group permissions:

```bash
sudo groupadd conda-users
sudo usermod -aG conda-users $USER
sudo chown -R root:conda-users /opt/miniconda3
sudo chmod -R 775 /opt/miniconda3
```

### Avoid sudo Entirely

Never use `sudo conda install`. Always install conda as a normal user:

```bash
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
```

## Common Mistakes

- Running `sudo conda install` once, which changes ownership of shared directories
- Not noticing that package cache is root-owned until the next update fails
- Installing conda system-wide to `/opt` without setting group permissions
- Leaving `conda init` out of root's shell config, forcing manual sudo for activation

## Related Pages

- [Conda Environment Error]({{< relref "/tools/conda/conda-environment-error" >}}) -- environment issues
- [Conda Update Error]({{< relref "/tools/conda/conda-update-error" >}}) -- update failures
- [Conda Solver Error]({{< relref "/tools/conda/conda-solver-error" >}}) -- solver failures
