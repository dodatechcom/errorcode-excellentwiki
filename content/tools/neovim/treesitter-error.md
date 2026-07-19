---
title: "[Solution] Neovim Treesitter parser error"
description: "Treesitter error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "treesitter", "parser", "syntax", "highlight"]
severity: "error"
---

# Treesitter parser error

## Error Message

```
Treesitter parser failed to load.
Error: no parser for 'language' language
```

## Common Causes

- Treesitter parser for the language is not installed
- Parser version is incompatible with current Treesitter version
- Treesitter configuration has errors

## Solutions

### Solution 1: Install the missing parser

Use the Treesitter command to install parsers:

```lua
vim.api.nvim_command('TSInstall lua')
-- Or install all recommended parsers
vim.api.nvim_command('TSInstallSync all')
-- Or check installed parsers
vim.api.nvim_command('TSInstallInfo')
```

### Solution 2: Configure Treesitter

Set up Treesitter with proper configuration:

```bash
require('nvim-treesitter.configs').setup({
  ensure_installed = {
    'lua', 'vim', 'vimdoc', 'javascript', 'typescript',
    'json', 'html', 'css', 'markdown', 'python',
  },
  highlight = {
    enable = true,
    additional_vim_regex_highlighting = false,
  },
  indent = {
    enable = true,
  },
  rainbow = {
    enable = true,
    extended_mode = true,
    max_file_lines = nil,
  },
})
```

## Prevention Tips

- Keep parsers updated with :TSUpdate
- Check parser compatibility with :checkhealth treesitter
- Disable treesitter for problematic file types if needed

## Related Errors

- [highlight-error]({{< relref "/tools/neovim/highlight-error" >}})
- [config-error]({{< relref "/tools/neovim/config-error" >}})
- [plugin-load-error]({{< relref "/tools/neovim/plugin-load-error" >}})
