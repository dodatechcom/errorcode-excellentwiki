---
title: "[Solution] EACCES npm Error — Permission Denied Global Install"
description: "Fix EACCES permission errors when installing npm packages globally. Use nvm, change npm prefix, or use sudo safely."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# EACCES npm Global Install Error

npm global installs fail due to directory ownership.

## Fix (Recommended)

Use a Node version manager:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install node
```

## Alternative

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:/home/admin1/.nvm/versions/node/v22.23.1/bin:/home/admin1/.cargo/bin:/home/admin1/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/admin1/.fzf/bin' >> ~/.bashrc
```
