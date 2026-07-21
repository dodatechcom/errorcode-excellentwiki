---
title: "Ubuntu eBPF Program Loading Error"
description: "eBPF programs fail to load or attach to kernel hooks"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu eBPF Program Loading Error

eBPF programs fail to load or attach to kernel hooks

## Common Causes

- Kernel does not support required eBPF features
- BTF (BPF Type Format) not enabled in kernel
- eBPF map creation failed due to memory limits
- Insufficient capabilities to load eBPF program

## How to Fix

1. Check eBPF: `bpftool feature probe`
2. Check kernel: `grep CONFIG_BPF /boot/config-$(uname -r)`
3. Enable BTF: `CONFIG_DEBUG_INFO_BTF=y` in kernel config
4. Check capabilities: `capsh --print | grep cap_bpf`

## Examples

```bash
# Check eBPF support
bpftool feature probe

# Check kernel eBPF config
grep CONFIG_BPF /boot/config-$(uname -r)

# List loaded eBPF programs
bpftool prog list
```
