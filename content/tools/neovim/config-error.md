---
title: "[Solution] Neovim Configuration error"
description: "Configuration error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "config", "setup", "lua", "init"]
severity: "error"
---

# Configuration error

## Error Message

```
Neovim configuration error.
Error: invalid option or unknown setting
```

## Common Causes

- Lua syntax error in configuration file
- Using deprecated or removed options
- Conflicting settings between multiple plugins

## Solutions

### Solution 1: Validate Lua syntax

Check your configuration files for syntax errors:

```lua
-- Check Lua syntax with luac
-- Run in terminal: luac -p init.lua

-- Or check within Neovim
vim.cmd('luafile %')

-- Use pcall to catch errors
local ok, err = pcall(function()
  vim.cmd('source $MYVIMRC')
end)
if not ok then
  print('Error: ' .. err)
end
```

### Solution 2: Use minimal configuration

Test with a minimal config to isolate the issue:

```bash
-- minimal.lua
vim.opt.rtp:prepend(vim.fn.stdpath('data') .. '/lazy/lazy.nvim')
require('lazy').setup({
  spec = {},
  -- Add only the plugin you want to test
})

-- Launch with: nvim --config minimal.lua
```

## Prevention Tips

- Use a modular configuration structure
- Validate configuration files regularly
- Keep backup of working configurations

## Related Errors

- [init-lua-error]({{< relref "/tools/neovim/init-lua-error" >}})
- [plugin-load-error]({{< relref "/tools/neovim/plugin-load-error" >}})
- [highlight-error]({{< relref "/tools/neovim/highlight-error" >}})
