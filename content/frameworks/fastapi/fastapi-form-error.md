---
title: "[Solution] FastAPI Form Error — How to Fix"
description: "Fix FastAPI form data errors. Resolve form parsing, validation, and encoding issues."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI form error occurs when form data cannot be parsed, validated, or processed correctly.

## Why It Happens

Form errors happen due to incorrect content type headers, missing form fields, encoding issues, or mismatched types.

## Common Error Messages

```
ValueError: Field required
```

```
StarletteHTTPException: 422 Validation Error
```

```
TypeError: 'NoneType' object is not subscriptable
```

```
UnicodeDecodeError: 'utf-8' codec can't decode byte
```

## How to Fix It

### 1. Handle Form Data

Use FastAPI's Form class.

```python
from fastapi import Form

@app.post('/login/')
async def login(username: str = Form(...), password: str = Form(...)):
    user = authenticate(username, password)
    if user:
        return {'message': 'Logged in'}
    raise HTTPException(status_code=401)
```

### 2. Combine File and Form Data

Handle mixed uploads.

```python
from fastapi import Form, File, UploadFile

@app.post('/create/')
async def create(
    name: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...)
):
    contents = await file.read()
```

### 3. Validate Form Fields

Add validation to form inputs.

```python
@app.post('/register/')
async def register(
    username: str = Form(...),
    email: str = Form(...),
    age: int = Form(...)
):
    user = UserForm(username=username, email=email, age=age)
    return user.dict()
```

### 4. Handle Form Encoding

Process with proper encoding.

```python
@app.post('/submit/')
async def submit(data: str = Form(...)):
    decoded_data = data.encode('latin-1').decode('utf-8')
    return {'data': decoded_data}
```

## Common Scenarios

**Scenario 1: Form returns 422.**
Check Content-Type is `application/x-www-form-urlencoded`.

**Scenario 2: File upload field is None.**
Ensure form has `enctype="multipart/form-data"`.

**Scenario 3: Form data corrupted.**
Verify encoding matches accept-charset.

## Prevent It

1. **Use proper form encoding.**
Set `enctype` correctly in HTML.

2. **Validate server-side.**
Never trust client validation.

3. **Test all submissions.**
Test valid and invalid inputs.

