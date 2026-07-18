---
title: "[Solution] Brew Fetch Error — Fix Formula Download Failed"
description: "Fix Homebrew fetch errors when downloading formula bottles or source tarballs fails. Resolve network issues, proxy configuration, and mirror selection problems."
tools: ["brew"]
error-types: ["fetch-error"]
severities: ["error"]
weight: 5
---

This error means Homebrew could not download a formula's bottle or source archive. The HTTP request to the download URL failed before the installation could proceed.

## What This Error Means

Homebrew downloads bottles from `ghcr.io` or source archives from the formula's homepage. When the download fails:

```
Error: Failed to download resource "<formula>"
Download failed: https://ghcr.io/v2/homebrew/core/<formula>/blobs/sha256:...
```

Or:

```
Error: DownloadError: Failed to download resource
curl: (7) Failed to connect to ghcr.io port 443: Connection refused
```

## Why It Happens

- Your network or firewall blocks access to GitHub Container Registry (ghcr.io)
- A corporate proxy intercepts and blocks the download
- The bottle was removed or is not available for your macOS version
- DNS cannot resolve ghcr.io or the formula's source URL
- The download times out due to a slow connection
- The formula URL changed and the formula definition is stale

## How to Fix It

### Check Connectivity to the Download Host

```bash
curl -I https://ghcr.io
curl -I https://github.com  # many formulae source from GitHub
```

### Update Homebrew and the Formula

```bash
brew update
brew upgrade <formula>
brew fetch <formula>
```

### Configure a Proxy

```bash
export ALL_PROXY=http://proxy-server:8080
brew fetch <formula>
```

### Use a Mirror

```bash
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles
brew fetch <formula>
```

Other mirrors:

```bash
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles
```

### Clear Download Cache

```bash
rm -rf "$(brew --cache)"
brew fetch <formula>
```

### Download Manually and Place in Cache

```bash
brew --cache <formula>
# Download the file to that path manually
curl -L -o "$(brew --cache <formula>)" <url>
```

## Common Mistakes

- Not updating Homebrew before fetching, causing expired URL errors
- Forgetting to set HTTPS proxy when HTTP_PROXY is configured but HTTPS_PROXY is not
- Using an outdated HOMEBREW_BOTTLE_DOMAIN mirror that no longer exists
- Not checking whether ghcr.io is accessible from your network

## Related Pages

- [Brew Install Error]({{< relref "/tools/brew/brew-install-error" >}}) -- install failures
- [Brew Update Error]({{< relref "/tools/brew/brew-update-error" >}}) -- update problems
- [Brew Cask Error]({{< relref "/tools/brew/brew-cask-error" >}}) -- cask issues
