---
title: "[Solution] VS Code Git repository not found"
description: "Fix VS Code Git integration errors. Resolve issues with Git detection, source control, and repository operations."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "git", "source-control", "repository"]
severity: "error"
---

# Git repository not found

## Error Message

```
Git repository not found. Make sure you have Git installed and that the current folder is part of a Git repository. Error: fatal: not a git repository.
```

## Common Causes

- The workspace folder is not inside a Git repository
- Git is not installed or not found in the system PATH
- The .git directory is missing or corrupted
- VS Code workspace settings override Git location

## Solutions

### Solution 1: Initialize Git Repository

Initialize a new Git repository in the current workspace folder using the terminal.

```
git init && git add . && git commit -m 'Initial commit'
```

### Solution 2: Configure Git Path

Set the correct Git executable path in VS Code settings if Git is installed in a non-standard location.

```
{"git.path": "/usr/bin/git", "git.terminalIntegration": true}
```

### Solution 3: Clone and Open Repository

Clone the repository and open it directly in VS Code to ensure proper Git integration.

```
code --folder-uri vscode://file/path/to/repo --goto 'src/main.ts:1'
```

## Prevention Tips

- Ensure Git is installed and accessible from the terminal
- Use 'git status' in the terminal to verify repository state
- Keep the .gitignore file updated to exclude build artifacts

## Related Errors

- [Remote SSH error]({{< relref "/tools/vscode/remote-ssh-error" >}})
- [Extension host crash]({{< relref "/tools/vscode/extension-host-crash" >}})
- [Unable to open workspace]({{< relref "/tools/vscode/workspace-error" >}})
