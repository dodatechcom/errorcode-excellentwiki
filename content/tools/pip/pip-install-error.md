---
title: "[Solution] pip Install Failed — Fix Environment Error During Installation"
description: "Fix pip install failures caused by environment errors when building or installing packages. Troubleshoot missing compilers, headers, and system libraries."
tools: ["pip"]
error-types: ["install-error"]
severities: ["error"]
weight: 5
---

This error means pip could not install a package because the build environment or system configuration prevented compilation or file placement. The error typically mentions a failed build step or missing system tool.

## What This Error Means

When pip downloads a source distribution (sdist) instead of a wheel, it must build the package locally. The build can fail if the C compiler, Python headers, or other system libraries are missing. The error message usually contains lines like:

```
error: command 'gcc' failed or
Failed to build installable wheels for some pyproject.toml based projects
```

On Windows you may see `Microsoft Visual C++ 14.0 or greater is required` instead.

## Why It Happens

- The system is missing build essentials (`build-essential`, `python3-dev`)
- The package only ships a source distribution with no pre-built wheel
- A system library required by the C extension is not installed (e.g., `libffi-dev`, `libssl-dev`)
- The Python installation does not include development headers
- Disk space or memory ran out during compilation

## How to Fix It

### Install Build Tools on Debian/Ubuntu

```bash
sudo apt update
sudo apt install build-essential python3-dev libffi-dev libssl-dev
```

### Install Build Tools on macOS

```bash
xcode-select --install
brew install openssl
```

### Install Build Tools on Windows

Install the Visual Studio Build Tools with the C++ workload, or use:

```
pip install --upgrade pip setuptools wheel
```

### Try a Pre-built Wheel

Some packages provide wheels for specific platforms. Force pip to only use binary wheels:

```bash
pip install --only-binary=:all: <package-name>
```

### Use a Virtual Environment

A clean venv avoids system-wide permission issues:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install <package-name>
```

### Check Disk Space

```bash
df -h /tmp
```

If `/tmp` is full, pip cannot unpack build artifacts. Set a different temp dir:

```bash
export TMPDIR=/home/$USER/tmp
mkdir -p $TMPDIR
```

## Common Mistakes

- Assuming all packages ship wheels; many scientific libraries do not
- Skipping `python3-dev` on headless servers
- Running out of space in `/tmp` without checking
- Trying to install with `sudo pip install` instead of using a virtual environment

## Related Pages

- [pip Permission Denied]({{< relref "/tools/pip/pip-permission-denied" >}}) -- permission denied installing packages
- [pip Connection Error]({{< relref "/tools/pip/pip-connection-error" >}}) -- network issues during install
- [pip SSL Error]({{< relref "/tools/pip/pip-ssl-error" >}}) -- SSL certificate verification failed
