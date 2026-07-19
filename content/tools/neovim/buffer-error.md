---
title: "[Solution] Neovim Buffer error"
description: "Buffer error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "buffer", "file", "memory", "storage"]
severity: "error"
---

# Buffer error

## Error Message

```
Buffer operation failed.
Error: Invalid buffer id or buffer no longer exists
```

## Common Causes

- Referencing a buffer that has been deleted or wiped out
- Buffer-local options set on an invalid buffer handle
- Race condition between async operations on buffers

## Solutions

### Solution 1: Validate buffer before operations

Always check if a buffer exists before performing operations:

```lua
local function safe_buf_action(bufnr)
  if not vim.api.nvim_buf_is_valid(bufnr) then
    vim.notify('Buffer ' .. bufnr .. ' is not valid', vim.log.levels.WARN)
    return
  end
  -- Safe to operate on the buffer
  local lines = vim.api.nvim_buf_get_lines(bufnr, 0, -1, false)
  vim.notify('Buffer has ' .. #lines .. ' lines')
end

-- Use it
safe_buf_action(0)  -- current buffer
```

### Solution 2: Manage buffer lifecycle

Properly handle buffer creation and deletion:

```bash
-- Create a scratch buffer
local buf = vim.api.nvim_create_buf(false, true)
vim.api.nvim_buf_set_lines(buf, 0, -1, false, {'Hello', 'World'})

-- Listen for buffer wipeout
vim.api.nvim_create_autocmd('BufWipeout', {
  callback = function(args)
    print('Buffer ' .. args.buf .. ' was wiped out')
  end,
  buffer = buf,
})

-- Delete buffer when done
vim.api.nvim_buf_delete(buf, { force = false })
```

## Prevention Tips

- Use vim.api.nvim_buf_is_valid() before all buffer operations
- Prefer buffer-local autocommands for cleanup
- Avoid storing buffer handles across sessions

## Related Errors

- [window-error]({{< relref "/tools/neovim/window-error" >}})
- [tab-error]({{< relref "/tools/neovim/tab-error" >}})
- [config-error]({{< relref "/tools/neovim/config-error" >}})
