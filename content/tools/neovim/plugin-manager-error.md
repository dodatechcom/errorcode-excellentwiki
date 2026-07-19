---
title: "[Solution] Neovim Plugin manager error"
description: "Plugin manager error (lazy.nvim/packer)"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "plugin", "manager", "lazy", "packer", "install"]
severity: "error"
---

# Plugin manager error

## Error Message

```
Failed to load plugin manager configuration.
Error: Unable to resolve plugin dependencies
```

## Common Causes

- Plugin manager configuration file has syntax errors
- Git repository is not accessible or has been moved
- Circular plugin dependencies or conflicts

## Solutions

### Solution 1: Verify plugin manager configuration

Check your plugin manager config file for syntax errors:

```lua
-- For lazy.nvim
require('lazy').setup({
  spec = {
    { 'nvim-treesitter/nvim-treesitter', build = ':TSUpdate' },
    { 'nvim-telescope/telescope.nvim', dependencies = { 'nvim-lua/plenary.nvim' } },
  },
  checker = { enabled = true },
})
```

### Solution 2: Clean and reinstall plugins

Force a clean installation of all plugins:

```bash
# For lazy.nvim
nvim --headless "+Lazy! sync" +qa

# For packer
nvim --headless -c 'autocmd User PackerComplete quitall' -c 'PackerSync'
```

## Prevention Tips

- Always backup your plugin list before making major changes
- Use lock files to ensure consistent plugin versions
- Regularly update plugins to get bug fixes and compatibility updates

## Related Errors

- [plugin-load-error]({{< relref "/tools/neovim/plugin-load-error" >}})
- [lazy-error]({{< relref "/tools/neovim/lazy-error" >}})
- [packer-error]({{< relref "/tools/neovim/packer-error" >}})
