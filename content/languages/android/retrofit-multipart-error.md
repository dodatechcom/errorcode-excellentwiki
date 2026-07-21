---
title: "Retrofit Multipart Upload Error"
description: "Fix Retrofit multipart file upload errors for image and document uploads"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
File upload fails because of incorrect multipart form data configuration

## Common Causes

- @Multipart annotation missing on interface method
- File not wrapped in RequestBody or MultipartBody.Part
- Content-Type not set on file part
- File URI does not point to accessible file

## Fixes

- Add @Multipart annotation to upload method
- Use MultipartBody.Part.createFormData for files
- Set correct MediaType on RequestBody
- Ensure file URI is readable by app

## Code Example

```kotlin
@Multipart
@POST("upload")
suspend fun uploadFile(
    @Part file: MultipartBody.Part,
    @Part("description") description: RequestBody
): UploadResponse

// Creating the parts:
val file = File(context.cacheDir, "photo.jpg")
val requestBody = file.asRequestBody("image/jpeg".toMediaTypeOrNull())
val filePart = MultipartBody.Part.createFormData(
    "file", file.name, requestBody
)
val descPart = "Profile photo".toRequestBody("text/plain".toMediaTypeOrNull())
```

# Get content URI file path:
val inputStream = contentResolver.openInputStream(uri)
val file = File(cacheDir, "upload.tmp")
file.outputStream().use { inputStream?.copyTo(it) }
