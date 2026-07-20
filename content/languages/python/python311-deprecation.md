---
title: "[Solution] Python 3.11 Deprecation — asynchat/asyncore, distutils, locale Changes"
description: "Fix Python 3.11 deprecation errors from asynchat/asyncore removal, distutils deprecation, locale.resetlocale, and unittest finding patterns."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 503
---

# Python 3.11 Deprecation — asynchat/asyncore, distutils, locale Changes

Python 3.11 removes `asynchat` and `asyncore` entirely, deprecates `distutils`, changes locale defaults, and modifies unittest test discovery patterns. Code using these modules breaks immediately on upgrade.

## Common Causes

```python
# Cause 1: asynchat and asyncore removed
import asynchat
import asyncore

# Cause 2: distutils deprecated (removed in 3.12)
from distutils.core import setup
setup(name="my-package")

# Cause 3: locale.resetlocale removed
import locale
locale.resetlocale()

# Cause 4: unittest test discovery pattern changes
import unittest
loader = unittest.TestLoader()
suite = loader.loadTestsFromModule("tests")  # Pattern behavior changed

# Cause 5: sqlite3 default adapters changed
import sqlite3
conn = sqlite3.connect(":memory:")
# datetime adapter behavior changed
```

## How to Fix

### Fix 1: Replace asynchat/asyncore with asyncio

```python
# Wrong — asynchat/asyncore removed in 3.11
import asynchat
import asyncore

class EchoHandler(asynchat.async_chat):
    def __init__(self, sock):
        super().__init__(sock)
        self.set_terminator(b"\n")

    def found_terminator(self):
        self.push(self.get_data())

# Correct — use asyncio
import asyncio

async def handle_client(reader, writer):
    while True:
        data = await reader.readline()
        if not data:
            break
        writer.write(data)
        await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())
```

### Fix 2: Migrate from distutils to setuptools

```python
# Wrong — distutils deprecated in 3.11, removed in 3.12
from distutils.core import setup, Extension

# Correct — use setuptools
from setuptools import setup, Extension, find_packages

setup(
    name="my-extension",
    version="1.0",
    ext_modules=[
        Extension("mymodule", ["mymodule.c"]),
    ],
)

# Or migrate to pyproject.toml entirely:
# [build-system]
# requires = ["setuptools>=64"]
# build-backend = "setuptools.backends._legacy:_Backend"
```

### Fix 3: Remove locale.resetlocale calls

```python
# Wrong — locale.resetlocale removed in 3.11
import locale
locale.setlocale(locale.LC_ALL, "")
locale.resetlocale()

# Correct — just use setlocale without reset
import locale
locale.setlocale(locale.LC_ALL, "")
# Or set explicit locale
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
```

### Fix 4: Update unittest discovery patterns

```python
# Wrong — old discovery pattern
import unittest
loader = unittest.TestLoader()
suite = loader.loadTestsFromModule("tests.test_module")

# Correct — use importlib or explicit module import
import unittest
import importlib
test_module = importlib.import_module("tests.test_module")
loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_module)
```

## Examples

```python
# Full migration of an asyncore-based server to asyncio
# Old code:
# import asyncore, asynchat
#
# class Handler(asynchat.async_chat):
#     def __init__(self, sock):
#         super().__init__(sock)
#         self.buffer = b""
#     def collect_incoming_data(self, data):
#         self.buffer += data
#     def found_terminator(self):
#         self.push(b"Echo: " + self.buffer)
#         self.buffer = b""
#
# class Server(asyncore.dispatcher):
#     def __init__(self, port):
#         asyncore.dispatcher.__init__(self)
#         self.create_socket()
#         self.bind(("", port))
#         self.listen(5)
#     def handle_accept(self):
#         pair = self.accept()
#         if pair:
#             Handler(pair[0])

# New code using asyncio:
import asyncio

async def echo_handler(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"New connection from {addr}")
    while True:
        data = await reader.read(1024)
        if not data:
            break
        writer.write(b"Echo: " + data)
        await writer.drain()
    writer.close()
    await writer.wait_closed()

async def run_server():
    server = await asyncio.start_server(echo_handler, "127.0.0.1", 8888)
    async with server:
        await server.serve_forever()

asyncio.run(run_server())

# Locale migration
# Old:
# import locale
# locale.setlocale(locale.LC_ALL, "")
# locale.resetlocale()  # Removed in 3.11

# New:
import locale
locale.setlocale(locale.LC_ALL, "")
# Resetlocale is no longer needed — setlocale is sufficient
```

## Related Errors

- [python312-deprecation](../python312-deprecation) — Python 3.12 removed distutils entirely
- [asyncio-error](../asyncio-error) — General asyncio errors
- [python-unittest-error](../python-unittest-error) — unittest issues
- [ImportError](../importerror) — Module not found after removal
