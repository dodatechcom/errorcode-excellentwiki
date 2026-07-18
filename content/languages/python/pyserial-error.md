---
title: "[Solution] Python PySerial Communication Error — How to Fix"
description: "Fix Python PySerial serial port errors. Resolve connection, timeout, and data format issues with PySerial."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python PySerial Communication Error

A PySerial error occurs when the serial port fails to open, read, or write data due to port configuration mismatches, permission issues, or hardware problems.

## Why It Happens

PySerial opens a serial port with specific baud rate, parity, and stop bits. Errors occur when the port doesn't exist, when another process has it open, or when the configured parameters don't match the connected device.

## Common Error Messages

- `serial.SerialException: could not open port`
- `serial.SerialTimeoutException: Read timeout`
- `ValueError: cannot configure port`
- `PermissionError: [Errno 13] could not open port`

## How to Fix It

### Fix 1: Handle port not found gracefully

```python
import serial.tools.list_ports
import serial

ports = serial.tools.list_ports.comports()
print([p.device for p in ports])

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
except serial.SerialException as e:
    print(f'Port error: {e}')
```

### Fix 2: Configure proper timeout

```python
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    timeout=2,
    write_timeout=2
)
```

### Fix 3: Use context manager for cleanup

```python
import serial

with serial.Serial('/dev/ttyUSB0', 9600) as ser:
    ser.write(b'AT\r\n')
    response = ser.readline()
    print(response.decode())
```

### Fix 4: Fix permission issues

```python
# Linux: add user to dialout group
# sudo usermod -a -G dialout $USER

import os
if os.name == 'posix':
    import stat
    mode = os.stat('/dev/ttyUSB0').st_mode
    print(f'Permissions: {oct(mode)}')
```

## Common Scenarios

- **Device not connected** — Serial port path exists but device is not responding.
- **Baud rate mismatch** — Data received is garbage due to wrong baud rate.
- **Permission denied** — User lacks permission to access the serial port device.

## Prevent It

- Always use try/except around serial.Serial() calls
- Use context managers (with statement) for proper port cleanup
- List available ports with serial.tools.list_ports before connecting

## Related Errors

- - [OSError](/languages/python/oserror/) — system call error
- - [FileNotFoundError](/languages/python/filenotfounderror/) — file not found
