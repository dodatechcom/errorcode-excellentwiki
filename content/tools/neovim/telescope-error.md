---
title: "[Solution] Neovim Telescope error"
description: "Telescope error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "telescope", "fuzzy-finder", "search", "picker"]
severity: "error"
---

# Telescope error

## Error Message

```
Telescope fuzzy finder error occurred.
Error: picker failed to render results
```

## Common Causes

- Telescope dependencies not installed (plenary.nvim)
- Picker configuration is invalid
- File permissions prevent access to search directories

## Solutions

### Solution 1: Verify Telescope dependencies

Ensure plenary.nvim and other dependencies are installed. Telescope relies on plenary.nvim for asynchronous operations and file system utilities. Without it, most pickers will fail immediately. The fzf-native extension is optional but significantly improves filtering performance for large result sets. Always install the native extension alongside Telescope for the best experience.

```lua
require('lazy').setup({
  {
    'nvim-telescope/telescope.nvim',
    branch = '0.1.x',
    dependencies = {
      'nvim-lua/plenary.nvim',
      { 'nvim-telescope/telescope-fzf-native.nvim', build = 'make' },
      'nvim-tree/nvim-web-devicons',
    },
    config = function()
      local telescope = require('telescope')
      telescope.setup({
        defaults = {
          file_ignore_patterns = { 'node_modules', '.git/' },
          layout_strategy = 'horizontal',
        },
      })
      telescope.load_extension('fzf')
    end,
  },
})
```

### Solution 2: Reset Telescope state

Clear Telescope state and restart the picker when errors persist. Sometimes the internal state becomes corrupted after a failed search or when the working directory changes. You can also configure custom pickers with specific paths to avoid searching inaccessible directories:

```lua
vim.api.nvim_create_autocmd('User', {
  pattern = 'TelescopeComplete',
  callback = function()
    vim.g.telescope_state = {}
  end,
})

-- Create a safe file finder that avoids common problematic directories
vim.keymap.set('n', '<leader>ff', function()
  require('telescope.builtin').find_files({
    find_command = { 'find', '.', '-type', 'f', '-not', '-path', '*/node_modules/*' },
  })
end, { desc = 'Find files safely' })
```

## Prevention Tips

- Keep Telescope and all dependencies updated to their latest versions regularly
- Use :checkhealth telescope for comprehensive diagnostics on missing components
- Consider using fzf-native for significantly better performance on large codebases
- Add file_ignore_patterns to skip directories like node_modules and .git
- Use pcall around Telescope API calls to gracefully handle picker failures

## Related Errors

- [plugin-load-error]({{< relref "/tools/neovim/plugin-load-error" >}})
- [keymap-error]({{< relref "/tools/neovim/keymap-error" >}})
- [float-error]({{< relref "/tools/neovim/float-error" >}})
