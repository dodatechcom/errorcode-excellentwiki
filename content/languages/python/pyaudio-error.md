---
title: "[Solution] Python PyAudio Audio Stream Error — How to Fix"
description: "Fix Python PyAudio stream errors. Resolve audio device, format, and buffer issues with PyAudio for recording and playback."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python PyAudio Audio Stream Error

A PyAudio error occurs when audio streams fail to open, read, or write due to device unavailability, format mismatches, or buffer configuration problems.

## Why It Happens

PyAudio wraps PortAudio for cross-platform audio I/O. Errors occur when the audio device is busy, when the sample format doesn't match the device capabilities, or when the buffer size is too small.

## Common Error Messages

- `OSError: [Errno -9999] Unanticipated host error`
- `IOError: [Errno -9996] Input device not initialized`
- `ValueError: Sample format not supported`
- `OSError: Invalid number of channels`

## How to Fix It

### Fix 1: Check audio device availability

```python
import pyaudio

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f'{i}: {info["name"]} (in:{info["maxInputChannels"]}, out:{info["maxOutputChannels"]})')
p.terminate()
```

### Fix 2: Use correct audio format

```python
import pyaudio

p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    input=True,
    frames_per_buffer=1024
)
```

### Fix 3: Handle stream errors gracefully

```python
import pyaudio
import numpy as np

p = pyaudio.PyAudio()
try:
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True)
    data = stream.read(1024, exception_on_overflow=False)
    audio = np.frombuffer(data, dtype=np.float32)
except OSError as e:
    print(f'Audio error: {e}')
finally:
    stream.close()
    p.terminate()
```

### Fix 4: Use callback-based streaming

```python
import pyaudio

def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)

p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, channels=1, rate=44100,
    input=True, stream_callback=callback
)
stream.start_stream()
```

## Common Scenarios

- **Device busy** — Another application is using the microphone.
- **Unsupported format** — Requested sample rate not supported by device.
- **Buffer overflow** — Read loop too slow, causing data overflow.

## Prevent It

- Always close streams and terminate PyAudio when done
- Use exception_on_overflow=False for recording loops
- Query device capabilities before opening streams

## Related Errors

- - [OSError](/languages/python/oserror/) — system call error
- - [IOError](/languages/python/ioerror/) — input/output error
