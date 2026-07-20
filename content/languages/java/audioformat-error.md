---
title: "[Solution] Java AudioFormat — Audio Format Error"
description: "Fix Java AudioFormat errors by checking sample rate, verifying encoding, and handling format mismatches between source and target."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 44
---

# AudioFormat — Audio Format Error

Errors related to `AudioFormat` occur when audio parameters are invalid, when format conversions are unsupported, or when a line is opened with an incompatible format.

## Description

`javax.sound.sampled.AudioFormat` describes the encoding, sample rate, sample size, and channel count of audio data. Errors arise when attempting to use unsupported format combinations, when format parameters are zero or negative, or when converting between incompatible formats.

Common message variants:

- `IllegalArgumentException: invalid AudioFormat parameters`
- `LineUnavailableException: format not supported by mixer`
- `IllegalArgumentException: sample rate must be > 0`
- `UnsupportedAudioFileException: file format does not match`
- `IllegalArgumentException: bits per sample must be > 0`

## Common Causes

```java
// Cause 1: Zero sample rate
AudioFormat format = new AudioFormat(0, 16, 2, true, false);
// IllegalArgumentException — sample rate must be > 0

// Cause 2: Invalid encoding string
Encoding encoding = new Encoding("INVALID");
AudioFormat format = new AudioFormat(encoding, 44100, 16, 2, 4, 8, false, null);
// IllegalArgumentException — unknown encoding

// Cause 3: Negative sample size
AudioFormat format = new AudioFormat(AudioFormat.Encoding.PCM_SIGNED,
    44100, -1, 2, 4, 8, false, null);
// IllegalArgumentException — sample size must be > 0

// Cause 4: Format mismatch with audio file
AudioInputStream stream = AudioSystem.getAudioInputStream(new File("music.mp3"));
AudioFormat streamFormat = stream.getFormat();
SourceDataLine line = AudioSystem.getSourceDataLine(streamFormat);
line.open(streamFormat);  // LineUnavailableException — format not supported

// Cause 5: Incompatible format conversion
AudioFormat sourceFormat = new AudioFormat(AudioFormat.Encoding.PCM_SIGNED,
    44100, 16, 2, 4, 8, false, null);
AudioFormat targetFormat = new AudioFormat(AudioFormat.Encoding.PCM_FLOAT,
    96000, 32, 2, 8, 16, true, null);
// Conversion may fail — not all conversions supported
```

## Solutions

### Fix 1: Create AudioFormat with validated parameters

```java
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioSystem;

public class SafeAudioFormat {
    public static AudioFormat createFormat(
            float sampleRate, int sampleSizeInBits,
            int channels, boolean signed, boolean bigEndian) {
        if (sampleRate <= 0) {
            throw new IllegalArgumentException(
                "Sample rate must be > 0, got: " + sampleRate);
        }
        if (sampleSizeInBits <= 0 || sampleSizeInBits % 8 != 0) {
            throw new IllegalArgumentException(
                "Sample size must be > 0 and multiple of 8, got: " + sampleSizeInBits);
        }
        if (channels <= 0) {
            throw new IllegalArgumentException(
                "Channels must be > 0, got: " + channels);
        }

        return new AudioFormat(
            AudioFormat.Encoding.PCM_SIGNED,
            sampleRate, sampleSizeInBits, channels,
            (sampleSizeInBits / 8) * channels,  // frame size
            sampleRate,  // frame rate
            signed, bigEndian
        );
    }
}
```

### Fix 2: Convert format safely

```java
import javax.sound.sampled.*;
import java.io.File;
import java.io.IOException;

public class SafeFormatConverter {
    public static AudioInputStream convertFormat(
            AudioInputStream sourceStream,
            AudioFormat targetFormat) throws IllegalArgumentException {
        if (!AudioSystem.isConversionSupported(targetFormat, sourceStream.getFormat())) {
            throw new IllegalArgumentException(
                "Conversion not supported from " + sourceStream.getFormat()
                + " to " + targetFormat);
        }
        return AudioSystem.getAudioInputStream(targetFormat, sourceStream);
    }

    public static AudioFormat getStandardFormat() {
        return new AudioFormat(
            AudioFormat.Encoding.PCM_SIGNED,
            44100.0f, 16, 2, 4, 44100.0f, false
        );
    }
}
```

### Fix 3: Check format support before opening lines

```java
import javax.sound.sampled.*;

public class FormatChecker {
    public static boolean isFormatSupported(AudioFormat format) {
        DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);
        return AudioSystem.isLineSupported(info);
    }

    public static AudioFormat findSupportedFormat(AudioFormat[] formats) {
        for (AudioFormat format : formats) {
            if (isFormatSupported(format)) {
                return format;
            }
        }
        return null;
    }
}
```

### Fix 4: Get format from existing audio file

```java
import javax.sound.sampled.*;
import java.io.File;
import java.io.IOException;

public class FileFormatReader {
    public static AudioFormat getFormatFromFile(File audioFile)
            throws UnsupportedAudioFileException, IOException {
        AudioInputStream stream = AudioSystem.getAudioInputStream(audioFile);
        AudioFormat format = stream.getFormat();
        stream.close();
        return format;
    }
}
```

### Fix 5: Create format from AudioInputStream

```java
import javax.sound.sampled.*;
import java.io.File;
import java.io.IOException;

public class StreamFormatHelper {
    public static SourceDataLine createLineForStream(AudioInputStream stream)
            throws LineUnavailableException {
        AudioFormat format = stream.getFormat();
        DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);

        if (!AudioSystem.isLineSupported(info)) {
            // Try converting to standard format
            AudioFormat standard = new AudioFormat(
                AudioFormat.Encoding.PCM_SIGNED,
                44100.0f, 16, 2, 4, 44100.0f, false
            );
            info = new DataLine.Info(SourceDataLine.class, standard);
        }

        return (SourceDataLine) AudioSystem.getLine(info);
    }
}
```

## Prevention Checklist

- Always validate sample rate (> 0), sample size (> 0, multiple of 8), and channels (> 0).
- Check `AudioSystem.isLineSupported()` before opening a line with a given format.
- Use `AudioSystem.getAudioInputStream()` to get the correct format from an audio file.
- Verify format conversion is supported before calling `AudioSystem.getAudioInputStream(targetFormat, source)`.
- Use standard PCM_SIGNED 44100Hz 16-bit stereo as a safe default format.
- Handle `UnsupportedAudioFileException` when loading files of unknown types.

## Related Errors

- [LineUnavailableException](../lineunavailableexception) — audio line does not support format.
- [IllegalArgumentException](../illegalargumentexception) — invalid format parameters.
- [UnsupportedAudioFileException](../unsupportedaudiofileexception) — file format not recognized.
- [IOException](../ioerror) — audio file I/O error.
