---
title: "[Solution] Docker Exec Format Error — exec format error"
description: "Fix Docker exec format error. Resolve architecture mismatch and binary format issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

# exec format error

This error occurs when Docker tries to execute a binary that is compiled for a different CPU architecture. The binary format does not match the host system.

## Common Causes

- Binary compiled for wrong architecture (ARM vs AMD64)
- Running x86_64 binary on ARM system without emulation
- Corrupted binary or image layer
- Shell script with wrong shebang line
- Missing executable bit on binary

## How to Fix

### Check Your Architecture

```bash
uname -m
# x86_64 for AMD64
# aarch64 for ARM64
```

### Use Correct Platform Image

```bash
docker run --platform linux/amd64 my-image
```

### Enable QEMU Emulation

```bash
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```

### Check Binary Architecture

```bash
file ./my-binary
# ELF 64-bit LSB executable, x86-64
```

### Rebuild for Correct Platform

```bash
docker buildx build --platform linux/amd64 -t myimage .
```

## Examples

```bash
# Example 1: Architecture mismatch
docker run my-arm-image
# exec format error
# Fix: docker run --platform linux/arm64 my-arm-image

# Example 2: Check binary
file ./app
# ELF 64-bit LSB executable, ARM aarch64

# Example 3: Enable emulation
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
docker run my-cross-platform-image
```

## Related Errors

- [No matching manifest]({{< relref "/tools/docker/no-matching-manifest" >}}) — related error
- [Image not found]({{< relref "/tools/docker/image-not-found-manifest-unknown" >}}) — related error
