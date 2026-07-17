---
title: "File not found in Laravel"
description: "Laravel throws FileNotFoundException or FilesystemNotFoundException when a referenced file does not exist"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Laravel tries to read, write, or reference a file that does not exist on disk. It is thrown by the Filesystem component when the path is invalid or the file is missing.

## Common Causes

- Incorrect file path in `Storage::get()` or `file_get_contents()`
- File was moved or deleted but reference remains
- Symlink points to a non-existent target
- Permission issue prevents file access
- Storage disk not configured correctly

## How to Fix

1. Check if the file exists before accessing it:

```php
use Illuminate\Support\Facades\Storage;

if (Storage::disk('local')->exists('file.txt')) {
    $content = Storage::disk('local')->get('file.txt');
} else {
    Log::error('File not found: file.txt');
}
```

2. Use absolute paths with `storage_path()` helper:

```php
$path = storage_path('app/public/exports/report.csv');

if (!file_exists($path)) {
    abort(404, 'Report file not found');
}
```

3. Verify storage link is created:

```bash
php artisan storage:link
```

4. Handle missing files in the exception handler:

```php
use Symfony\Component\Finder\Exception\FileNotFoundException;

public function register()
{
    $this->renderable(function (FileNotFoundException $e, $request) {
        return response()->json(['error' => 'File not found'], 404);
    });
}
```

## Examples

```php
// Download that handles missing file
Route::get('/download/{filename}', function ($filename) {
    $path = 'exports/' . $filename;

    if (!Storage::disk('public')->exists($path)) {
        abort(404, 'File not found');
    }

    return Storage::disk('public')->download($path);
});
```

## Related Errors

- [File upload validation error]({{< relref "/frameworks/laravel/laravel-upload-error-v2" >}})
- [Model not found]({{< relref "/frameworks/laravel/laravel-model-not-found-v2" >}})
