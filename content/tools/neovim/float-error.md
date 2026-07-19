---
title: "[Solution] Neovim Floating window error"
description: "Float error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "float", "floating", "popup", "window"]
severity: "error"
---

# Floating window error

## Error Message

```
Floating window error.
Error: Failed to create floating window
```

## Common Causes

- Invalid floating window configuration
- Window position calculated outside screen bounds
- Buffer for floating window is not valid

## Solutions

### Solution 1: Create floats safely

Use proper error handling for floating windows:

```lua
local function create_float(opts)
  local buf = vim.api.nvim_create_buf(false, true)

  -- Set buffer content if provided
  if opts.lines then
    vim.api.nvim_buf_set_lines(buf, 0, -1, false, opts.lines)
  end

  local width = opts.width or 60
  local height = opts.height or 15

  -- Ensure float is within screen bounds
  local screen_width = vim.o.columns
  local screen_height = vim.o.lines
  width = math.min(width, screen_width - 4)
  height = math.min(height, screen_height - 4)

  local win_opts = {
    relative = 'editor',
    width = width,
    height = height,
    row = math.floor((screen_height - height) / 2),
    col = math.floor((screen_width - width) / 2),
    style = 'minimal',
    border = 'rounded',
  }

  local ok, win = pcall(vim.api.nvim_open_win, buf, true, win_opts)
  if not ok then
    vim.notify('Failed to create float: ' .. tostring(win), vim.log.levels.ERROR)
    vim.api.nvim_buf_delete(buf, { force = true })
    return nil, nil
  end

  return win, buf
end
```

### Solution 2: Manage float lifecycle

Properly track and clean up floating windows:

```bash
local float_manager = {
  floats = {},
}

function float_manager:create(opts)
  local win, buf = create_float(opts)
  if win then
    table.insert(self.floats, { win = win, buf = buf })

    -- Auto-close on BufLeave
    vim.api.nvim_create_autocmd('BufLeave', {
      buffer = buf,
      once = true,
      callback = function()
        self:close(win)
      end,
    })
  end
  return win, buf
end

function float_manager:close(win)
  if vim.api.nvim_win_is_valid(win) then
    vim.api.nvim_win_close(win, true)
  end
end

function float_manager:close_all()
  for _, float in ipairs(self.floats) do
    self:close(float.win)
    if vim.api.nvim_buf_is_valid(float.buf) then
      vim.api.nvim_buf_delete(float.buf, { force = true })
    end
  end
  self.floats = {}
end
```

## Prevention Tips

- Always use pcall() when creating floating windows
- Calculate float position relative to editor dimensions
- Implement BufLeave autocmds for automatic cleanup

## Related Errors

- [window-error]({{< relref "/tools/neovim/window-error" >}})
- [buffer-error]({{< relref "/tools/neovim/buffer-error" >}})
- [statusline-error]({{< relref "/tools/neovim/statusline-error" >}})
