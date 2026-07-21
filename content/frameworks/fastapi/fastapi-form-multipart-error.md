---
title: "[Solution] FastAPI Form Multipart Error"
description: "Fix FastAPI multipart form data errors when form fields are missing or content type is incorrect."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

When FastAPI receives a multipart form request, it fails if the content type header is missing or form fields do not match the endpoint parameters.

## Common Causes

- Client sends `application/json` instead of `multipart/form-data`
- Form boundary is missing or malformed in the Content-Type header
- File field name in the form does not match the parameter name
- Request body is too large for the default parser
- Using `Form(...)` without `File(...)` for file uploads

## How to Fix

### Set Correct Content Type

```python
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.post("/upload")
async def upload(
    name: str = Form(...),
    file: UploadFile = File(...),
):
    return {"name": name, "filename": file.filename}
```

## Examples

```bash
curl -X POST http://localhost:8000/profile \
  -F "username=alice" \
  -F "avatar=@photo.jpg"
```

Using `-d` (JSON body) instead of `-F` will fail with a 422 error.
