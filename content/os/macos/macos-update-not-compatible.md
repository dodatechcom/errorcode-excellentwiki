---
title: "[Solution] macOS Update Not Compatible -- This Version of macOS Is Not Supported"
description: "Fix macOS update not compatible error when Mac says the update is not supported. Resolve incompatible macOS version messages."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Update Not Compatible -- This Version of macOS Is Not Supported

This error appears when macOS Software Update or the installer determines that your Mac hardware cannot run the target macOS version.

## Common Causes
- Mac model is too old for the target macOS version
- Insufficient RAM (minimum 4 GB for recent macOS versions)
- Storage controller not supported by the new OS
- Apple dropped support for your Mac in the target release
- A configuration profile is incorrectly reporting hardware information

## How to Fix
1. Verify your Mac model against Apple's compatibility list for the target macOS
2. Check About This Mac to confirm your model identifier
3. If your Mac is compatible but still shows the error, reset SMC and NVRAM
4. Update to the latest version of your current macOS first, then try again
5. Consider community tools for unsupported Macs

```bash
# Check your Mac model
system_profiler SPHardwareDataType | grep -i "Model\|Memory"

# Check current macOS version
sw_vers
```

## Examples

```bash
# List all Mac models and their maximum supported macOS
# macOS Sonoma supports: MacBook Air 2018+, MacBook Pro 2018+
# macOS Ventura supports: MacBook Air 2018+, MacBook Pro 2017+
```

This error is expected when Apple has dropped support for older Mac hardware, when trying to install an ARM-only macOS on an Intel Mac, or when a configuration profile is masking the actual hardware model.
