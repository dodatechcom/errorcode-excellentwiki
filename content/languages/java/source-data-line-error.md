---
title: "[Solution] Java SourceDataLine — Audio Playback Buffer Error"
description: "Fix Java SourceDataLine errors by checking buffer size, handling buffer overflow, and verifying audio format compatibility."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 45
---

# SourceDataLine — Audio Playback Buffer Error

Errors related to `SourceDataLine` occur when the buffer is overflowed, the line is not opened before writing, or the audio format is incompatible with the output device.

## Description

`SourceDataLine` is used for audio playback. It buffers audio data before sending it to the output device. Errors arise when data is written faster than it is consumed (overflow), when the line is not opened or started, or when the buffer size is insufficient for the audio stream.

Common message variants:

- `IllegalArgumentException: overflow in SourceDataLine.write`
- `IllegalStateException: line not open`
- `IllegalArgumentException: number of bytes does not match frame size`
- `LineUnavailableException: line not supported`
- `NullPointerException: line not initialized`

## Common Causes

```java
// Cause 1: Writing to unopened line
SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);
line.write(data, 0, data.length);  // IllegalStateException — not open

// Cause 2: Buffer size mismatch
SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);
line.open(format, 1024);  // Small buffer
line.write(data, 0, data.length);  // May block if data exceeds buffer

// Cause 3: Writing odd number of bytes for stereo 16-bit audio
byte[] oddData = new byte[1023];  // Not multiple of frame size (4 bytes)
line.write(oddData, 0, oddData.length);  // IllegalArgumentException

// Cause 4: Not calling start() after open()
line.open(format);
line.write(data, 0, data.length);
// Data queued but not playing — forgot line.start()

// Cause 5: Closing line while write is in progress
new Thread(() -> {
    line.write(data, 0, data.length);
}).start();
line.close();  // Disrupts write — IllegalStateException
```

## Solutions

### Fix 1: Properly open, start, write, and close

```java
import javax.sound.sampled.*;

public class SafeAudioPlayback {
    public static void playAudio(AudioInputStream stream) throws Exception {
        AudioFormat format = stream.getFormat();
        DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);

        try (SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info)) {
            line.open(format);
            line.start();

            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = stream.read(buffer)) != -1) {
                line.write(buffer, 0, bytesRead);
            }

            line.drain();   // Wait for all data to be played
            line.stop();
        }
    }
}
```

### Fix 2: Use appropriate buffer size

```java
import javax.sound.sampled.*;

public class BufferedPlayback {
    public static void playWithBuffer(AudioInputStream stream)
            throws LineUnavailableException, java.io.IOException {
        AudioFormat format = stream.getFormat();
        DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);

        SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);

        // Calculate buffer size: at least 4x the frame size
        int bufferSize = format.getFrameSize() * (int) format.getFrameRate() / 10;
        bufferSize = Math.max(bufferSize, line.getBufferSize());

        line.open(format, bufferSize);
        line.start();

        byte[] buffer = new byte[bufferSize];
        int bytesRead;
        while ((bytesRead = stream.read(buffer)) != -1) {
            line.write(buffer, 0, bytesRead);
        }

        line.drain();
        line.stop();
        line.close();
    }
}
```

### Fix 3: Validate frame size before writing

```java
import javax.sound.sampled.AudioFormat;

public class FrameSizeValidator {
    public static int validateAndWrite(
            javax.sound.sampled.SourceDataLine line,
            byte[] data, int offset, int length,
            AudioFormat format) {
        int frameSize = format.getFrameSize();

        if (length % frameSize != 0) {
            length = (length / frameSize) * frameSize;
            System.err.println("Warning: truncated to frame boundary: " + length);
        }

        if (offset + length > data.length) {
            throw new IllegalArgumentException(
                "Data array too small: need " + (offset + length)
                + ", got " + data.length);
        }

        return line.write(data, offset, length);
    }
}
```

### Fix 4: Monitor buffer available space

```java
import javax.sound.sampled.*;

public class MonitoredPlayback {
    public static void playSafe(AudioInputStream stream) throws Exception {
        AudioFormat format = stream.getFormat();
        DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);

        try (SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info)) {
            line.open(format);
            line.start();

            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = stream.read(buffer)) != -1) {
                // Wait until buffer has space
                while (line.available() < bytesRead) {
                    Thread.sleep(10);
                }
                line.write(buffer, 0, bytesRead);
            }

            line.drain();
            line.stop();
        }
    }
}
```

### Fix 5: Handle interruption during playback

```java
import javax.sound.sampled.*;

public class InterruptiblePlayback {
    private volatile boolean playing = false;

    public void play(AudioInputStream stream) throws Exception {
        AudioFormat format = stream.getFormat();
        DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);
        SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);

        playing = true;
        line.open(format);
        line.start();

        try {
            byte[] buffer = new byte[4096];
            int bytesRead;
            while (playing && (bytesRead = stream.read(buffer)) != -1) {
                line.write(buffer, 0, bytesRead);
            }
        } finally {
            line.drain();
            line.stop();
            line.close();
            playing = false;
        }
    }

    public void stop() {
        playing = false;
    }
}
```

## Prevention Checklist

- Always call `line.open()` then `line.start()` before writing.
- Use `line.drain()` after the last write to ensure all data is played.
- Set buffer size to at least 4x the frame size for smooth playback.
- Ensure write length is a multiple of `format.getFrameSize()`.
- Close the line in a finally block to prevent resource leaks.
- Check `line.available()` before writing to avoid buffer overflow blocking.

## Related Errors

- [LineUnavailableException](../lineunavailableexception) — audio line not available.
- [IllegalStateException](../illegalstateexception) — line not open.
- [IllegalArgumentException](../illegalargumentexception) — write length not frame-aligned.
- [IOException](../ioerror) — audio stream read error.
