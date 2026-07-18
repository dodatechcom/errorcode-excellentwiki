---
title: "[Solution] pip Build Error — Fix subprocess-exited-with-error"
description: "Fix pip subprocess-exited-with-error during package builds. Resolve C extension compilation failures, missing build tools, and native library issues."
tools: ["pip"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

This error means pip's build backend exited with a non-zero status while compiling a package from source. The build process fails before pip can install the wheel into your environment.

## What This Error Means

When a package has no pre-built wheel for your platform, pip downloads the source distribution and invokes the build system (setuptools, poetry, flit, meson) to compile it. If compilation fails, you see:

```
ERROR: Command errored out with exit status 1:
  command: /usr/bin/python3 -c 'import setuptools...'
      cwd: /tmp/pip-install-xxx/package/
  Complete output (85 lines):
  building 'package' extension
  gcc: error: x86_64-linux-gnu-gcc: No such file or directory
  ----------------------------------------
ERROR: subprocess-exited-with-error
```

## Why It Happens

- Missing C compiler or build tools (gcc, g++, make, build-essential)
- Missing Python development headers (python3-dev / python3-devel)
- A native library dependency is not installed (libssl, libffi, libxml2)
- The package relies on Rust but rustc/cargo are not installed
- Outdated pip cannot build wheels from modern pyproject.toml-only packages

## How to Fix It

### Install Build Tools on Linux

```bash
sudo apt update
sudo apt install build-essential python3-dev
```

On RHEL/CentOS/Fedora:

```bash
sudo dnf groupinstall "Development Tools"
sudo dnf install python3-devel
```

### Install Native Library Dependencies

Check the error output for missing library names:

```bash
# Common libraries
sudo apt install libssl-dev libffi-dev libxml2-dev libxslt1-dev
```

### Install Rust for Rust-Based Packages

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
pip install <package>
```

### Upgrade pip and Build Tools

```bash
pip install --upgrade pip setuptools wheel
pip install <package>
```

### Install a Pre-Built Wheel Instead

Try a binary wheel from a third-party index:

```bash
pip install --only-binary=:all: <package>
```

If this fails, the package has no wheel for your platform.

### Use the Binary Alternative

Many packages have pre-compiled binary alternatives:

```bash
# Instead of building from source
pip install <package>-binary
# Or use conda
conda install <package>
```

## Common Mistakes

- Skipping the error output and not identifying which dependency is missing
- Upgrading pip but not setuptools or wheel
- Assuming all packages have wheels for every platform
- Not checking the build log for the actual compiler error

## Related Pages

- [pip Install Error]({{< relref "/tools/pip/pip-install-error" >}}) -- environment errors during install
- [pip Cache Error]({{< relref "/tools/pip/pip-cache-error" >}}) -- cache corruption issues
- [pip Wheel Error]({{< relref "/tools/pip/pip-wheel-error" >}}) -- wheel build failures
