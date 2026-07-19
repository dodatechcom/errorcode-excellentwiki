---
title: "[Solution] VS Code Format document failed"
description: "Fix VS Code formatting errors. Resolve issues when the document formatter fails or produces incorrect output."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "formatting", "prettier", "code-style"]
severity: "error"
---

# Format document failed

## Error Message

```
Format document failed: Cannot format 'app.js' because formatter 'prettier' is not installed or not configured. Install the formatter extension.
```

## Common Causes

- No formatter extension is installed for the current language
- Formatter configuration file is missing or invalid
- Extension workspace trust restrictions prevent formatter execution
- Multiple formatters conflict and no default is configured

## Solutions

### Solution 1: Configure Default Formatter

Set the default formatter in VS Code settings for each language or globally.

```
{"editor.defaultFormatter": "esbenp.prettier-vscode", "editor.formatOnSave": true, "[python]": {"editor.defaultFormatter": "ms-python.black-formatter"}}
```

### Solution 2: Install Formatter Extensions

Install the appropriate formatter extension for your language and coding style.

```
code --install-extension esbenp.prettier-vscode && code --install-extension esbenp.prettier-vscode --force
```

### Solution 3: Configure Formatter Rules

Create or update the formatter configuration file in your project root with specific formatting rules.

```
{"semi": true, "trailingComma": "es5", "singleQuote": true, "printWidth": 100, "tabWidth": 2}
```

## Prevention Tips

- Enable format on save for consistent code style
- Create .prettierrc or .editorconfig files in project root
- Use the Format Document with... command to switch formatters

## Related Errors

- [Lint error]({{< relref "/tools/vscode/lint-error" >}})
- [Extension activation failed]({{< relref "/tools/vscode/extension-activation-failed" >}})
- [Emmet abbreviation not working]({{< relref "/tools/vscode/emmet-error" >}})
