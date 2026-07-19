---
title: "[Solution] Neovim init.lua error"
description: "init.lua error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "init", "lua", "startup", "bootstrap"]
severity: "error"
---

# init.lua error

## Error Message

```
Error loading init.lua.
Error: attempt to index a nil value in init.lua
```

## Common Causes

- Syntax error in init.lua file
- Required module is not installed
- Variable used before initialization

## Solutions

### Solution 1: Check init.lua syntax

Validate your init.lua file for common errors:

```lua
-- Check for syntax errors
vim.cmd('luafile ' .. vim.fn.stdpath('config') .. '/init.lua')

-- Use verbose mode to trace issues
vim.o.verbose = 1
vim.o.verbosefile = '/tmp/nvim_init.log'
vim.cmd('source $MYVIMRC')
```

### Solution 2: Create modular init structure

Split init.lua into manageable modules:

```bash
-- init.lua
local lazypath = vim.fn.stdpath('data') .. '/lazy/lazy.nvim'
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    'git', 'clone',
    '--filter=blob:none',
    'https://github.com/folke/lazy.nvim.git',
    '--branch=stable',
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- Load options
require('config.options')
-- Load keymaps
require('config.keymaps')
-- Load plugins
require('config.plugins')
```

## Prevention Tips

- Start with minimal init.lua and add features incrementally
- Use require() for modular configuration
- Keep init.lua focused on bootstrap and core settings

## Related Errors

- [config-error]({{< relref "/tools/neovim/config-error" >}})
- [plugin-manager-error]({{< relref "/tools/neovim/plugin-manager-error" >}})
- [plugin-load-error]({{< relref "/tools/neovim/plugin-load-error" >}})
