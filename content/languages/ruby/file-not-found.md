---
title: "[Solution] Ruby Errno::ENOENT — No such file or directory Fix"
description: "Fix Ruby Errno::ENOENT: No such file or directory. Check file paths, verify existence, and handle missing files."
languages: ["ruby"]
severities: ["error"]
error_types: ["file"]
weight: 230
---

# Errno::ENOENT — No such file or directory Fix

An `Errno::ENOENT` is raised when a file or directory operation references a path that doesn't exist.

## Description

`Errno::ENOENT` (Error NO ENTry) is the most common file system error. It means the operating system cannot find the file or directory at the specified path.

Common scenarios:

- **File doesn't exist** — typo in filename or wrong directory.
- **Directory doesn't exist** — trying to read from a missing directory.
- **Symlink broken** — symbolic link points to non-existent target.
- **Case sensitivity** — `File.txt` vs `file.txt` on Linux.

## Common Causes

```ruby
# Cause 1: File doesn't exist
File.read("config.yml")  # Errno::ENOENT: No such file or directory

# Cause 2: Wrong path
File.read("src/main.rb")  # Errno::ENOENT if path is incorrect

# Cause 3: Directory doesn't exist
Dir.entries("/nonexistent/dir")  # Errno::ENOENT

# Cause 4: Broken symlink
File.read("link_to_missing")  # Errno::ENOENT if target doesn't exist
```

## Solutions

### Fix 1: Check file existence before access

```ruby
# Wrong
data = File.read("config.yml")

# Correct
if File.exist?("config.yml")
  data = File.read("config.yml")
else
  puts "Config file not found, using defaults"
  data = default_config
end
```

### Fix 2: Use begin/rescue for graceful handling

```ruby
# Wrong
config = File.read("config.yml")

# Correct
begin
  config = File.read("config.yml")
rescue Errno::ENOENT
  config = default_config
end
```

### Fix 3: Verify paths with File.directory?

```ruby
# Wrong
Dir.entries("/path/to/dir")  # Errno::ENOENT

# Correct
dir_path = "/path/to/dir"
if File.directory?(dir_path)
  entries = Dir.entries(dir_path)
else
  puts "Directory not found: #{dir_path}"
end
```

### Fix 4: Use File.expand_path for absolute paths

```ruby
# Wrong — relative path depends on working directory
File.read("data.txt")

# Correct — use absolute path
data_path = File.expand_path("../data.txt", __FILE__)
if File.exist?(data_path)
  data = File.read(data_path)
end
```

## Related Errors

- [Errno::EACCES](permission-denied) — permission denied.
- [LoadError](load-error) — cannot load such file.
- [IOError](io-error) — stream closed or invalid I/O.
