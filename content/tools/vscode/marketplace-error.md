---
title: "[Solution] VS Code Unable to install extension"
description: "Fix VS Code Marketplace errors. Resolve issues when extensions fail to download or install from the marketplace."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "marketplace", "install", "network"]
severity: "error"
---

# Unable to install extension

## Error Message

```
Unable to install extension 'ms-python.python'. Marketplace request failed with status 403. Check your network connection and proxy settings.
```

## Common Causes

- Network proxy or firewall is blocking Marketplace access
- Marketplace service is temporarily unavailable or rate-limited
- Insufficient disk space to download and extract the extension
- Corporate network requires custom proxy authentication

## Solutions

### Solution 1: Configure HTTP Proxy Settings

Set the HTTP proxy in VS Code settings to allow connections through corporate networks.

```
{"http.proxy": "http://proxy.example.com:8080", "http.proxyStrictSSL": false, "http.proxyAuthorization": null}
```

### Solution 2: Install Extension from VSIX File

Download the extension VSIX file manually and install it directly from the file system.

```
code --install-extension /path/to/extension.vsix
```

### Solution 3: Clear Marketplace Cache

Remove cached marketplace data to force a fresh download of extension metadata.

```
rm -rf ~/.vscode/extensions/.obsolete && rm -rf ~/.vscode/CachedExtensionVSIXs/
```

## Prevention Tips

- Check the VS Code Marketplace status page for service outages
- Use the Extensions view to retry failed installations
- Download extensions from the marketplace website as a fallback

## Related Errors

- [Extension activation failed]({{< relref "/tools/vscode/extension-activation-failed" >}})
- [Failed to connect to remote host]({{< relref "/tools/vscode/remote-ssh-error" >}})
- [Settings Sync error]({{< relref "/tools/vscode/settings-sync-error" >}})
