---
title: "[Solution] Neovim LSP request timed out"
description: "LSP timeout"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "lsp", "timeout", "performance", "slow"]
severity: "error"
---

# LSP request timed out

## Error Message

```
LSP request timed out after 30000ms.
Warning: Request textDocument/hover timed out
```

## Common Causes

- LSP server is overloaded with too many concurrent requests
- Network latency connecting to remote language servers
- Project is too large for the LSP server to handle efficiently

## Solutions

### Solution 1: Increase timeout settings

Configure the LSP client with a higher timeout value:

```lua
vim.lsp.config('*.lua', {
  capabilities = vim.lsp.protocol.make_client_capabilities(),
  timeout = 60000,  -- 60 seconds
  flags = {
    debounce_text_changes = 150,
  },
})
```

### Solution 2: Optimize LSP configuration

Disable unnecessary features to reduce LSP server load:

```bash
vim.lsp.config('*.lua', {
  settings = {
    Lua = {
      diagnostics = { enable = true },
      format = { enable = false },
      completion = { autoRequire = false },
    },
  },
})
```

## Prevention Tips

- Add large directories to .gitignore to reduce indexing scope
- Use workspace/symbol only when needed
- Consider using a lighter LSP server for large projects

## Related Errors

- [lsp-crash]({{< relref "/tools/neovim/lsp-crash" >}})
- [lsp-initialize-error]({{< relref "/tools/neovim/lsp-initialize-error" >}})
- [treesitter-error]({{< relref "/tools/neovim/treesitter-error" >}})
