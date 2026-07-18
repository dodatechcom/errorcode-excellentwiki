---
title: "[Solution] Brew Bottle Error — Fix Bottle Download Failed or Checksum Mismatch"
description: "Fix Homebrew bottle errors when a pre-built binary download fails or the checksum does not match. Resolve corrupted bottles and fall back to source builds."
tools: ["brew"]
error-types: ["bottle-error"]
severities: ["error"]
weight: 5
---

This error means Homebrew failed to download a pre-built bottle or the downloaded file has a checksum mismatch. Homebrew falls back to building from source when bottles are unavailable.

## What This Error Means

Homebrew distributes pre-compiled binaries called bottles. When bottle download fails:

```
Error: <formula>: bottle download failed
curl: (22) The requested URL returned error: 404
```

Or checksum mismatch:

```
Error: SHA256 mismatch
Expected: abc123...
Actual:   def456...
Archive: /Users/.../<formula--1.0.arm64_monterey.bottle.tar.gz>
```

## Why It Happens

- No bottle exists for your macOS version or architecture
- The bottle was removed from the server after a new release
- The download was corrupted during transfer
- A proxy or antivirus modified the downloaded file
- The bottle checksum in the formula definition was updated but the file was not
- Your Homebrew version is too old to use the latest bottle format

## How to Fix It

### Install from Source Instead

```bash
brew install --build-from-source <formula>
```

### Update Homebrew and Re-fetch

```bash
brew update
brew reinstall <formula>
```

### Clear the Bottle Cache

```bash
rm "$(brew --cache)/<formula>*.tar.gz"
brew fetch <formula>
```

### Force the Bottle Download

```bash
brew fetch --force-bottle <formula>
```

### Check Available Bottles for Your System

```bash
brew info <formula> | grep "bottle"
brew config | grep -E "(HOMEBREW_PREFIX|OS)"
```

### Use a Compatible Bottle Mirror

```bash
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles
brew fetch --force-bottle <formula>
```

### Build the Bottle Locally

```bash
brew install --build-bottle <formula>
```

## Common Mistakes

- Assuming bottles exist for all platforms (Apple Silicon bottles differ from Intel)
- Not running `brew update` before installing, which can point to stale bottle URLs
- Ignoring the specific SHA256 mismatch error and blindly re-downloading
- Using `--build-from-source` for all installs instead of debugging the bottle issue

## Related Pages

- [Brew Install Error]({{< relref "/tools/brew/brew-install-error" >}}) -- install failures
- [Brew Fetch Error]({{< relref "/tools/brew/brew-fetch-error" >}}) -- download failures
- [Brew Update Error]({{< relref "/tools/brew/brew-update-error" >}}) -- update problems
