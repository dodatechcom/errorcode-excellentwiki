---
title: "[Solution] Rails Credentials — Master Key, Encrypted Config, Edit/Decrypt Errors"
description: "Fix Rails credentials errors. Handle missing master key, decryption failures, and encrypted config issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rails, credentials, master_key, encrypted"]
severity: "error"
---

# Rails Credentials Errors

## Error Message

```
ActiveSupport::EncryptedConfiguration::Error: Missing encryption key
# or
RbNaCl::CryptoError: Decryption failed
# or
Errno::ENOENT: No such file or directory - config/credentials.yml.enc
```

## Common Causes

- Missing `RAILS_MASTER_KEY` environment variable or `config/master.key`
- `credentials.yml.enc` file corrupted or missing
- Wrong encryption key for the environment
- Editing credentials with `EDITOR` not set

## Solutions

### Solution 1: Set Up the Master Key

Create or restore the master key for decrypting credentials.

```bash
# Generate a new master key
rails credentials:edit

# This creates config/master.key and config/credentials.yml.enc

# Or set the key via environment variable
export RAIL_MASTER_KEY="your_master_key_here"

# View current credentials
EDITOR="cat" rails credentials:edit
```

### Solution 2: Fix Decryption Failures

Restore the master key if decryption fails.

```ruby
# config/credentials.yml.enc requires the master key
# If you lost config/master.key, you need to recreate credentials

# In production, set RAILS_MASTER_KEY env var
# On Render:
# RAILS_MASTER_KEY=your_key_here

# Or in .env:
# RAILS_MASTER_KEY=your_key_here
```

### Solution 3: Edit Credentials Safely

Use `rails credentials:edit` for secure editing.

```bash
# Edit credentials (opens in $EDITOR)
rails credentials:edit

# View without editing
EDITOR="cat" rails credentials:edit

# Edit environment-specific credentials
RAILS_ENV=production rails credentials:edit

# Check credentials in code
Rails.application.credentials.dig(:aws, :access_key_id)
Rails.application.credentials.secret_key_base
```

### Solution 4: Handle Environment-Specific Credentials

Use separate credentials files for each environment.

```bash
# config/credentials.yml.enc (default)
# config/credentials/production.yml.enc
# config/credentials/development.yml.enc

# Access in code
Rails.application.credentials.production
Rails.application.credentials.development

# Or use dig for nested keys
Rails.application.credentials.production.dig(:database, :password)
```

## Prevention Tips

- Never commit `config/master.key` to version control
- Use `RAILS_MASTER_KEY` environment variable in production
- Backup `config/master.key` securely before deploying
- Use `rails credentials:edit` instead of manually editing files

## Related Errors

- [Errno::ENOENT]({{< relref "/languages/ruby/file-not-found" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [SecurityError]({{< relref "/languages/ruby/permission-denied" >}})
