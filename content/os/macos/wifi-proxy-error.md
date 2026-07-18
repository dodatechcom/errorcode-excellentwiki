---
title: "[Solution] macOS WiFi Proxy Error — Proxy Settings Blocking Internet"
description: "Fix macOS WiFi proxy error: proxy settings blocking internet, WiFi works without proxy but not with proxy enabled."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 164
---

# WiFi Proxy Error — Proxy Settings Blocking Internet

Fix macOS WiFi proxy error: proxy settings blocking internet, WiFi works without proxy but not with proxy enabled.

## Common Causes

- Proxy server configured but no longer available
- Proxy authentication credentials expired or incorrect
- System proxy settings conflicting with VPN configuration
- Proxy configuration corrupted after macOS update

## How to Fix

### 1. Check and Disable Proxy Settings

```bash
networksetup -getwebproxy Wi-Fi
networksetup -getsecurewebproxy Wi-Fi
networksetup -setwebproxystate Wi-Fi off
networksetup -setsecurewebproxystate Wi-Fi off
```

### 2. Verify Proxy Configuration

```bash
# System Settings → Network → WiFi → Details → Proxies → Review settings
```

### 3. Clear Proxy Settings Completely

```bash
sudo networksetup -setwebproxystate Wi-Fi off
sudo networksetup -setsecurewebproxystate Wi-Fi off
sudo networksetup -setsocksfirewallproxystate Wi-Fi off
```

### 4. Test Without Proxy

```bash
# Disable all proxy settings temporarily
# Test internet connection without proxy
# If internet works, proxy settings were the issue
```

## Common Scenarios

This error commonly occurs when:

- Internet works when proxy is disabled but fails when enabled
- Proxy settings keep reappearing after being disabled
- Cannot authenticate with proxy server credentials
- Proxy blocks specific websites or services

## Prevent It

- Review proxy settings after macOS updates for unwanted changes
- Keep proxy server credentials updated and current
- Disable proxy settings when not required for network access
- Test internet connectivity with and without proxy to isolate issues
