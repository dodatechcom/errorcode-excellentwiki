---
title: "[Solution] MATLAB audioread/audiowrite Error — Format, Sample Rate & Bit Depth"
description: "Fix MATLAB audioread/audiowrite errors for unsupported formats, sample rate mismatches, and bit depth issues with actionable code solutions."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 101
---

MATLAB's `audioread` and `audiowrite` functions handle audio I/O, but they can fail when the file format is unsupported, the sample rate is inconsistent, or the bit depth is invalid.

## Common Causes

- Attempting to read a file format not supported by the platform's codec library (e.g., `.flac`, `.opus`)
- Passing a sample rate to `audiowrite` that is not a positive scalar
- Using an unsupported `BitsPerSample` value in `audiowrite`
- Providing a file path that does not exist or has incorrect permissions
- Reading multi-channel audio but expecting a mono vector

## How to Fix

### Solution 1: Validate file existence and format before reading

```matlab
filename = 'recording.wav';
if ~isfile(filename)
    error('File not found: %s', filename);
end
[y, Fs] = audioread(filename);
disp(['Sample rate: ', num2str(Fs), ' Hz']);
disp(['Duration: ', num2str(length(y)/Fs), ' seconds']);
```

### Solution 2: Convert sample rate when writing

```matlab
[y, Fs] = audioread('input.wav');
targetFs = 44100;
if Fs ~= targetFs
    y = resample(y, targetFs, Fs);
    Fs = targetFs;
end
audiowrite('output.wav', y, Fs, 'BitsPerSample', 16);
```

### Solution 3: Handle different bit depths

```matlab
% Write with specific bit depth
audiowrite('output_16.wav', y, Fs, 'BitsPerSample', 16);
audiowrite('output_24.wav', y, Fs, 'BitsPerSample', 24);
audiowrite('output_32.wav', y, Fs, 'BitsPerSample', 32);

% Read back and verify
info = audioinfo('output_24.wav');
disp(info.BitsPerSample);
```

### Solution 4: Read a specific segment of audio

```matlab
info = audioinfo('long_recording.wav');
startSample = round(2.5 * info.SampleRate);  % 2.5 seconds in
numSamples = round(5 * info.SampleRate);      % 5 seconds duration
[y, Fs] = audioread('long_recording.wav', [startSample, startSample + numSamples - 1]);
```

### Solution 5: Normalize audio data before writing

```matlab
[y, Fs] = audioread('input.wav');
if max(abs(y(:))) > 1
    y = y / max(abs(y(:)));
    warning('Audio data was out of range [-1, 1] and has been normalized.');
end
audiowrite('normalized.wav', y, Fs);
```

## Examples

Read a WAV file and inspect its properties:

```matlab
[y, Fs] = audioread('speech.wav');
info = audioinfo('speech.wav');
fprintf('Channels: %d\n', info.NumChannels);
fprintf('Sample rate: %d Hz\n', info.SampleRate);
fprintf('Duration: %.2f s\n', info.Duration);
plot((0:length(y)-1)/Fs, y(:,1));
xlabel('Time (s)'); ylabel('Amplitude');
title('Waveform');
```

Write a synthesized tone to different formats:

```matlab
Fs = 44100;
t = 0:1/Fs:2;
y = 0.5 * sin(2*pi*440*t)';  % 440 Hz tone for 2 seconds
audiowrite('tone_440hz.wav', y, Fs);
audiowrite('tone_440hz.flac', y, Fs);
```

## Related Errors

- [MATLAB audiorecorder Error](matlab-audiorecorder) — recording and playback issues
- [MATLAB VideoReader Error](matlab-videoreader) — media file reading errors
- [MATLAB Serial Port Error](matlab-serial-port) — hardware communication issues
