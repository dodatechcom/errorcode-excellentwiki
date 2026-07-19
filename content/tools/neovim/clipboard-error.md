---
title: "[Solution] Neovim Clipboard error"
description: "Clipboard error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "neovim"
tags: ["neovim", "vim", "ide", "clipboard", "copy", "paste", "yank"]
severity: "error"
---

# Clipboard error

## Error Message

```
Clipboard provider error.
Error: Clipboard provider not found or not working
```

## Common Causes

- No clipboard utility installed (xclip, xsel, wl-copy)
- Running in SSH session without X forwarding
- Wayland vs X11 clipboard provider mismatch

## Solutions

### Solution 1: Configure clipboard provider

Set up the clipboard provider for your environment:

```lua
-- For X11 (xclip)
vim.g.clipboard = {
  name = 'xclip',
  copy = {
    ['+'] = 'xclip -selection clipboard',
    ['*'] = 'xclip -selection primary',
  },
  paste = {
    ['+'] = 'xclip -selection clipboard -o',
    ['*'] = 'xclip -selection primary -o',
  },
}

-- For Wayland (wl-copy)
vim.g.clipboard = {
  name = 'wl-copy',
  copy = {
    ['+'] = 'wl-copy',
    ['*'] = 'wl-copy --primary',
  },
  paste = {
    ['+'] = 'wl-paste',
    ['*'] = 'wl-paste --primary',
  },
}
```

### Solution 2: Install clipboard tools

Install the appropriate clipboard utility for your system:

```bash
# Debian/Ubuntu
sudo apt install xclip
# or
sudo apt install xsel

# Fedora/RHEL
sudo dnf install xclip

# Arch Linux
sudo pacman -S xclip

# Wayland
sudo pacman -S wl-clipboard
# or
sudo apt install wl-clipboard

# macOS (built-in)
# pbcopy and pbpaste are included
```

## Prevention Tips

- Test clipboard with :checkhealth provider
- Use vim.fn.has('clipboard') to check clipboard support
- Set clipboard=unnamedplus to use system clipboard by default

## Related Errors

- [terminal-error]({{< relref "/tools/neovim/terminal-error" >}})
- [config-error]({{< relref "/tools/neovim/config-error" >}})
- [plugin-load-error]({{< relref "/tools/neovim/plugin-load-error" >}})
