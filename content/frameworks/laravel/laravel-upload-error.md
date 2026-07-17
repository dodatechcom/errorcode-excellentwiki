---
title: "UploadedFile error - upload failed"
description: "Laravel throws UploadedFile error when file upload fails due to size limits or validation rules"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["upload", "file", "validation", "storage", "request"]
weight: 5
---

This error occurs when a file upload fails in Laravel due to PHP upload limits, validation failures, or storage issues. It throws exceptions related to `UploadedFile` or validation errors.

## Common Causes

- File exceeds PHP `upload_max_filesize` or `post_max_size` limits
- File does not pass Laravel validation rules (mimetypes, size)
- Storage directory is not writable
- Temporary upload directory is full
- Multipart form encoding issue

## How to Fix

1. Configure PHP upload limits in `php.ini`:

```ini
upload_max_filesize = 10M
post_max_size = 12M
```

2. Validate uploaded files properly:

```php
public function store(Request $request)
{
    $validated = $request->validate([
        'document' => 'required|file|mimes:pdf,doc,docx|max:10240',
        'avatar' => 'required|image|mimes:jpeg,png,jpg|max:2048',
    ]);

    $path = $request->file('document')->store('documents');
    return response()->json(['path' => $path]);
}
```

3. Use chunked uploads for large files:

```php
public function uploadLargeFile(Request $request)
{
    $file = $request->file('large_file');
    $chunks = 5;
    $chunkSize = ceil($file->getSize() / $chunks);

    // Process chunks...
}
```

## Examples

```php
$request->validate(['file' => 'required|file|max:5120']);
// ValidationException: The file must not be greater than 5120 kilobytes.
```

## Related Errors

- [File not found]({{< relref "/frameworks/laravel/file-not-found" >}})
- [Validation error]({{< relref "/frameworks/laravel/validation-error2" >}})
