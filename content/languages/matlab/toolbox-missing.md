---
title: "[Solution] MATLAB Toolbox Not Found Error Fix"
description: "Fix 'Toolbox not found' or 'Undefined function' when a required MATLAB toolbox is missing or unlicensed."
languages: ["matlab"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# MATLAB Toolbox Not Found Error Fix

This error occurs when MATLAB cannot find or access a required toolbox. The message typically reads: `Undefined function 'functionName' for input arguments of type 'double'.` or `Required toolbox not found.`

## Description

MATLAB toolboxes provide specialized functions for domains like signal processing, image processing, control systems, and machine learning. When you try to use a function from a toolbox that isn't installed or the license isn't available, MATLAB cannot resolve the function call. The error message depends on the specific situation but often appears as an undefined function error.

## Common Causes

- **Toolbox not installed** — the toolbox was never added to the MATLAB installation.
- **License checkout failed** — all available licenses for the toolbox are in use.
- **Toolbox added but not at startup** — the toolbox is installed but not on the MATLAB path.
- **Version mismatch** — the function exists in a newer version of the toolbox than what is installed.

## How to Fix

### Fix 1: Check which toolboxes are installed

```matlab
% List all installed toolboxes
ver

% Check for a specific toolbox
if ~isempty(ver('signal_toolbox'))
    disp('Signal Processing Toolbox is available');
else
    disp('Signal Processing Toolbox is NOT available');
end
```

### Fix 2: Test for toolbox functions before use

```matlab
% Wrong — assumes toolbox is available
result = spectrogram(data, 256, 128, 256, fs);

% Correct — check with license and exist
if license('test', 'signal_toolbox') && exist('spectrogram', 'file')
    result = spectrogram(data, 256, 128, 256, fs);
else
    error('Signal Processing Toolbox is required for this operation');
end
```

### Fix 3: Use isToolboxAvailable helper

```matlab
% Helper function to check toolbox availability
function available = isToolboxAvailable(toolboxName)
    available = ~isempty(ver(toolboxName)) && ...
                license('test', toolboxName);
end

% Usage
if isToolboxAvailable('signal_toolbox')
    result = fft(data);
else
    % Fallback computation
    result = myOwnFFT(data);
end
```

### Fix 4: Use the MATLAB Add-On Explorer

```matlab
% Check license status
[status, errmsg] = license('checkout', 'signal_toolbox');
if status == 0
    disp('License checkout failed:');
    disp(errmsg);
    % Option: open Add-On Explorer to install
    matlab.addons.explore;
end
```

## Examples

```matlab
>> spectrogram(x, 256, [], [], fs)
Undefined function 'spectrogram' for input arguments of type 'double'.

>> imread('photo.jpg')  % Requires Image Processing Toolbox
Undefined function 'imread' for input arguments of type 'char'.

>> ver('signal')
% Empty if Signal Processing Toolbox is not installed
```

## Related Errors

- [Undefined Function]({{< relref "/languages/matlab/undefined-function" >}}) — general undefined function or variable error.
- [Not Enough Inputs]({{< relref "/languages/matlab/not-enough-inputs" >}}) — missing function arguments.
