---
title: "[Solution] GitHub Actions Windows Runner Error"
description: "Fix GitHub Actions Windows runner specific errors and quirks."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Windows runner errors can include path separator issues, shell differences, and missing tools:

```
Error: The term 'apt-get' is not recognized as a name of a cmdlet
```

## Common Causes

- Using Linux commands on a Windows runner.
- Path separators: Windows uses `\\` while Linux uses `/`.
- Shell defaults to PowerShell, not bash.

## How to Fix

**Use the `shell` key to specify bash:**

```yaml
steps:
  - name: Run in bash
    shell: bash
    run: echo "Using bash shell"
```

## Examples

```yaml
# Wrong - apt-get does not exist on Windows
steps:
  - run: apt-get install -y curl

# Correct - use platform-specific approach
steps:
  - shell: bash
    run: echo "Platform: $RUNNER_OS"
```
