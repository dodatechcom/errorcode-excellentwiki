---
title: "[Solution] FastAPI Query Parameter Error — How to Fix"
description: "Fix FastAPI query parameter errors. Resolve query string parsing, validation, and type conversion issues."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI query parameter error occurs when query string parameters are missing, invalid, or cannot be converted to the expected type.

## Why It Happens

Query parameter errors happen due to missing required parameters, type mismatches, validation constraint failures, or incorrect default values.

## Common Error Messages

```
missing 1 required positional argument: query parameter
```

```
ValueError: value is not a valid integer
```

```
fastapi.exceptions.QueryParameterError: Invalid query parameter
```

```
TypeError: default_value must be provided for optional parameters
```

## How to Fix It

### 1. Define Query Parameters

Use proper type annotations.

```python
from fastapi import Query

@app.get("/items/")
async def get_items(
    q: str = Query(..., min_length=1, max_length=50),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    return {"query": q, "skip": skip, "limit": limit}
```

### 2. Use Query Aliases

Rename parameters in the URL.

```python
@app.get("/items/")
async def get_items(
    item_name: str = Query(..., alias="item-name"),
    page_num: int = Query(1, alias="page")
):
    return {"name": item_name, "page": page_num}
```

### 3. Handle Optional Query Parameters

Make parameters optional with defaults.

```python
from typing import Optional

@app.get("/search/")
async def search(
    q: Optional[str] = None,
    category: Optional[str] = None,
    sort_by: str = Query("created_at", regex="^(name|price|created_at)$")
):
    filters = {"q": q, "category": category, "sort": sort_by}
    return filters
```

### 4. Validate Query Parameters

Add validation constraints.

```python
@app.get("/reports/")
async def get_report(
    start_date: str = Query(..., regex=r"\d{4}-\d{2}-\d{2}"),
    end_date: str = Query(..., regex=r"\d{4}-\d{2}-\d{2}"),
    format: str = Query("json", enum=["json", "csv", "pdf"])
):
    return {"start": start_date, "end": end_date, "format": format}
```

## Common Scenarios

**Scenario 1: Query returns unexpected results.**
Check that query parameter types match expected values.

**Scenario 2: Required parameter not provided.**
Use  for required parameters.

**Scenario 3: Parameter validation fails.**
Check regex patterns and enum values.

## Prevent It

1. **Use explicit type hints.**
Don't rely on auto-inference for query params.

2. **Add descriptions.**
Help API consumers understand parameter usage.

3. **Test parameter validation.**
Send requests with missing and invalid params.

