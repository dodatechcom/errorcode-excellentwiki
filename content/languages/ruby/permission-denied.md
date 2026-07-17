---
title: "[Solution] Ruby Errno::EACCES — Permission Denied Fix"
description: "Fix Ruby Errno::EACCES: Permission denied. Check file permissions, user ownership, and directory access."
languages: ["ruby"]
severities: ["error"]
error_types: ["permission"]
weight: 240
---

# Errno::EACCES — Permission Denied Fix

An `Errno::EACCES` is raised when a file system operation is denied due to insufficient permissions.

## Description

`Errno::EACCES` means the operating system denied access to a file or directory. This can be due to file permissions, directory permissions, or ownership issues.

Common scenarios:

- **Read without permission** — file not readable by current user.
- **Write without permission** — file not writable by current user.
- **Execute without permission** — trying to execute a non-executable file.
- **Directory not accessible** — parent directory permissions prevent access.
- **Root-only files** — trying to modify system files without root.

## Common Causes

```ruby
# Cause 1: Read from protected file
File.read("/etc/shadow")  # Errno::EACCES: Permission denied

# Cause 2: Write to read-only file
File.write("/usr/bin/program", "data")  # Errno::EACCES

# Cause 3: Create file in protected directory
File.write("/root/file.txt", "data")  # Errno::EACCES

# Cause 4: Execute non-executable file
system("/path/to/script.sh")  # Errno::EACCES if not executable
```

## Solutions

### Fix 1: Check file permissions

```ruby
if File.readable?(filename)
  data = File.read(filename)
else
  puts "Cannot read #{filename}: permission denied"
end

if File.writable?(filename)
  File.write(filename, data)
else
  puts "Cannot write #{filename}: permission denied"
end
```

### Fix 2: Use begin/rescue for permission errors

```ruby
begin
  data = File.read("/etc/shadow")
rescue Errno::EACCES => e
  puts "Permission denied: #{e.message}"
rescue Errno::ENOENT => e
  puts "File not found: #{e.message}"
end
```

### Fix 3: Use proper file modes

```ruby
# Create file with specific permissions
File.open("file.txt", File::WRONLY | File::CREAT, 0644) do |f|
  f.write("data")
end

# Make file executable
File.chmod(0755, "script.sh")
```

### Fix 4: Check directory permissions

```ruby
dir = "/path/to/directory"
if File.directory?(dir) && File.writable?(dir)
  File.write("#{dir}/file.txt", "data")
else
  puts "Cannot write to #{dir}: check permissions"
end
```

## Related Errors

- [Errno::ENOENT](file-not-found) — file or directory not found.
- [Errno::ECONNREFUSED](connection-refused) — connection refused.
- [IOError](io-error) — stream closed or invalid I/O.
