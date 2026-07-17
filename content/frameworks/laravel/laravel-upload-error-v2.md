---
title: "File upload validation error"
description: "Laravel throws ValidationException or UploadException when a file upload fails validation or exceeds limits"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a file upload fails Laravel's validation rules or hits a server-side upload limit. It is thrown as `Illuminate\Validation\ValidationException` or `Symfony\Component\HttpFoundation\Exception\UploadException`.

## Common Causes

- File exceeds `upload_max_filesize` PHP limit
- File exceeds Laravel's `max` validation rule
- Uploaded file MIME type does not match allowed types
- Missing or empty file field in the request
- Temporary upload directory is not writable

## How to Fix

1. Validate file uploads with proper rules:

```php
public function store(Request $request)
{
    $validated = $request->validate([
        'document' => 'required|file|max:10240|mimes:pdf,docx',
        'avatar' => 'required|image|max:2048',
    ]);

    $path = $request->file('document')->store('documents', 'public');
}
```

2. Increase PHP upload limits in `php.ini`:

```
upload_max_filesize = 20M
post_max_size = 25M
max_file_uploads = 20
```

3. Handle the upload error gracefully:

```php
try {
    $path = $request->file('avatar')->store('avatars', 'public');
} catch (\Exception $e) {
    Log::error('Upload failed: ' . $e->getMessage());
    return back()->withErrors(['avatar' => 'Upload failed. Please try again.']);
}
```

4. Use disk-level validation with the `Storage` facade:

```php
use Illuminate\Http\UploadedFile;

$file = $request->file('attachment');

if (!$file || !$file->isValid()) {
    return back()->withErrors(['attachment' => 'Upload failed']);
}
```

## Examples

```php
// Full upload validation example
$request->validate([
    'photo' => 'required|image|mimes:jpeg,png,jpg,gif|max:5120',
]);

$path = $request->file('photo')->storeOnDisk('public', 'photos');

// Multiple file upload
$request->validate([
    'files.*' => 'required|file|max:10240',
]);
```

## Related Errors

- [File not found in Laravel]({{< relref "/frameworks/laravel/laravel-file-not-found-v2" >}})
- [Validation failed]({{< relref "/frameworks/laravel/laravel-validation-error-v2" >}})
