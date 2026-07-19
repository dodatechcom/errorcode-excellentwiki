---
title: "[Solution] Neovim Autocommand error"
description: "Autocommand error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "autocmd", "event", "callback", "pattern"]
severity: "error"
---

# Autocommand error

## Error Message

```
Autocommand callback error.
Error: Error detected in autocmd callback
```

## Common Causes

- Autocommand callback function throws an error
- Event fires before expected resources are available
- Recursive autocommand triggering infinite loop

## Solutions

### Solution 1: Use protected callbacks

Wrap autocmd callbacks in error handlers:

```lua
vim.api.nvim_create_autocmd('BufWritePost', {
  pattern = '*.lua',
  callback = function(args)
    local ok, err = pcall(function()
      -- Your autocmd logic here
      local file = args.match
      vim.notify('File saved: ' .. file)
      -- Run linter
      local result = vim.fn.system('luacheck ' .. vim.fn.shellescape(file))
      if vim.v.shell_error ~= 0 then
        vim.notify('Lint errors found', vim.log.levels.WARN)
      end
    end)
    if not ok then
      vim.notify('Autocmd error: ' .. tostring(err), vim.log.levels.ERROR)
    end
  end,
})
```

### Solution 2: Prevent recursive autocommands

Use a guard variable to prevent infinite recursion:

```bash
local autocmd_guard = false

vim.api.nvim_create_autocmd('TextChanged', {
  pattern = '*',
  callback = function()
    if autocmd_guard then return end
    autocmd_guard = true

    pcall(function()
      -- Your logic here
      vim.cmd('noautocmd silent write')
    end)

    autocmd_guard = false
  end,
})
```

## Prevention Tips

- Always use pcall() in autocmd callbacks
- Set once = true for one-shot autocommands when appropriate
- Use :autocmd! to clear conflicting autocommands

## Related Errors

- [keymap-error]({{< relref "/tools/neovim/keymap-error" >}})
- [config-error]({{< relref "/tools/neovim/config-error" >}})
- [init-lua-error]({{< relref "/tools/neovim/init-lua-error" >}})
