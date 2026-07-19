---
title: "[Solution] Neovim Healthcheck error"
description: "Healthcheck error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "health", "check", "diagnostic", "status"]
severity: "error"
---

# Healthcheck error

## Error Message

```
Health check failed.
Error: checkhealth command encountered errors
```

## Common Causes

- Plugin health check function throws an error
- Required external tools not found by health check
- Health check function references outdated APIs

## Solutions

### Solution 1: Run checkhealth with verbose output

Use checkhealth to diagnose issues with Neovim and plugins:

```lua
-- Check all health
:checkhealth

-- Check specific plugin
:checkhealth nvim
:checkhealth treesitter
:checkhealth lsp

-- Verbose output
:checkhealth! vim.lsp

-- Check specific health check function
:lua require('checkhealth').run({ 'nvim-treesitter' })
```

### Solution 2: Fix health check failures

Address common health check failures:

```bash
# Common fixes for health check issues:

# 1. Install missing dependencies
# For treesitter:
vim.cmd('TSInstallSync lua vim vimdoc')

# 2. Verify LSP server installation
:lua print(vim.inspect(vim.lsp.get_active_clients()))

# 3. Check Python support
# Install pynvim: pip install pynvim

# 4. Check Node.js support
# Install neovim: npm install -g neovim

# 5. Check clipboard
:lua print(vim.fn.has('clipboard'))

# 6. Check for missing tools
:lua print(vim.fn.executable('git'))
```

## Prevention Tips

- Run :checkhealth after installing new plugins
- Fix critical issues before non-critical ones
- Use :checkhealth! to include optional checks

## Related Errors

- [config-error]({{< relref "/tools/neovim/config-error" >}})
- [plugin-load-error]({{< relref "/tools/neovim/plugin-load-error" >}})
- [lsp-initialize-error]({{< relref "/tools/neovim/lsp-initialize-error" >}})
