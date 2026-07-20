---
title: "[Solution] Extended Globbing Not Enabled"
description: "Enable and fix extended globbing (extglob) errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Extended Globbing Not Enabled

Extended globbing patterns like `+(pattern)` require `extglob` to be enabled.

### Common Causes
- `shopt -s extglob` not called.
- Using extended glob syntax in a non-interactive shell.

### How to Fix
```bash
# Enable extglob
shopt -s extglob

# Use extended patterns
shopt -s extglob
echo *.+(gz|bz2)    # match .gz and .bz2 files

# Disable extglob
shopt -u extglob

# Check status
shopt extglob
```

### Example
```bash
# Broken
echo *.+(log)    # extglob not enabled

# Fixed
shopt -s extglob
echo *.+(log)
```
