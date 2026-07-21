---
title: "[Solution] VS Code Workspace Edit Apply Error"
description: "Fix VS Code workspace edit apply errors when refactoring operations fail to apply changes across multiple files."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Workspace Edit Apply Error

A workspace edit applies changes across multiple files simultaneously, commonly used during refactoring operations like rename symbol, move file, or organize imports. When the apply step fails, the files may end up in a partially modified state.

## Common Causes

- One or more target files have been deleted or moved since the edit was prepared
- File permissions prevent writing to the target location
- A file is open in another process with an exclusive lock
- The workspace folder is not writable
- An extension provided invalid edit ranges that do not match the current file content

## How to Fix

1. Check that all files referenced in the edit still exist:

```bash
ls -la path/to/affected/file.ts
```

2. Verify write permissions on the workspace folder:

```bash
chmod -R u+w /path/to/workspace/
```

3. Close the file in other editors or processes that may hold a lock:

```bash
lsof +D /path/to/workspace/src/
```

4. Use the undo command (Ctrl+Z) to revert partial changes if the edit applied to some files:

```
# In VS Code, press Ctrl+Z or Cmd+Z to undo the partial edit
```

5. Retry the refactoring after fixing the underlying issue:

```
# Use the rename command again
F2 on the symbol to rename
```

## Examples

```
# Error: Unable to apply workspace edit
# File /home/user/project/src/utils.ts has been modified since the edit was prepared
# Expected line 42: export function helper()
# Actual line 42: export async function helper()
```

```bash
# Check git status to see what changed
git diff --name-only
# Revert partial changes if needed
git checkout -- src/utils.ts
```

## Related Errors

- [Refactor Error]({{< relref "/tools/vscode/refactor-error" >}}) -- refactoring failures
- [Rename Symbol]({{< relref "/tools/vscode/rename-symbol" >}}) -- symbol rename issues
- [Save Error]({{< relref "/tools/vscode/save-error" >}}) -- file save failures
