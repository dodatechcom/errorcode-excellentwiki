---
title: "[Solution] macOS Permission Error -- Operation Not Permitted on Mac"
description: "Fix macOS permission error when apps or operations show 'Operation not permitted.' Resolve file and folder permission issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Permission Error -- Operation Not Permitted on Mac

Permission errors on macOS prevent apps and users from accessing files, folders, or system resources. The 'Operation not permitted' message appears when the app lacks the necessary permissions.

## Common Causes
- App does not have Full Disk Access permission
- File or folder ownership is incorrect
- File permissions do not allow the app to read/write
- System Integrity Protection is blocking the operation
- TCC (Transparency, Consent, and Control) permissions not granted

## How to Fix
1. Grant the app Full Disk Access in System Preferences > Privacy & Security
2. Check and fix file ownership and permissions
3. Use terminal to grant necessary permissions
4. Check SIP status if the operation involves system files
5. Reset TCC permissions and re-grant them

```bash
# Check file permissions
ls -la /path/to/file

# Change file ownership
sudo chown $(whoami) /path/to/file

# Grant Full Disk Access via terminal (requires SIP disabled)
sudo tccutil reset SystemPolicyAllFiles
```

## Examples

```bash
# Check TCC permissions
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "SELECT client,service,auth_value FROM access;"
```

This error is common when apps lack Full Disk Access, when file ownership is incorrect after copying, or when TCC permissions have not been granted.
