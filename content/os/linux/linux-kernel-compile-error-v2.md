---
title: "[Solution] Linux Kernel Compilation Error — Missing Headers"
description: "Fix Linux kernel compilation errors caused by missing headers. Resolve build failures, install kernel headers, and fix Makefile errors."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kernel", "compile", "headers", "build", "make", "gcc"]
weight: 5
---

# Linux: Kernel — compilation error — missing headers

The kernel compilation error `fatal error: xxx.h: No such file or directory` or `Cannot find <header>` means the kernel build process cannot locate required header files. These headers come from the kernel source tree, installed kernel headers packages, or external dependencies.

## What This Error Means

The Linux kernel build system (`make`) compiles C source files that reference headers via `#include` directives. When the kernel source tree is incomplete, the `headers_install` step was not run, or system-level headers (like `libelf`, `openssl`, `bpf`) are missing, the compiler cannot find the required `.h` files and aborts.

## Common Causes

- Kernel source tree incomplete or partially extracted
- Missing `make modules_prepare` step before building modules
- System development headers not installed (`linux-headers`, `libelf-dev`, etc.)
- Out-of-tree module referencing wrong kernel headers version
- Config changed requiring headers not previously needed
- Cross-compilation with wrong architecture headers

## How to Fix

### 1. Install Required Development Headers

```bash
# Debian/Ubuntu
sudo apt install build-essential linux-headers-$(uname -r)
sudo apt install libelf-dev libssl-dev lib ncurses-dev flex bison bc

# RHEL/CentOS/Fedora
sudo dnf groupinstall 'Development Tools'
sudo dnf install kernel-devel-$(uname -r) kernel-headers-$(uname -r)
sudo dnf install elfutils-libelf-devel openssl-devel ncurses-devel
```

### 2. Run modules_prepare

```bash
# In the kernel source directory
cd /usr/src/linux-$(uname -r)

# Prepare the source tree for module building
sudo make modules_prepare

# This runs necessary header generation steps
```

### 3. Verify Kernel Source Integrity

```bash
# Check that include/ directory exists
ls /usr/src/linux-$(uname -r)/include/linux/

# If headers are missing, re-extract the source
cd /usr/src
sudo tar xf /usr/src/linux-source-$(uname -r).tar.xz
cd linux-source-$(uname -r)
sudo make headers_install
```

### 4. Fix Out-of-Tree Module Headers

```bash
# Check the Makefile of the out-of-tree module
cat /path/to/module/Makefile | grep KVER

# Point to correct kernel source
export KVER=$(uname -r)
export KSRC=/usr/src/linux-headers-$KVER

# Or create a symlink
sudo ln -s /usr/src/linux-headers-$(uname -r) /lib/modules/$(uname -r)/build
```

### 5. Fix Specific Header Errors

```bash
# 'linux/config.h' not found (older kernels)
# Use 'autoconf.h' instead or run:
make olddefconfig

# 'generated/autoconf.h' not found
make prepare

# 'scripts/mod/modpost' not found
make scripts

# 'asm' not found — architecture headers missing
sudo apt install gcc-multilib
```

### 6. Clean and Rebuild

```bash
# Full clean
make mrproper

# Start fresh
make defconfig
make olddefconfig
make -j$(nproc)
```

## Examples

```bash
$ make -j$(nproc)
  CC      scripts/mod/empty.o
scripts/mod/empty.c:1:10: fatal error: linux/compiler_types.h: No such file or directory
    1 | #include <linux/compiler_types.h>
make[1]: *** [scripts/Makefile.build:310: scripts/mod/empty.o] Error 2

$ ls /usr/src/linux-$(uname -r)/include/linux/compiler_types.h
ls: cannot access: No such file or directory

$ sudo make headers_install INSTALL_HDR_PATH=/usr
$ make -j$(nproc)
# Compilation proceeds successfully
```

## Related Errors

- [Kernel compile error]({{< relref "/os/linux/linux-kernel-compile-error" >}}) — General kernel build failures
- [Kernel module error]({{< relref "/os/linux/linux-kernel-module" >}}) — Module loading failures
- [Kernel panic]({{< relref "/os/linux/linux-kernel-panic" >}}) — Kernel runtime crashes
