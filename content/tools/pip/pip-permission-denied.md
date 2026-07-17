---
title: "[Solution] pip Permission Denied — Fix Access Errors Installing Packages"
description: "Fix pip permission denied errors when installing packages to system or protected directories. Learn to use virtual environments and avoid sudo pip installs."
tools: ["pip"]
error-types: ["permission-error"]
severities: ["error"]
weight: 5
---

This error means pip tried to write a package file to a directory where the current user does not have write access. The install fails partway through, leaving a broken partial install.

## What This Error Means

pip needs to write into `site-packages` and sometimes `bin/` to register a new package. If those directories are owned by root or another user, pip raises a `PermissionError`. The traceback usually ends with:

```
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied
```

## Why It Happens

- You ran `pip install` without a virtual environment and the system `site-packages` is root-owned
- A previous `sudo pip install` created root-owned files that normal pip cannot overwrite
- You are installing to a `--prefix` directory you do not own
- The `umask` is too restrictive and files were created unreadable
- A running process has a file lock on a package being replaced

## How to Fix It

### Use a Virtual Environment (Recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install <package>
```

### Use `--user` Flag

Install into your home directory instead of system-wide:

```bash
pip install --user <package>
```

### Fix Ownership of System Packages

If root-owned files are blocking normal installs:

```bash
sudo chown -R $(whoami) $(python3 -m site --user-site)
```

### Use `pipx` for CLI Tools

```bash
pipx install <package>
```

pipx installs each tool in an isolated environment and avoids permission conflicts entirely.

### Avoid `sudo pip install`

Running pip as root is almost never correct on a development machine. Remove any root-installed packages and reinstall with `--user`:

```bash
sudo pip uninstall <package>
pip install --user <package>
```

## Common Mistakes

- Using `sudo pip install` as a quick fix, which creates a permissions mess later
- Not activating a virtual environment before running pip
- Trying to install into `/usr/lib/python3/dist-packages` directly
- Running pip from a Dockerfile without a virtual environment

## Related Pages

- [pip Install Error]({{< relref "/tools/pip/pip-install-error" >}}) -- build environment failures
- [pip Virtualenv Error]({{< relref "/tools/pip/pip-virtualenv-error" >}}) -- virtualenv creation and activation errors
- [pip Cache Error]({{< relref "/tools/pip/pip-cache-error" >}}) -- cache corruption and permission issues
