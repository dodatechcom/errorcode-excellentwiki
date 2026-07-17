---
title: "FileNotFoundException - file not found"
description: "Laravel throws FileNotFoundException when a required file does not exist at the expected path"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Laravel attempts to read, include, or require a file that does not exist at the specified path. It throws `Symfony\Component\Finder\Exception\FileNotFoundException`.

## Common Causes

- Configuration file missing from `config/` directory
- View template referenced but not created in `resources/views`
- Storage symlink not created (`php artisan storage:link`)
- Environment file `.env` missing or misconfigured
- Uploaded file path references a non-existent directory

## How to Fix

1. Ensure required config files exist:

```bash
# Re-publish config files
php artisan config:publish --all
```

2. Create missing storage symlink:

```bash
php artisan storage:link
```

3. Use `File::exists()` to check before accessing:

```php
use Illuminate\Support\Facades\File;

$path = storage_path('app/private/report.pdf');

if (!File::exists($path)) {
    abort(404, 'File not found');
}

return response()->file($path);
```

4. Verify `.env` file exists:

```bash
cp .env.example .env
php artisan key:generate
```

## Examples

```php
// Config file references a path that doesn't exist
$config = config('app.export_path'); // null if config key missing
$file = File::get($config); // FileNotFoundException
```

## Related Errors

- [Upload error]({{< relref "/frameworks/laravel/upload-error" >}})
- [Route not found]({{< relref "/frameworks/laravel/route-not-found3" >}})
