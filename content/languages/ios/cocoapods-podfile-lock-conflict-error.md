---
title: "[Solution] CocoaPods Podfile.lock Conflict Error"
description: "Fix CocoaPods Podfile.lock merge conflicts when working with version control."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# CocoaPods Podfile.lock Conflict Error

Podfile.lock merge conflicts occur when multiple developers modify dependencies simultaneously, causing Git merge conflicts in the lock file.

## Common Causes
- Multiple developers adding different pods simultaneously
- Merge conflict markers left in Podfile.lock
- Podfile.lock not committed before switching branches
- Resolving conflict incorrectly causing version mismatches

## How to Fix
1. Accept one version of Podfile.lock
2. Run pod install to regenerate from Podfile
3. Commit the regenerated Podfile.lock
4. Ensure team coordinates pod additions

```bash
# Fix merge conflict:
# 1. Accept incoming changes or current branch version
# 2. Then run:
$ pod install
# This regenerates Podfile.lock based on your Podfile
# 3. Commit the regenerated Podfile.lock
```

## Examples
```bash
# Preventive measures:
# .gitattributes for Podfile.lock:
# Podfile.lock merge=union

# Or add to .gitignore and regenerate:
# .gitignore:
# Podfile.lock

# Team workflow:
# Always run pod install after pulling changes
$ git pull
$ pod install
```
