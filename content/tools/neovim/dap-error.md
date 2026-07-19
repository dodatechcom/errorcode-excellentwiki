---
title: "[Solution] Neovim DAP adapter error"
description: "DAP error (debugging)"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "dap", "debugging", "adapter", "breakpoint"]
severity: "error"
---

# DAP adapter error

## Error Message

```
Debug Adapter Protocol error.
Error: DAP adapter failed to connect
```

## Common Causes

- DAP adapter binary not installed or not in PATH
- Debugger configuration file is missing or invalid
- Port conflict with existing debugging session

## Solutions

### Solution 1: Install DAP adapter

Ensure the debugging adapter is installed via Mason or manually:

```lua
require('mason').setup()
require('mason-nvim-dap').setup({
  ensure_installed = {
    'delve',      -- Go
    'node2',      -- Node.js
    'codelldb',   -- Rust/C/C++
    'python',     -- Python
  },
  automatic_installation = true,
})
```

### Solution 2: Configure DAP settings

Set up DAP with proper configuration:

```bash
local dap = require('dap')

dap.configurations.python = {
  {
    type = 'python',
    request = 'launch',
    name = 'Launch file',
    program = '${file}',
    pythonPath = function()
      return '/usr/bin/python3'
    end,
  },
}

require('dapui').setup()
require('nvim-dap-virtual-text').setup()
```

## Prevention Tips

- Use :DapStatus to check adapter connection status
- Set breakpoints with <leader>db
- Install language-specific DAP extensions via Mason

## Related Errors

- [mason-error]({{< relref "/tools/neovim/mason-error" >}})
- [config-error]({{< relref "/tools/neovim/config-error" >}})
- [plugin-load-error]({{< relref "/tools/neovim/plugin-load-error" >}})
