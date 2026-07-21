---
title: "[Solution] VS Code Extension Gallery Connection Error"
description: "Fix VS Code extension gallery connection errors when the marketplace server is unreachable or returns a connection failure."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Extension Gallery Connection Error

VS Code connects to the extension marketplace to search, install, and update extensions. A connection error means the editor cannot reach the marketplace server, which prevents all extension management operations.

## Common Causes

- Proxy settings are misconfigured or the proxy server is down
- Firewall rules block outbound connections to the marketplace domain
- Corporate network restricts access to external package registries
- DNS resolution fails for the marketplace host
- The `http.proxy` setting contains an invalid URL

## How to Fix

1. Verify network connectivity to the marketplace:

```bash
curl -I https://marketplace.visualstudio.com
```

2. Configure proxy settings in VS Code if behind a corporate network:

```json
{
  "http.proxy": "http://proxy.example.com:8080",
  "http.proxyStrictSSL": false
}
```

3. Bypass proxy for the marketplace host if direct access works:

```json
{
  "http.noProxy": "marketplace.visualstudio.com"
}
```

4. Check DNS resolution on your system:

```bash
nslookup marketplace.visualstudio.com
```

5. Clear VS Code server cache and retry:

```bash
rm -rf ~/.vscode/extensions/.obsolete
code --install-extension ms-vscode.cpptools
```

## Examples

```
# Error shown in VS Code
Error: connect ECONNREFUSED 13.107.42.18:443
    at TCPConnectWrap.afterConnect [as oncomplete]
```

```
# Proxy configuration fix
{
  "http.proxy": "http://corporate-proxy:3128",
  "http.proxyStrictSSL": true
}
```

## Related Errors

- [Extension Marketplace]({{< relref "/tools/vscode/extension-marketplace" >}}) -- marketplace UI errors
- [Proxy Setting]({{< relref "/tools/vscode/proxy-setting" >}}) -- proxy configuration issues
- [Offline Mode]({{< relref "/tools/vscode/offline-mode" >}}) -- working without network
