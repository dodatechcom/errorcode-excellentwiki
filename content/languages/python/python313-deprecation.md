---
title: "[Solution] Python 3.13 Deprecation — asyncio, typing, cgi/cgitb Removal"
description: "Fix Python 3.13 deprecation errors from asyncio changes, typing updates, cgi/cgitb removal, aifc/audioop removal, and more."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 502
---

# Python 3.13 Deprecation — asyncio, typing, cgi/cgitb Removal

Python 3.13 removes several legacy modules including `cgi`, `cgitb`, `aifc`, `audioop`, `chunk`, and `binhex`. It also deprecates parts of `asyncio` and `typing` that relied on older patterns.

## Common Causes

```python
# Cause 1: cgi module removed
import cgi
form = cgi.FieldStorage()

# Cause 2: cgitb module removed
import cgitb
cgitb.enable()

# Cause 3: aifc and audioop modules removed
import aifc
import audioop

# Cause 4: chunk module removed
import chunk

# Cause 5: binhex module removed
import binhex
```

## How to Fix

### Fix 1: Replace cgi with urllib.parse or email

```python
# Wrong — cgi module removed in 3.13
import cgi
form = cgi.FieldStorage()
value = form.getvalue("name")

# Correct — use urllib.parse for URL query strings
from urllib.parse import parse_qs, urlparse
parsed = urlparse("http://example.com?name=hello")
params = parse_qs(parsed.query)
value = params.get("name", [None])[0]

# For multipart form data, use multipart or python-multipart
# pip install python-multipart
from multipart import parse_form_data
```

### Fix 2: Replace cgitb with logging or traceback

```python
# Wrong — cgitb module removed
import cgitb
cgitb.enable(display=0, logdir="/tmp/logs")

# Correct — use logging with traceback
import logging
import traceback

logging.basicConfig(filename="/tmp/error.log", level=logging.DEBUG)

try:
    risky_operation()
except Exception:
    logging.error("Exception occurred", exc_info=True)
```

### Fix 3: Replace aifc/audioop with wave or pydub

```python
# Wrong — aifc and audioop removed
import aifc
aif = aifc.open("sound.aif", "rb")

import audioop
result = audioop.add(b"data1", b"data2", 2)

# Correct — use wave module for WAV files
import wave
with wave.open("sound.wav", "rb") as wf:
    frames = wf.readframes(wf.getnframes())

# For audio processing, use pydub
# pip install pydub
from pydub import AudioSegment
audio = AudioSegment.from_file("sound.wav")
```

### Fix 4: Replace cgi.parse_header and cgi.parse_multipart

```python
# Wrong — cgi.parse_header removed
import cgi
content_type = "text/html; charset=utf-8"
mime, params = cgi.parse_header(content_type)

# Correct — parse manually or use email module
from email.message import Message
m = Message()
m["Content-Type"] = content_type
charset = m.get_param("charset", "utf-8")

# For multipart parsing
# pip install python-multipart
from multipart.multipart import parse_options_header
content_type_bytes = content_type.encode()
content_type_parsed, options = parse_options_header(content_type_bytes)
```

### Fix 5: Update asyncio deprecated APIs

```python
# Wrong — deprecated asyncio APIs in 3.13
import asyncio

async def old_style():
    loop = asyncio.get_event_loop()  # Deprecated
    await loop.create_task(some_coroutine())

# Correct — use modern asyncio
async def new_style():
    result = await some_coroutine()  # Direct await
    # Or use asyncio.run() for entry points
    # asyncio.run(main())
```

## Examples

```python
# Migrating a CGI script to WSGI/ASGI
# Old CGI approach (broken in 3.13):
# import cgi
# form = cgi.FieldStorage()
# print("Content-Type: text/html")
# print()
# print(f"<h1>Hello {form.getvalue('name')}</h1>")

# Modern approach with Flask:
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    name = request.args.get("name", "World")
    return f"<h1>Hello {name}</h1>"

# Audio file processing migration
# Old:
# import aifc, audioop
# f = aifc.open("file.aif")
# raw = f.readframes(f.getnframes())
# vol = audioop.rms(raw, 2)

# New:
import wave
import struct
with wave.open("file.wav", "rb") as wf:
    raw = wf.readframes(wf.getnframes())
    samples = struct.unpack(f"<{len(raw)//2}h", raw)
    rms = (sum(s**2 for s in samples) / len(samples)) ** 0.5
```

## Related Errors

- [ImportError](../importerror) — Module not found when removed modules are imported
- [python312-deprecation](../python312-deprecation) — Python 3.12 deprecation changes
- [python311-deprecation](../python311-deprecation) — Python 3.11 deprecation changes
- [DeprecationWarning](../deprecationwarning) — General deprecation warnings
