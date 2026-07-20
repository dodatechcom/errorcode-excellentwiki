---
title: "[Solution] Rails ActiveSupport::EventedFileUpdateChecker — File Watcher Errors"
description: "Fix Rails ActiveSupport file watcher errors. Handle EventedFileUpdateChecker issues and file change detection."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rails, file_watcher, active_support, evented"]
severity: "error"
---

# Rails ActiveEvent File Watcher Errors

## Error Message

```
RuntimeError: unable to create event machine thread
# or
NotImplementedError: file watcher not supported on this platform
# or
IOError: stream closed in another thread
```

## Common Causes

- File watcher not supported on the current platform
- listen gem not installed or incompatible
- Too many files being watched causing system limits
- EventMachine thread conflicts with other threads

## Solutions

### Solution 1: Install the listen Gem

The `listen` gem is required for file watching in development.

```ruby
# Gemfile
gem "listen", "~> 3.8"

# Install
bundle install

# Verify
rails server
# Should see: "Listening on http://127.0.0.1:3000"
```

### Solution 2: Increase File Watcher Limits

Raise system limits for watching many files.

```bash
# Linux: check current limit
cat /proc/sys/fs/inotify/max_user_watches

# Increase limit temporarily
sudo sysctl fs.inotify.max_user_watches=524288

# Make permanent
echo "fs.inotify.max_user_watches=524288" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

### Solution 3: Use Polling as Fallback

Configure Rails to use polling if native file watching fails.

```ruby
# config/environments/development.rb
config.file_watcher = ActiveSupport::EventedFileUpdateChecker

# Fallback to polling if listen gem has issues
config.file_watcher = ActiveSupport::FileUpdateChecker

# Or set environment variable
# LISTEN_GEM_FILESYSTEM_POLLING=1
```

### Solution 4: Configure File Watching Directories

Limit which directories are watched to reduce resource usage.

```ruby
# config/environments/development.rb
config.file_watcher = ActiveSupport::EventedFileUpdateChecker.new(
  [Rails.root.join("app")],  # watch only app/
  { reload: true }
)

# Ignore specific directories
config.file_watcher = ActiveSupport::EventedFileUpdateChecker.new(
  Dir[Rails.root.join("app/**/*.rb")],
  {}
)
```

## Prevention Tips

- Keep the `listen` gem updated for platform compatibility
- Increase `fs.inotify.max_user_watches` on Linux systems
- Watch only necessary directories to reduce resource usage
- Use polling mode as a fallback when native watching fails

## Related Errors

- [IOError]({{< relref "/languages/ruby/io-error" >}})
- [LoadError]({{< relref "/languages/ruby/load-error" >}})
- [RuntimeError]({{< relref "/languages/ruby/runtime-error" >}})
