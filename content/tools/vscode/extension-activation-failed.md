---
title: "[Solution] VS Code Extension activation failed"
description: "Fix VS Code extension activation failures. Resolve activation errors for extensions that fail to initialize properly."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "extensions", "activation", "modules"]
severity: "error"
---

# Extension activation failed

## Error Message

```
Extension activation failed: Cannot find module '@babel/core'. Extension: ms-python.python. Error: Module not found.
```

## Common Causes

- Missing or corrupted Node.js modules required by the extension
- Extension dependencies are not installed in the extension directory
- Version incompatibility between the extension and VS Code API
- Corrupted extension installation or incomplete download

## Solutions

### Solution 1: Reinstall the Extension

Uninstall the failing extension completely, then reinstall it from the marketplace. This ensures all dependencies are properly downloaded.

```
code --uninstall-extension ms-python.python && code --install-extension ms-python.python
```

### Solution 2: Install Extension Dependencies

Navigate to the extension directory and install its dependencies manually using npm.

```
cd ~/.vscode/extensions/ms-python.python-* && npm install
```

### Solution 3: Check Extension Logs

Enable verbose logging to see the exact activation error. Review the Output panel for the Extensions channel.

```
code --logtrace --log=trace
```

## Prevention Tips

- Check the extension's marketplace page for known compatibility issues
- Verify your Node.js version matches the extension's requirements
- Use the Extensions view to check extension health status

## Related Errors

- [Extension host crash]({{< relref "/tools/vscode/extension-host-crash" >}})
- [Extension API error]({{< relref "/tools/vscode/extension-api-error" >}})
- [TypeScript language service error]({{< relref "/tools/vscode/typescript-error" >}})
