---
title: "[Solution] Java LineUnavailableException — Audio Line Cannot Be Opened"
description: "Fix Java LineUnavailableException by checking audio device availability, releasing other lines, and handling audio device conflicts."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 16
---

# LineUnavailableException — Audio Line Cannot Be Opened

A `LineUnavailableException` is thrown when an audio line (source data line, target data line, or clip) cannot be opened because the audio device is already in use, unavailable, or lacks sufficient resources.

## Description

Java Sound provides access to audio lines through `SourceDataLine`, `TargetDataLine`, and `Clip`. Each line requires exclusive access to an audio device. When multiple applications or threads attempt to use the same line simultaneously, or when the system has limited audio resources, `LineUnavailableException` is thrown.

Common message variants:

- `javax.sound.sampled.LineUnavailableException: line is not supported`
- `javax.sound.sampled.LineUnavailableException: mixer not supported`
- `javax.sound.sampled.LineUnavailableException: can't open line`
- `javax.sound.sampled.LineUnavailableException: line in use`

## Common Causes

```java
// Cause 1: Opening same line twice simultaneously
import javax.sound.sampled.*;
AudioFormat format = new AudioFormat(44100, 16, 2, true, false);
DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);

SourceDataLine line1 = (SourceDataLine) AudioSystem.getLine(info);
line1.open(format);
// line1 is still open

SourceDataLine line2 = (SourceDataLine) AudioSystem.getLine(info);
line2.open(format);  // LineUnavailableException — line already in use

// Cause 2: Unsupported audio format
AudioFormat badFormat = new AudioFormat(96000, 32, 8, true, false);
DataLine.Info badInfo = new DataLine.Info(SourceDataLine.class, badFormat);
SourceDataLine line = (SourceDataLine) AudioSystem.getLine(badInfo);
line.open(badFormat);  // LineUnavailableException — unsupported format

// Cause 3: No audio device available
// On headless server with no sound card
DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);
SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);
// LineUnavailableException — no mixer available

// Cause 4: Clip limit exceeded
Clip[] clips = new Clip[100];
for (int i = 0; i < clips.length; i++) {
    clips[i] = AudioSystem.getClip();
    clips[i].open(AudioSystem.getAudioInputStream(new File("sound.wav")));
    // LineUnavailableException after system Clip limit
}
```

## Solutions

### Fix 1: Ensure lines are properly closed

```java
import javax.sound.sampled.*;

SourceDataLine line = null;
try {
    AudioFormat format = new AudioFormat(44100, 16, 2, true, false);
    DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);
    line = (SourceDataLine) AudioSystem.getLine(info);
    line.open(format);

    // Use the line...
    byte[] buffer = new byte[1024];
    line.write(buffer, 0, buffer.length);

} catch (LineUnavailableException e) {
    System.err.println("Audio line unavailable: " + e.getMessage());
} finally {
    if (line != null && line.isOpen()) {
        line.drain();
        line.close();
    }
}
```

### Fix 2: Use try-with-resources for auto-close

```java
import javax.sound.sampled.*;

public class SafeAudioPlayer {
    public static void playSound(AudioInputStream audioStream) {
        AudioFormat format = audioStream.getFormat();
        DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);

        try (SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info)) {
            line.open(format);
            line.start();

            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = audioStream.read(buffer)) != -1) {
                line.write(buffer, 0, bytesRead);
            }

            line.drain();
            line.stop();
        } catch (LineUnavailableException e) {
            System.err.println("Audio line unavailable: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Audio I/O error: " + e.getMessage());
        }
    }
}
```

### Fix 3: Use synchronized access for shared lines

```java
import javax.sound.sampled.*;
import java.util.concurrent.locks.ReentrantLock;

public class ThreadSafeAudioPlayer {
    private final ReentrantLock lock = new ReentrantLock();
    private SourceDataLine currentLine;

    public void play(AudioInputStream stream) {
        lock.lock();
        try {
            AudioFormat format = stream.getFormat();
            DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);

            if (currentLine == null || !currentLine.isOpen()) {
                currentLine = (SourceDataLine) AudioSystem.getLine(info);
                currentLine.open(format);
            }

            currentLine.start();
            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = stream.read(buffer)) != -1) {
                currentLine.write(buffer, 0, bytesRead);
            }
            currentLine.drain();
            currentLine.stop();

        } catch (LineUnavailableException e) {
            System.err.println("Audio device unavailable: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Playback error: " + e.getMessage());
        } finally {
            lock.unlock();
        }
    }

    public void close() {
        lock.lock();
        try {
            if (currentLine != null && currentLine.isOpen()) {
                currentLine.drain();
                currentLine.close();
            }
        } finally {
            lock.unlock();
        }
    }
}
```

### Fix 4: Check available mixers before opening

```java
import javax.sound.sampled.*;

public class AudioDeviceChecker {
    public static void listAvailableMixers() {
        Mixer.Info[] mixers = AudioSystem.getMixerInfo();

        System.out.println("Available audio mixers:");
        for (Mixer.Info mixer : mixers) {
            System.out.println("  " + mixer.getName());
            System.out.println("    Vendor: " + mixer.getVendor());
            System.out.println("    Version: " + mixer.getVersion());
        }
    }

    public static boolean canOpenLine(AudioFormat format) {
        try {
            DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);
            if (!AudioSystem.isLineSupported(info)) {
                return false;
            }
            SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);
            line.open(format);
            line.close();
            return true;
        } catch (LineUnavailableException e) {
            return false;
        }
    }
}
```

### Fix 5: Handle audio conflicts gracefully

```java
import javax.sound.sampled.*;

public class ResilientAudioPlayer {
    public void playWithRetry(AudioInputStream stream, int maxRetries) {
        for (int attempt = 1; attempt <= maxRetries; attempt++) {
            try {
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
                    line.drain();
                    return;  // Success
                }
            } catch (LineUnavailableException e) {
                System.err.println("Attempt " + attempt + " failed: " + e.getMessage());
                if (attempt < maxRetries) {
                    try {
                        Thread.sleep(1000);  // Wait before retry
                    } catch (InterruptedException ie) {
                        Thread.currentThread().interrupt();
                        return;
                    }
                }
            } catch (IOException e) {
                System.err.println("Audio I/O error: " + e.getMessage());
                return;
            }
        }
        System.err.println("All " + maxRetries + " attempts failed");
    }
}
```

## Prevention Checklist

- Always close audio lines when done (use try-with-resources).
- Use `AudioSystem.isLineSupported()` before attempting to open a line.
- Avoid opening multiple lines on the same mixer simultaneously.
- Use locks or synchronized blocks when multiple threads access audio.
- Handle `LineUnavailableException` with retry logic for critical audio.
- Release audio resources promptly in application shutdown hooks.

## Related Errors

- [MidiUnavailableException](../midiunavailableexception) — MIDI device unavailable.
- [IllegalArgumentException](../illegalargumentexception) — unsupported audio format.
- [IOException](../ioexception) — audio file I/O error.
