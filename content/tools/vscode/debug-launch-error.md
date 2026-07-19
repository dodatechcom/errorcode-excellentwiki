---
title: "[Solution] VS Code Cannot launch debug target"
description: "Fix VS Code debug launch errors. Resolve issues when the debugger fails to start or attach to a target."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "debugging", "launch", "configuration"]
severity: "error"
---

# Cannot launch debug target

## Error Message

```
Cannot launch debug target: Unable to launch program 'src/app.js'. Ensure the program path exists and you have permission to execute it.
```

## Common Causes

- The launch.json configuration has an incorrect program path
- Required runtime (Node.js, Python, etc.) is not installed or not in PATH
- Port used for debugging is already occupied by another process
- Missing debugger extension for the target language

## Solutions

### Solution 1: Verify launch.json Configuration

Check your launch.json file for correct program path, runtime arguments, and debug configuration settings.

```
{"version": "0.2.0", "configurations": [{"type": "node", "request": "launch", "name": "Launch Program", "program": "${workspaceFolder}/src/app.js", "console": "integratedTerminal"}]}
```

### Solution 2: Check Runtime Installation

Verify the required runtime is installed and accessible from the command line.

```
node --version && which node
```

### Solution 3: Free Debugging Port

Kill any process using the default debugging port, or configure a different port in launch.json.

```
lsof -ti:9229 | xargs kill -9
```

## Prevention Tips

- Use the built-in debugger configuration generator for new projects
- Check the Debug Console panel for detailed error output
- Ensure file permissions allow execution of the target program

## Related Errors

- [Cannot attach to target process]({{< relref "/tools/vscode/debug-attach-error" >}})
- [Breakpoint could not be set]({{< relref "/tools/vscode/debug-breakpoint-error" >}})
- [Terminal process failed to launch]({{< relref "/tools/vscode/terminal-error" >}})
