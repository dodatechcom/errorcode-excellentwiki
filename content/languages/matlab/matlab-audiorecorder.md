---
title: "[Solution] MATLAB audiorecorder Error — Record, Play, Pause & getaudiodata"
description: "Fix MATLAB audiorecorder errors for recording, playback, pause/resume, and getaudiodata extraction with working code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 102
---

The `audiorecorder` object in MATLAB allows recording from a microphone, but errors arise when the audio device is unavailable, sampling parameters are invalid, or playback is attempted on an unrecorded object.

## Common Causes

- No audio input device is connected or recognized by the system
- Sample rate is not supported by the hardware (e.g., requesting 192 kHz on a device that only supports 44.1 kHz)
- Number of channels exceeds the hardware capability
- Calling `play` on an `audiorecorder` object that has no recorded data
- Attempting to resume playback after calling `stop` instead of `pause`

## How to Fix

### Solution 1: Verify audio devices are available

```matlab
devices = audiodevinfo;
if isempty(devices.input)
    error('No audio input devices found.');
end
disp('Available input devices:');
for i = 1:length(devices.input)
    fprintf('  %d: %s (MaxFs: %d Hz)\n', devices.input(i).ID, ...
        devices.input(i).Name, devices.input(i).SupportedSampleRates(end));
end
```

### Solution 2: Create audiorecorder with safe defaults

```matlab
recObj = audiorecorder(44100, 16, 1);
disp('Start speaking...');
recordblocking(recObj, 5);  % Record for 5 seconds
disp('Recording complete.');

y = getaudiodata(recObj);
disp(['Recorded samples: ', num2str(length(y))]);
```

### Solution 3: Record and play back safely

```matlab
recObj = audiorecorder(44100, 16, 1);
record(recObj);       % Start recording asynchronously
disp('Recording...');
pause(3);             % Record for 3 seconds
stop(recObj);         % Stop recording
disp('Playing back...');
play(recObj);         % Play back the recording
wait(recObj);         % Wait until playback finishes
```

### Solution 4: Extract and process recorded data

```matlab
recObj = audiorecorder(44100, 16, 1);
recordblocking(recObj, 4);

y = getaudiodata(recObj);
t = (0:length(y)-1) / recObj.SampleRate;

% Plot waveform
figure;
plot(t, y);
xlabel('Time (s)');
ylabel('Amplitude');
title('Recorded Audio');

% Compute spectrum
Y = fft(y);
f = (0:length(y)-1) * (recObj.SampleRate / length(y));
figure;
plot(f(1:floor(end/2)), abs(Y(1:floor(end/2))));
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Frequency Spectrum');
```

### Solution 5: Handle pause and resume correctly

```matlab
recObj = audiorecorder(44100, 16, 1);
record(recObj);
disp('Recording...');
pause(2);
pause(recObj);        % Pause recording
disp('Paused.');
pause(1);
resume(recObj);       % Resume recording
disp('Resumed.');
pause(2);
stop(recObj);

% Save the recording
y = getaudiodata(recObj);
audiowrite('captured.wav', y, recObj.SampleRate);
```

## Examples

Record audio, detect silence, and trim:

```matlab
recObj = audiorecorder(44100, 16, 1);
recordblocking(recObj, 5);
y = getaudiodata(recObj);
Fs = recObj.SampleRate;

threshold = 0.01;
speechIdx = find(abs(y) > threshold);
if ~isempty(speechIdx)
    yTrimmed = y(speechIdx(1):speechIdx(end));
    audiowrite('trimmed.wav', yTrimmed, Fs);
end
```

## Related Errors

- [MATLAB audioread/audiowrite Error](matlab-audioread-error) — file format and codec issues
- [MATLAB Serial Port Error](matlab-serial-port) — hardware device communication
- [MATLAB Arduino Error](matlab-arduino-error) — microcontroller I/O
