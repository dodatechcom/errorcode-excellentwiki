---
title: "[Solution] macOS Music Error -- Apple Music Not Playing or Syncing"
description: "Fix macOS Music error when Apple Music fails to play songs or sync with your library. Resolve Music app issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Music Error -- Apple Music Not Playing or Syncing

The Music app on macOS handles Apple Music streaming and local music library management. Errors can include songs not playing, library sync failures, or the app crashing.

## Common Causes
- Apple Music subscription has expired
- Corrupted music library database
- DRM license cache is outdated
- Network connectivity issues preventing streaming
- Local music files have been moved or deleted

## How to Fix
1. Verify the Apple Music subscription is active
2. Rebuild the music library
3. Sign out of the iTunes Store and sign back in
4. Check network connectivity for streaming
5. Re-add music files that have been moved or deleted

```bash
# Check Music library
ls -la ~/Music/Music/

# View Music errors
log show --predicate 'process == "Music"' --last 10m
```

## Examples

```bash
# Check iTunes Store authorization
# Music > Account > Authorizations > Deauthorize This Computer
```

This error is common after an Apple Music subscription expires, when the library database is corrupted, or when DRM licenses need to be refreshed.
