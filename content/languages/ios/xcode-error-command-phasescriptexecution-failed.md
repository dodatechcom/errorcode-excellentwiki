---
title: "[Solution] Xcode Error: Command PhaseScriptExecution Failed"
description: "Resolve Xcode script phase execution failures during iOS app builds."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Command PhaseScriptExecution Failed

This error happens when a Run Script build phase fails during compilation. The script phase returns a non-zero exit code and halts the build process.

## Common Causes
- Script references missing files or directories
- Incorrect shell script paths or environment variables
- Missing dependencies required by the script
- Permissions issues on script files

## How to Fix
1. Check the build log for the exact script that failed
2. Verify all file paths referenced in the script exist
3. Ensure the script has executable permissions
4. Add error handling to your Run Script phases

```bash
#!/bin/bash
# Add this at the top of every Run Script phase
set -e

# Verify required tools exist
command -v swiftlint >/dev/null 2>&1 || { echo "swiftlint not installed"; exit 1; }

# Run with proper error handling
swiftlint lint --config .swiftlint.yml
```

## Examples
```bash
# Example: Fixing a failed script phase
# Before (failing):
/usr/libexec/PlistBuddy -c "Set :CFBundleShortVersionString 1.0" "${TARGET_BUILD_DIR}/${INFOPLIST_FILE}"

# After (with error handling):
if [ -f "${TARGET_BUILD_DIR}/${INFOPLIST_FILE}" ]; then
  /usr/libexec/PlistBuddy -c "Set :CFBundleShortVersionString 1.0" "${TARGET_BUILD_DIR}/${INFOPLIST_FILE}"
else
  echo "warning: Info.plist not found at expected path"
fi
```
