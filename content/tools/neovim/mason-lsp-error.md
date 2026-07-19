---
title: "[Solution] Neovim Mason LSP config error"
description: "Mason LSP error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "mason", "lsp", "configuration", "setup"]
severity: "error"
---

# Mason LSP config error

## Error Message

```
Mason LSP configuration error.
Error: failed to setup language server via mason
```

## Common Causes

- Mason-lspconfig bridge not properly configured
- LSP server requires manual configuration after Mason install
- Version mismatch between Mason and lspconfig

## Solutions

### Solution 1: Configure mason-lspconfig

Set up the mason-lspconfig bridge correctly:

```lua
require('mason').setup()
require('mason-lspconfig').setup({
  ensure_installed = {
    'lua_ls',
    'ts_ls',
    'pyright',
    'rust_analyzer',
  },
  automatic_installation = true,
})

require('mason-lspconfig').setup_handlers({
  function(server_name)
    require('lspconfig')[server_name].setup({})
  end,
})
```

### Solution 2: Manual LSP configuration

Manually configure LSP servers that Mason installs:

```bash
local lspconfig = require('lspconfig')

lspconfig.lua_ls.setup({
  settings = {
    Lua = {
      runtime = { version = 'LuaJIT' },
      diagnostics = { globals = { 'vim' } },
      workspace = { library = vim.api.nvim_get_runtime_file('', true) },
    },
  },
})
```

## Prevention Tips

- Run :checkhealth mason to verify installation
- Keep mason.nvim and mason-lspconfig.nvim versions synced
- Use :LspInfo to verify server configuration

## Related Errors

- [mason-error]({{< relref "/tools/neovim/mason-error" >}})
- [lsp-initialize-error]({{< relref "/tools/neovim/lsp-initialize-error" >}})
- [config-error]({{< relref "/tools/neovim/config-error" >}})
