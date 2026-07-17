---
title: "[Solution] Deep Learning Toolbox: GPU out of memory in MATLAB"
description: "Fix MATLAB Deep Learning Toolbox errors when GPU runs out of memory during training or inference."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["deep-learning", "gpu", "memory", "toolbox", "neural-network", "matlab"]
weight: 5
---

## What This Error Means

Deep Learning Toolbox GPU errors occur when the GPU runs out of memory during network training or inference. This is common with large networks, large batch sizes, or insufficient GPU memory.

## Common Causes

- Batch size too large for GPU memory
- Network architecture too complex
- Multiple networks on GPU simultaneously
- GPU memory fragmented
- Data not properly managed

## How to Fix

```matlab
% WRONG: Batch size too large
options = trainingOptions('sgdm', ...
    'MiniBatchSize', 256, ...  % Too large
    'MaxEpochs', 10);

% CORRECT: Reduce batch size
options = trainingOptions('sgdm', ...
    'MiniBatchSize', 32, ...  % Smaller batch
    'MaxEpochs', 100);
```

```matlab
% WRONG: Not checking GPU memory
gpuDevice(1);  % May not have enough memory

% CORRECT: Check GPU and clear memory
gpu = gpuDevice(1);
disp(['Available GPU memory: ' num2str(gpu.AvailableMemory/1e9) ' GB']);

% Clear GPU memory
clear gpu;
gpuDevice(1);
```

```matlab
% CORRECT: Use memory-efficient training
options = trainingOptions('sgdm', ...
    'MiniBatchSize', 16, ...
    'MaxEpochs', 50, ...
    'GradientThreshold', 1, ...
    'Verbose', false);

% Train with smaller network
layers = [
    imageInputLayer([28 28 1])
    convolution2dLayer(3, 8)
    reluLayer
    maxPooling2dLayer(2)
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer
];
```

```matlab
% CORRECT: Train on CPU if GPU insufficient
options = trainingOptions('sgdm', ...
    'ExecutionEnvironment', 'cpu', ...
    'MiniBatchSize', 64);
```

```matlab
% CORRECT: Use datastores for large datasets
ds = imageDatastore('images/', 'IncludeSubfolders', true);
augimds = augmentedImageDatastore([28 28 1], ds);

% Train in mini-batches automatically
net = trainNetwork(augimds, layers, options);
```

## Related Errors

- [Out of Memory](/languages/fortran/fortran-allocate-error-v2) - memory issues
- [ODE Solver Error](matlab-ode-solver-error) - solver issues
- [Simulink Error](matlab-simulink-error-v2) - model errors
