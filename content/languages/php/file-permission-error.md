---
title: "[Solution] PHP File Permission Error — Permission Denied"
description: "Fix PHP file permission errors. Resolve 'Permission denied' when reading, writing, or uploading files in PHP."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "filesystem", "permission"]
severity: "error"
---

# PHP File Permission Error

## Error Message

```
Permission denied: unable to open stream
```

## Common Causes

- The web server user (www-data, nginx, apache) does not own the file or directory
- File or directory permissions are too restrictive (e.g., 600 or 700 instead of 644/755)
- SELinux or AppArmor policies blocking PHP access to the path

## Solutions

### Solution 1: Fix File and Directory Permissions

Set correct ownership and permissions so the web server user can access the file.

```php
// Check current permissions before writing
$path = "/var/www/uploads/report.csv";
if (is_writable($path)) {
    file_put_contents($path, $data);
} else {
    // Log the issue — fix via terminal
    error_log("Cannot write to $path. Current perms: " . substr(sprintf('%o', fileperms($path)), -4));
}

// Terminal fix:
// sudo chown -R www-data:www-data /var/www/uploads
// sudo chmod -R 755 /var/www/uploads
// sudo chmod 644 /var/www/uploads/report.csv
```

### Solution 2: Use umask to Set Default Permissions

Set a umask before creating files so new files are created with the correct permissions automatically.

```php
<?php
// Set umask so new files are 644 and directories are 755
umask(0022);

// Now newly created files will be readable by the web server
$logFile = "/var/www/app/logs/app.log";
file_put_contents($logFile, date('Y-m-d H:i:s') . " App started\n");
echo "File permissions: " . substr(sprintf('%o', fileperms($logFile)), -4);
// Output: File permissions: 644
?>
```

## Prevention Tips

- Never run the web server as root in production
- Use 644 for files and 755 for directories as a baseline
- Check SELinux context with `ls -Z` on RHEL/CentOS systems

## Related Errors

- [File Not Found Error]({{< relref "/languages/php/file-not-found-error" >}})
- [File Write Error]({{< relref "/languages/php/file-write-error" >}})
