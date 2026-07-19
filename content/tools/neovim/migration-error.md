---
title: "[Solution] Neovim Migration from Vim error"
description: "Migration error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "migration", "vim", "compatibility", "legacy"]
severity: "error"
---

# Migration from Vim error

## Error Message

```
Vim compatibility error.
Error: Vim script command not supported in Neovim Lua
```

## Common Causes

- Using deprecated Vim script syntax in Lua configuration
- Vimscript function not available in Lua API
- Mixed Vim script and Lua causing initialization order issues

## Solutions

### Solution 1: Convert Vim script to Lua

Replace Vim script commands with their Lua equivalents:

```lua
-- Instead of: set number
vim.opt.number = true

-- Instead of: set tabstop=4
vim.opt.tabstop = 4

-- Instead of: command! Test echo 'hello'
vim.api.nvim_create_user_command('Test', function()
  vim.notify('hello')
end, {})

-- Instead of: autocmd BufWritePost *.lua echo 'saved'
vim.api.nvim_create_autocmd('BufWritePost', {
  pattern = '*.lua',
  callback = function()
    vim.notify('saved')
  end,
})

-- Instead of: let g:var = 1
vim.g.var = 1

-- Instead of: echo g:var
print(vim.g.var)
```

### Solution 2: Use vim.cmd for Vim script compatibility

When Lua equivalents don't exist, use vim.cmd as a bridge:

```bash
# Use vim.cmd for Vim script commands
vim.cmd('source $MYVIMRC')
vim.cmd('echo "Hello from Vim script"')

# Execute block of Vim script
vim.cmd([[
  function! MyVimFunction()
    echo 'This is a Vim function'
  endfunction
  command! CallVimFunc call MyVimFunction()
]])

# Use vim.fn for Vim functions
local home = vim.fn.expand('~')
local files = vim.fn.glob('/path/*', false, true)
vim.fn.system('echo hello')

# Mix Vim and Lua safely
vim.cmd('runtime plugin/matchit.vim')
require('my_lua_module')
```

## Prevention Tips

- Gradually migrate from Vim script to Lua
- Use vim.cmd() as a bridge during migration
- Test Vim script functions with vim.fn.exists()

## Related Errors

- [init-lua-error]({{< relref "/tools/neovim/init-lua-error" >}})
- [config-error]({{< relref "/tools/neovim/config-error" >}})
- [plugin-load-error]({{< relref "/tools/neovim/plugin-load-error" >}})
