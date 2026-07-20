---
title: "[Solution] MATLAB fft/ifft — Length, Dimension, and Frequency Resolution Errors"
description: "Fix MATLAB FFT errors: transform length selection, dimension mismatch, frequency resolution, and zero-padding."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 123
---

## Common Causes

- FFT along wrong dimension for matrix input
- Non-power-of-2 length causing slow computation (not an error, but confusing)
- Frequency axis computed with wrong sampling rate
- Forgetting `fftshift` for centered spectrum display
- Zero-padding changing frequency resolution unexpectedly

## How to Fix

```matlab
% WRONG: FFT along rows instead of columns
data = randn(100, 10);  % 10 signals, 100 samples each
Y = fft(data);           % FFT along columns — 100-point FFT for each column

% CORRECT: Specify dimension for multi-channel data
Y = fft(data, [], 1);    % FFT along dim 1 (samples) — same as default
Y = fft(data, [], 2);    % FFT along dim 2 if needed
```

```matlab
% WRONG: Frequency axis wrong length
Fs = 1000;
N = 1024;
x = randn(N, 1);
X = fft(x);
f = 0:Fs/N:Fs-Fs/N;     % Length N — correct
% f = linspace(0, Fs, N); % WRONG: includes Fs endpoint, length mismatch

% CORRECT: Proper frequency axis
f = (0:N-1) * (Fs / N);              % One-sided
f_shifted = (-N/2:N/2-1) * (Fs / N); % Two-sided centered
```

```matlab
% CORRECT: Use fftshift for centered display
X_shifted = fftshift(X);
f = (-N/2:N/2-1) * (Fs / N);
plot(f, abs(X_shifted));
xlabel('Frequency (Hz)');
ylabel('Magnitude');
```

```matlab
% CORRECT: Zero-padding for interpolation, not resolution
N_orig = 256;
N_padded = 1024;
x = randn(N_orig, 1);
X_padded = fft(x, N_padded);
% Note: frequency resolution is still Fs/N_orig, not Fs/N_padded

% True resolution improvement requires more data
```

```matlab
% CORRECT: Compute PSD with proper normalization
function [Pxx, f] = computePSD(x, Fs, NFFT)
    if nargin < 3, NFFT = min(256, length(x)); end
    [Pxx, f] = pwelch(x, hanning(NFFT), NFFT/2, NFFT, Fs);
end
```

## Examples

```matlab
% Example: Full FFT analysis pipeline
Fs = 1000;
t = 0:1/Fs:1-1/Fs;
f0 = 50;
x = sin(2*pi*f0*t) + 0.5*randn(size(t));
N = length(x);

X = fft(x);
X_mag = abs(X(1:N/2+1)) / N;
f = (0:N/2) * (Fs / N);

figure;
subplot(2,1,1); plot(t, x); xlabel('Time (s)');
subplot(2,1,2); plot(f, X_mag); xlabel('Frequency (Hz)');
```

## Related Errors

- [Plot Error](matlab-plot-error) — display issues
- [Matrix Inversion](matlab-matrix-inversion) — numerical issues
- [Linear Solve](matlab-linear-solve) — matrix operations
