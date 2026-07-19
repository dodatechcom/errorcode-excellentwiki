---
title: "[Solution] Neovim Plugin failed to load"
description: "Plugin load error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "plugin", "load", "startup", "error"]
severity: "error"
---

# Plugin failed to load

## Error Message

```
Failed to load plugin module.
Error: module 'plugin_name' not found
```

## Common Causes

- Plugin dependencies are not installed
- Plugin requires specific Neovim version or features
- Plugin initialization code has errors

## Solutions

### Solution 1: Check plugin dependencies

Ensure all required dependencies are listed in your plugin spec. Many plugins depend on other plugins to function correctly, and missing dependencies are the most common cause of load failures. Always check the plugin's README for required dependencies and include them in your configuration. For lazy.nvim, dependencies are automatically installed and loaded before the parent plugin:

```lua
require('lazy').setup({
  {
    'plugin/name',
    dependencies = {
      'dependency1/dep1',
      'dependency2/dep2',
    },
    config = function()
      require('plugin').setup({})
    end,
  },
})
```

### Solution 2: Debug plugin loading

Use verbose logging to trace plugin loading issues and identify which module is causing the failure. Enable verbose output before sourcing your configuration to capture detailed information about each plugin's initialization process:

```bash
vim.o.verbose = 1
vim.o.verbosefile = '/tmp/nvim_verbose.log'
vim.cmd('source $MYVIMRC')
-- Check the log file for detailed information
vim.cmd('!cat /tmp/nvim_verbose.log')
```

### Solution 3: Test with minimal configuration

Create a stripped-down configuration to isolate the problematic plugin. Start with only the essential plugins and add others one at a time until you identify the culprit. This binary search approach is the fastest way to find conflicting or broken plugins:

```lua
-- minimal_init.lua
vim.opt.rtp:prepend(vim.fn.stdpath('data') .. '/lazy/lazy.nvim')
require('lazy').setup({
  spec = {
    -- Add only the plugin you want to test
    { 'plugin/to-test' },
  },
})
```

## Prevention Tips

- Load plugins in correct order (dependencies first before main plugins)
- Use lazy loading to defer non-critical plugins until they are needed
- Test configuration changes with minimal init before applying them
- Pin plugin versions in lock files to prevent unexpected breakage
- Read plugin changelogs before updating to understand breaking changes

## Related Errors

- [plugin-manager-error]({{< relref "/tools/neovim/plugin-manager-error" >}})
- [config-error]({{< relref "/tools/neovim/config-error" >}})
- [lazy-error]({{< relref "/tools/neovim/lazy-error" >}})
