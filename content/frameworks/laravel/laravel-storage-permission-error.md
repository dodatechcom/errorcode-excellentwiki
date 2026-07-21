---
title: "[Solution] Laravel Storage Permission Denied Error"
description: "Fix Laravel file_put_contents permission denied. Resolve storage directory permission issues in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when the web server process does not have write access to the `storage` directory or its subdirectories.

## Common Causes

- `storage` directory is owned by a different user than the web server process
- Permission bits do not allow group or other write access
- `bootstrap/cache` directory has incorrect permissions
- SELinux or AppArmor policies block write access
- Docker container runs as a different user

## How to Fix

1. Set correct ownership and permissions:

```bash
chmod -R 775 storage bootstrap/cache
chown -R www-data:www-data storage bootstrap/cache
```

2. For shared hosting, use ACLs:

```bash
setfacl -R -m u:www-data:rwx storage bootstrap/cache
setfacl -R -d -m u:www-data:rwx storage bootstrap/cache
```

3. Verify in a helper script:

```php
$paths = [storage_path(), base_path('bootstrap/cache')];
foreach ($paths as $path) {
    $writable = is_writable($path);
    echo "{$path}: " . ($writable ? 'writable' : 'NOT writable') . PHP_EOL;
}
```

4. For Docker, ensure the correct user runs the process:

```dockerfile
RUN chown -R www-data:www-data /var/www/html/storage /var/www/html/bootstrap/cache
```

## Examples

```php
// Log channel write fails
Log::info('Application started');
// RuntimeException: Unable to create configured logger. Unable to create directory

// File upload fails silently
$request->file('avatar')->store('avatars');
// Could not create directory: .../storage/app/public/avatars
```
