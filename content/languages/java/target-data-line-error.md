---
title: "[Solution] Java TargetDataLine — Audio Capture Buffer Error"
description: "Fix Java TargetDataLine errors by checking buffer size, handling buffer underflow, and verifying audio capture format."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 46
---

# TargetDataLine — Audio Capture Buffer Error

Errors related to `TargetDataLine` occur when the buffer underflows during capture, the line is not started before reading, or the capture format is not supported by the input device.

## Description

`TargetDataLine` is used for audio capture from a microphone or other input source. It reads audio data into a buffer that the application consumes. Errors arise when the application does not read data fast enough causing overflow, when the line is not started, or when the audio format is incompatible with the input device.

Common message variants:

- `IllegalStateException: line not open`
- `IllegalArgumentException: buffer underflow — data not available`
- `LineUnavailableException: capture format not supported`
- `NullPointerException: target data line not initialized`
- `IllegalArgumentException: read length exceeds available data`

## Common Causes

```java
// Cause 1: Reading from unopened line
TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info);
line.read(buffer, 0, buffer.length);  // IllegalStateException — not open

// Cause 2: Not starting the line before reading
line.open(format);
int bytesRead = line.read(buffer, 0, buffer.length);
// Returns 0 or blocks — forgot line.start()

// Cause 3: Buffer too small for continuous capture
byte[] smallBuffer = new byte[64];
line.start();
while (true) {
    int read = line.read(smallBuffer, 0, smallBuffer.length);
    // Data may overflow if processing takes too long
}

// Cause 4: Reading more data than available
line.start();
int available = line.available();
line.read(buffer, 0, available + 100);  // May block waiting for data

// Cause 5: Closing line during active capture
line.start();
new Thread(() -> {
    line.read(buffer, 0, buffer.length);
}).start();
line.close();  // Disrupts active read
```

## Solutions

### Fix 1: Properly open, start, read, and close

```java
import javax.sound.sampled.*;
import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class SafeAudioCapture {
    public static byte[] captureAudio(AudioFormat format, long durationMs)
            throws LineUnavailableException, IOException {
        DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);

        try (TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info)) {
            line.open(format);
            line.start();

            ByteArrayOutputStream out = new ByteArrayOutputStream();
            byte[] buffer = new byte[4096];

            long endTime = System.currentTimeMillis() + durationMs;
            while (System.currentTimeMillis() < endTime) {
                int bytesRead = line.read(buffer, 0, buffer.length);
                if (bytesRead > 0) {
                    out.write(buffer, 0, bytesRead);
                }
            }

            line.stop();
            return out.toByteArray();
        }
    }
}
```

### Fix 2: Use adequate buffer size

```java
import javax.sound.sampled.*;

public class BufferedCapture {
    public static void captureWithAdequateBuffer(AudioFormat format)
            throws LineUnavailableException {
        DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);

        try (TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info)) {
            // Request larger buffer for continuous capture
            int bufferSize = (int) (format.getFrameSize() * format.getFrameRate());
            line.open(format, bufferSize);

            line.start();

            byte[] readBuffer = new byte[bufferSize / 4];
            while (true) {
                int read = line.read(readBuffer, 0, readBuffer.length);
                if (read > 0) {
                    processAudioData(readBuffer, read);
                }
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    private static void processAudioData(byte[] data, int length) {
        // Process captured audio
    }
}
```

### Fix 3: Check available bytes before reading

```java
import javax.sound.sampled.TargetDataLine;

public class NonBlockingCapture {
    public static int readAvailable(TargetDataLine line, byte[] buffer,
                                     int offset, int maxLength) {
        int available = line.available();
        int toRead = Math.min(Math.min(available, maxLength), buffer.length - offset);

        if (toRead <= 0) {
            return 0;
        }

        return line.read(buffer, offset, toRead);
    }
}
```

### Fix 4: Capture with timeout

```java
import javax.sound.sampled.*;

public class TimeoutCapture {
    public static byte[] captureWithTimeout(
            AudioFormat format, long timeoutMs)
            throws LineUnavailableException, InterruptedException {
        DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);

        try (TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info)) {
            line.open(format);
            line.start();

            java.io.ByteArrayOutputStream out = new java.io.ByteArrayOutputStream();
            byte[] buffer = new byte[4096];
            long startTime = System.currentTimeMillis();

            while (System.currentTimeMillis() - startTime < timeoutMs) {
                int read = line.read(buffer, 0, buffer.length);
                if (read > 0) {
                    out.write(buffer, 0, read);
                }
            }

            line.stop();
            return out.toByteArray();
        }
    }
}
```

### Fix 5: Handle overflow gracefully

```java
import javax.sound.sampled.*;
import java.util.concurrent.LinkedBlockingQueue;

public class OverflowSafeCapture {
    private final LinkedBlockingQueue<byte[]> audioQueue = new LinkedBlockingQueue<>(100);
    private volatile boolean capturing = false;

    public void startCapture(AudioFormat format) throws LineUnavailableException {
        DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);
        TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info);

        line.open(format);
        line.start();
        capturing = true;

        Thread captureThread = new Thread(() -> {
            byte[] buffer = new byte[4096];
            while (capturing) {
                int read = line.read(buffer, 0, buffer.length);
                if (read > 0) {
                    byte[] data = new byte[read];
                    System.arraycopy(buffer, 0, data, 0, read);
                    if (!audioQueue.offer(data)) {
                        System.err.println("Audio buffer overflow — dropping data");
                    }
                }
            }
            line.stop();
            line.close();
        });
        captureThread.setDaemon(true);
        captureThread.start();
    }

    public void stopCapture() {
        capturing = false;
    }
}
```

## Prevention Checklist

- Always call `line.open()` then `line.start()` before reading audio data.
- Use a buffer size at least 4x the frame size for smooth capture.
- Read data continuously to prevent buffer overflow.
- Check `line.available()` before reading to avoid unnecessary blocking.
- Use try-with-resources to ensure the line is closed after capture.
- Handle the case where the line is closed during an active read.

## Related Errors

- [LineUnavailableException](../lineunavailableexception) — capture line not available.
- [IllegalStateException](../illegalstateexception) — line not open.
- [IllegalArgumentException](../illegalargumentexception) — read parameters invalid.
- [IOException](../ioerror) — audio stream error during capture.
