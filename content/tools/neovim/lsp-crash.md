---
title: "[Solution] Neovim LSP server crashed"
description: "LSP crash"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "lsp", "language-server", "crash", "server"]
severity: "error"
---

# LSP server crashed

## Error Message

```
Language server protocol (LSP) server has crashed unexpectedly.
Error: LSP server process terminated with exit code 1
```

## Common Causes

- The language server binary is corrupted or incompatible
- Insufficient memory allocated to the LSP server process
- Conflicting LSP configurations in project or user settings

## Solutions

### Solution 1: Restart the LSP server

Use Neovim's built-in LSP restart command to restart the crashed server. This is the quickest way to recover from an LSP crash without restarting Neovim entirely. The restart command will terminate the existing server process and spawn a fresh instance with the same configuration. You can also target specific servers by name if multiple LSP servers are running simultaneously:

```lua
vim.api.nvim_command('LspRestart')
-- Or for a specific server
vim.api.nvim_command('LspStop')
vim.api.nvim_command('LspStart')

-- List all active LSP clients
local clients = vim.lsp.get_active_clients()
for _, client in ipairs(clients) do
  print('Active LSP: ' .. client.name)
end
```

### Solution 2: Check LSP server logs

Enable verbose logging to diagnose the crash cause and understand why the server terminated. The logs will contain detailed information about the crash, including any error messages or stack traces from the language server process. Regular review of these logs can help you identify patterns before they become critical failures:

```bash
vim.lsp.set_log_level('debug')
-- View logs with:
-- :lua vim.cmd('edit ' .. vim.lsp.get_log_path())

-- You can also filter logs programmatically
local log = require('vim.lsp.log')
-- Check the log file at the path returned by vim.lsp.get_log_path()
```

## Prevention Tips

- Regularly update your LSP server binaries to the latest stable release
- Monitor memory usage during heavy editing sessions with large files
- Keep Neovim and plugins updated to latest stable versions for bug fixes
- Consider increasing system memory limits if crashes are frequent
- Use :checkhealth lsp regularly to catch issues before they cause crashes

## Related Errors

- [lsp-timeout]({{< relref "/tools/neovim/lsp-timeout" >}})
- [lsp-initialize-error]({{< relref "/tools/neovim/lsp-initialize-error" >}})
- [lsp-diagnostics-error]({{< relref "/tools/neovim/lsp-diagnostics-error" >}})
