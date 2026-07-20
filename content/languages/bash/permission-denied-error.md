---
title: "[Solution] Bash Permission Denied Error"
description: "Fix 'bash: permission denied' when trying to execute a script or access a file without proper permissions."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "command", "permissions", "chmod", "execute"]
severity: "error"
---

# Permission Denied

## Error Message

```
bash: ./script.sh: Permission denied
```

## Common Causes

- The script or file does not have execute (`+x`) permission
- The current user is not the file owner and lacks the required permission bits
- A directory in the path lacks execute permission (needed to traverse it)
- SELinux or AppArmor policies are blocking execution

## Solutions

### Solution 1: Add Execute Permission to the Script

Use `chmod` to add execute permission for the user, group, or all users as appropriate.

```bash
# Check current permissions
ls -la script.sh

# Add execute permission for owner
chmod +x script.sh

# Add execute for owner, read+execute for group and others
chmod 755 script.sh

# Make a script executable by everyone (use with caution)
chmod a+x script.sh 
```

### Solution 2: Run the Script with bash Explicitly

If you don't want to change permissions, run the script by passing it to `bash` as an argument instead of executing it directly.

```bash
# Instead of
./script.sh

# Run with bash directly (no +x needed)
bash script.sh

# Or use sh for POSIX-compatible scripts
sh script.sh

# Run with sudo if you need root privileges
sudo ./script.sh 
```

## Prevention Tips

- Use `ls -la` to check file permissions before executing
- Only add `+x` to files you trust — never to untrusted scripts
- Use `chmod 700` for personal scripts to restrict access to only the owner

## Related Errors

- [Command Not Found]({< relref "/languages/bash/command-not-found-error" >})
- [No Such File]({< relref "/languages/bash/no-such-file" >})
