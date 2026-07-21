---
title: "[Solution] VS Code Terminal Shell Integration Error"
description: "Fix VS Code terminal shell integration errors when shell integration scripts fail to initialize or produce incorrect prompts."
tools: ["vscode"]
error-types: ["tool-error"]
severities: ["error"]
---

# VS Code Terminal Shell Integration Error

Terminal shell integration in VS Code allows the editor to detect command positions, prompts, and command output boundaries. When shell integration fails, features like command decorations, run selections, and prompt detection stop working.

## Common Causes

- Shell integration scripts are not installed for the active shell
- The `terminal.integrated.shellIntegration.enabled` setting is disabled
- A custom shell configuration overrides the integration injection
- Fish, zsh, or bashrc files contain conflicting prompt commands
- A firewall or security tool blocks the integration script

## How to Fix

1. Check that shell integration is enabled in settings:

```json
{
  "terminal.integrated.shellIntegration.enabled": true
}
```

2. Verify the shell integration script exists for your platform:

```bash
ls ~/.vscode/extensions/ms-vscode.shell-integration-*/shellIntegration.sh
```

3. Add the integration script manually to your shell profile if auto-injection fails:

```bash
# Add to ~/.bashrc or ~/.zshrc
source /usr/share/code/resources/app/out/vs/base/node/shellIntegration.sh
```

4. Disable custom prompt functions that conflict with shell integration:

```bash
# Temporarily comment out custom PROMPT_COMMAND in .bashrc
# PROMPT_COMMAND='custom_prompt'
```

5. Restart VS Code and open a new terminal session.

## Examples

```bash
# Verify shell integration is active in a terminal
echo $VSCODE_SHELL_INTEGRATION
# Should print: 1

# If blank, shell integration is not loaded
# Check the output panel for shell integration errors
```

```
# Typical error in Output > Terminal panel
[Shell Integration] Failed to activate shell integration for /bin/bash
```

## Related Errors

- [Terminal Error]({{< relref "/tools/vscode/terminal-error" >}}) -- general terminal failures
- [Integrated Terminal]({{< relref "/tools/vscode/integrated-terminal" >}}) -- terminal startup issues
