---
title: "[Solution] Neovim Highlight error"
description: "Highlight error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "highlight", "hl", "colors", "syntax"]
severity: "error"
---

# Highlight error

## Error Message

```
Highlight group error.
Error: Unknown or invalid highlight group
```

## Common Causes

- Referencing a highlight group that has not been defined
- Treesitter highlighter conflict with vim syntax highlighting
- Invalid color specification in highlight definition

## Solutions

### Solution 1: Define highlight groups properly

Use safe highlight group definition with pcall:

```lua
local function safe_hl(name, opts)
  local ok, err = pcall(vim.api.nvim_set_hl, 0, name, opts)
  if not ok then
    vim.notify('Failed to set highlight ' .. name .. ': ' .. err, vim.log.levels.WARN)
  end
end

-- Define highlight groups
safe_hl('MyCustomGroup', {
  fg = '#ff9e64',
  bg = '#1a1b26',
  bold = true,
  italic = true,
  underline = true,
})

safe_hl('DiagnosticUnderlineError', {
  undercurl = true,
  sp = '#ff0000',
})

-- Link to existing groups
vim.api.nvim_set_hl(0, 'MyLinkedGroup', { link = 'Comment' })
```

### Solution 2: Debug highlight groups

Inspect and debug highlight group assignments:

```bash
-- Get highlight group info
:hi MyCustomGroup

-- Get all highlights containing a name
:hi Cursor

-- Get highlight at cursor position
:lua print(vim.inspect(vim.treesitter.get_captures_at_cursor(0)))

-- List all highlight groups
:highlight

-- Check if a group exists
local hl = vim.api.nvim_get_hl(0, { name = 'MyCustomGroup' })
if vim.tbl_isempty(hl) then
  vim.notify('Highlight group not defined')
else
  vim.notify('Highlight: ' .. vim.inspect(hl))
end
```

## Prevention Tips

- Use vim.api.nvim_get_hl() to check if a group exists
- Define highlights after colorscheme loads
- Use :checkhealth highlight for diagnostic info

## Related Errors

- [theme-error]({{< relref "/tools/neovim/theme-error" >}})
- [treesitter-error]({{< relref "/tools/neovim/treesitter-error" >}})
- [statusline-error]({{< relref "/tools/neovim/statusline-error" >}})
