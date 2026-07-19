---
title: "[Solution] Eclipse Terminal error"
description: "Terminal error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "terminal", "shell", "command-line"]
severity: "error"
---

# Terminal error

## Error Message

```
Cannot launch terminal. The terminal emulator failed to start. Ensure that a local shell is available at /bin/bash or configure a different shell in Window > Preferences > Terminal.
```

## Common Causes

- The configured shell path does not exist on the system or is not executable.
- The Eclipse Terminal plugin is not installed or has been disabled.
- A permissions issue prevents Eclipse from accessing the shell binary.

## Solutions

### Solution 1: Install the Eclipse Terminal Plugin

Go to **Help > Eclipse Marketplace** and search for **TM Terminal**. Click **Install** and follow the installation wizard. After installation, open the Terminal view via **Window > Show View > Other > Terminal > Terminal**. The embedded terminal will use your system's default shell.

```java
# Check available shells on the system
which bash
which sh
which zsh
ls -la /bin/bash
ls -la /usr/bin/bash
```

### Solution 2: Configure the Terminal Shell Path

Open **Window > Preferences > Terminal** and set the **Shell path** to the absolute path of your shell. If using bash, try `/bin/bash`. For zsh, use `/bin/zsh`. Ensure the shell binary exists and is executable. You can also set environment variables in the terminal preferences.

```bash
# Verify shell is executable
chmod +x /bin/bash

# Check Eclipse terminal preferences file
# <workspace>/.metadata/.plugins/org.eclipse.ui.workbench/workbench.xml

# Alternative: use system terminal outside Eclipse
# Open system terminal and cd to project directory
```

## Prevention Tips

- Use **Open in System Terminal** from the Terminal view toolbar to open the OS native terminal.
- Set the terminal encoding to UTF-8 in **Window > Preferences > Terminal** for proper character display.
- Use the Terminal view's **Switch Terminal** button to manage multiple shell sessions.

## Related Errors

- [console-error]({{< relref "/tools/eclipse/console-error" >}})
- [run-configuration-error]({{< relref "/tools/eclipse/run-configuration-error" >}})
- [git-integration-error]({{< relref "/tools/eclipse/git-integration-error" >}})
