---
title: "[Solution] macOS Update Not Showing -- Software Update Missing New Version"
description: "Fix macOS update not showing in Software Update when new version is available but not appearing. Resolve missing Mac updates."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Update Not Showing -- Software Update Missing New Version

When Apple releases a new macOS version but it does not appear in your Software Update preferences, the issue is typically related to caching, configuration profiles, or eligibility checks.

## Common Causes
- Software Update catalog cache is stale and not refreshing
- A beta or developer profile is blocking stable updates
- MDM or configuration profile restricting available updates
- Mac model is not eligible for the target macOS version
- Apple server region has not yet rolled out the update

## How to Fix
1. Clear the Software Update cache and reload the catalog
2. Remove any beta or developer configuration profiles
3. Check that your Mac model supports the target macOS version
4. Use terminal to force a catalog refresh
5. Try the full installer from the App Store instead

```bash
# Clear and refresh the update catalog
sudo softwareupdate --clear-catalog
sudo softwareupdate --set-catalog https://swscan.apple.com/catalog/macOS/fullakt/installer_list.xml

# Check for available updates
softwareupdate -l
```

## Examples

```bash
# List installed configuration profiles
profiles -P

# Remove a specific beta profile
sudo profiles -r -i com.apple.SoftwareUpdate
```

This error commonly happens when a beta macOS profile was installed and is still active, when MDM restrictions from a work device block certain updates, or when a regional server has not yet propagated the update.
