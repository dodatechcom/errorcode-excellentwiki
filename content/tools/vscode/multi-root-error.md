---
title: "[Solution] VS Code Multi-root workspace error"
description: "Fix VS Code multi-root workspace errors. Resolve issues with managing multiple project folders in a single workspace."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "workspace", "multi-root", "folders"]
severity: "error"
---

# Multi-root workspace error

## Error Message

```
Multi-root workspace error: Folder '/project/api' cannot be added to the workspace. The path does not exist or is not accessible.
```

## Common Causes

- One of the workspace folders has been moved or deleted
- File system permissions prevent access to a workspace folder
- Workspace configuration file contains invalid folder entries
- Extension does not support multi-root workspace context

## Solutions

### Solution 1: Validate Workspace Folder Paths

Check that all workspace folders in your .code-workspace file exist and are accessible.

```
cat project.code-workspace | python -m json.tool
```

### Solution 2: Remove Invalid Workspace Folders

Remove non-existent or inaccessible folders from the workspace configuration.

```
code --command 'workbench.action.removeFolderFromWorkspace'
```

### Solution 3: Create Multi-Root Workspace File

Create a new .code-workspace file with only valid folder paths and shared settings.

```
{"folders": [{"path": "./frontend"}, {"path": "./backend"}], "settings": {"editor.formatOnSave": true, "files.exclude": {"**/node_modules": true}}}
```

## Prevention Tips

- Use .code-workspace files for complex multi-folder projects
- Configure per-folder settings when different projects need different configurations
- Keep shared extensions in the workspace settings for team consistency

## Related Errors

- [Unable to open workspace]({{< relref "/tools/vscode/workspace-error" >}})
- [Extension host crash]({{< relref "/tools/vscode/extension-host-crash" >}})
- [Git repository not found]({{< relref "/tools/vscode/git-integration-error" >}})
