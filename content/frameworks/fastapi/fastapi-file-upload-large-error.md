---
title: "[Solution] FastAPI File Upload Large File Error"
description: "Fix FastAPI large file upload errors when uploads fail due to size limits or memory constraints."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

When uploading large files to FastAPI, the request fails if the file exceeds the maximum body size or if the entire file is loaded into memory.

## Common Causes

- File exceeds the default 1MB body size limit in Starlette
- Entire file loaded into memory instead of streaming to disk
- Request timeout before upload completes
- Disk space insufficient for temporary upload files
- Content-Length header missing

## How to Fix

### Stream Upload to Disk

```python
from fastapi import FastAPI, UploadFile
import shutil

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "size": file.size}
```

### Set Upload Directory

```python
from fastapi import FastAPI, File, UploadFile
from pathlib import Path

app = FastAPI()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload-large")
async def upload_large(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as f:
        while chunk := await file.read(1024 * 1024):
            f.write(chunk)
    return {"filename": file.filename, "path": str(file_path)}
```

## Examples

```python
from fastapi import FastAPI, UploadFile

app = FastAPI()

# Bug -- loads entire file into memory
@app.post("/bad-upload")
async def bad_upload(file: UploadFile):
    content = await file.read()  # Loads entire file into RAM
    return {"size": len(content)}

# Fix -- stream in chunks
@app.post("/good-upload")
async def good_upload(file: UploadFile):
    total = 0
    while chunk := await file.read(8192):
        total += len(chunk)
    return {"size": total}
```
