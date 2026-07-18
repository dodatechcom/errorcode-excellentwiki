---
title: "[Solution] Python PyAudio Stream Error — How to Fix"
description: "Fix Python PyAudio errors. Resolve device, format, and buffer issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python PyAudio Stream Error

A `OSError: Unanticipated host error` occurs when Audio streaming fails due to device unavailability, format mismatches, or buffer issues..

## Why It Happens

This happens when audio device is busy, sample format unsupported, or buffer too small. Python enforces strict type and state checking.

## Common Error Messages

- `Unanticipated host error`
- `Input device not initialized`
- `Sample format not supported`

## How to Fix It

### Fix 1: Check devices

```python
import pyaudio
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f'{i}: {info["name"]}')
```

### Fix 2: Correct format

```python
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True)
```

### Fix 3: Handle overflow

```python
data = stream.read(1024, exception_on_overflow=False)
```

### Fix 4: Callback streaming

```python
def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, stream_callback=callback)
```

## Common Scenarios

- **Device busy** — Another app is using the microphone.
- **Unsupported format** — Sample rate not supported by device.
- **Buffer overflow** — Read loop too slow causes overflow.

## Prevent It

- Always close streams when done
- Use exception_on_overflow=False
- Query device capabilities first

## Related Errors

- - [OSError](/languages/python/oserror/) — system call error
- - [IOError](/languages/python/ioerror/) — I/O error
