---
title: "[Solution] VS Code VS Code is consuming high CPU"
description: "Fix VS Code high CPU usage. Identify and resolve processes causing excessive CPU consumption in the editor."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "performance", "cpu", "optimization"]
severity: "error"
---

# VS Code is consuming high CPU

## Error Message

```
VS Code process (PID 12345) is using 98% CPU. The TypeScript language service is consuming excessive resources. Consider restarting the language server.
```

## Common Causes

- TypeScript language server processing a large codebase without proper exclusions
- Extension running expensive background operations
- File watcher monitoring too many files or directories
- Syntax highlighting or extension scanning large generated files

## Solutions

### Solution 1: Exclude Large Directories from Watching

Configure file watchers to ignore large directories like node_modules, dist, and build output.

```
{"files.watcherExclude": {"**/node_modules/**": true, "**/dist/**": true, "**/build/**": true, "**/.git/objects/**": true}}
```

### Solution 2: Disable Unnecessary Extensions

Use the extension bisect tool to identify CPU-heavy extensions and disable them.

```
code --command 'extension bisect.start'
```

### Solution 3: Enable GPU Acceleration

Switch to hardware-accelerated rendering to offload work from the CPU to the GPU.

```
{"window.gpuAcceleration": "on", "editor.renderWhitespace": "none", "editor.minimap.enabled": false}
```

## Prevention Tips

- Monitor CPU usage through the VS Code process explorer
- Disable unused extensions to reduce background activity
- Increase the file watcher polling interval for large projects

## Related Errors

- [Memory error]({{< relref "/tools/vscode/memory-error" >}})
- [LSP crash]({{< relref "/tools/vscode/lsp-crash" >}})
- [Terminal process failed to launch]({{< relref "/tools/vscode/terminal-error" >}})
