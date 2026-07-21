---
title: "[Solution] FastAPI Upload Multiple Files Error"
description: "Fix FastAPI multiple file upload errors when form data contains several files and parsing fails."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

When uploading multiple files through FastAPI, the endpoint fails if the parameter type does not correctly handle multiple file parts.

## Common Causes

- Using `UploadFile` instead of `list[UploadFile]` for multiple files
- Client sends files under different form field names
- File size exceeds the configured maximum
- Content-Type header is missing or incorrect
- Files are sent as separate requests instead of a single multipart form

## How to Fix

### Accept Multiple Files

```python
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload-multiple")
async def upload_files(files: list[UploadFile] = File(...)):
    results = []
    for file in files:
        content = await file.read()
        results.append({"filename": file.filename, "size": len(content)})
    return {"files": results}
```

### Handle Mixed Form Data

```python
from fastapi import FastAPI, File, Form, UploadFile

@app.post("/upload-with-metadata")
async def upload_with_metadata(
    description: str = Form(...),
    files: list[UploadFile] = File(...),
):
    return {
        "description": description,
        "count": len(files),
        "filenames": [f.filename for f in files],
    }
```

## Examples

```python
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# Bug -- only accepts one file
@app.post("/wrong")
async def wrong_upload(file: UploadFile = File(...)):
    return {"filename": file.filename}

# Correct -- accepts multiple files
@app.post("/correct")
async def correct_upload(files: list[UploadFile] = File(...)):
    return {"count": len(files)}
```

The client must send the request as `multipart/form-data` with the field name matching the parameter name.
