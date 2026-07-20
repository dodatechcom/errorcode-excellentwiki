---
title: "[Solution] MATLAB Neural Network Training Error — trainNetwork & trainingOptions"
description: "Fix MATLAB trainNetwork and trainingOptions errors for data format, training configuration, and validation issues with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 125
---

MATLAB's `trainNetwork` and `trainingOptions` train deep neural networks. Errors occur when data dimensions do not match the network architecture, training options are misconfigured, or validation data is missing.

## Common Causes

- Input data dimensions do not match the first layer's input size
- `MiniBatchSize` exceeds the number of training samples
- `ValidationData` is not provided and automatic splitting fails
- Sequence data is not formatted as cell arrays of matrices
- `MaxEpochs` is set to 0 or negative

## How to Fix

### Solution 1: Simple classification network

```matlab
load fisheriris;
X = meas';
Y = categorical(species');
layers = [
    featureInputLayer(4)
    fullyConnectedLayer(10)
    reluLayer
    fullyConnectedLayer(3)
    softmaxLayer
    classificationLayer];
options = trainingOptions('sgdm', 'MaxEpochs', 50, 'MiniBatchSize', 16);
net = trainNetwork(X, Y, layers, options);
```

### Solution 2: Image classification with validation split

```matlab
imds = imageDatastore('data', 'IncludeSubfolders', true, 'LabelSource', 'foldernames');
[imdsTrain, imdsVal] = splitEachLabel(imds, 0.8, 'randomized');
layers = [
    imageInputLayer([28 28 1])
    convolution2dLayer(3, 8, 'Padding', 'same')
    batchNormalizationLayer
    reluLayer
    maxPooling2dLayer(2)
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer];
options = trainingOptions('adam', ...
    'MaxEpochs', 20, ...
    'ValidationData', imdsVal, ...
    'ValidationFrequency', 30);
net = trainNetwork(imdsTrain, layers, options);
```

### Solution 3: Sequence (time-series) network

```matlab
numFeatures = 3;
numClasses = 2;
layers = [
    sequenceInputLayer(numFeatures)
    lstmLayer(50, 'OutputMode', 'last')
    fullyConnectedLayer(numClasses)
    softmaxLayer
    classificationLayer];
XTrain = {[randn(3, 20), randn(3, 15)]};
YTrain = categorical({'A'});
options = trainingOptions('adam', 'MaxEpochs', 30);
net = trainNetwork(XTrain, YTrain, layers, options);
```

### Solution 4: Regression network

```matlab
X = randn(100, 5)';
Y = sum(X, 1) + 0.1*randn(1, 100);
layers = [
    featureInputLayer(5)
    fullyConnectedLayer(20)
    reluLayer
    fullyConnectedLayer(1)
    regressionLayer];
options = trainingOptions('sgdm', 'MaxEpochs', 100, 'MiniBatchSize', 32);
net = trainNetwork(X, Y, layers, options);
pred = predict(net, X);
```

### Solution 5: Resume training

```matlab
options = trainingOptions('adam', ...
    'MaxEpochs', 50, ...
    'InitialLearnRate', 1e-4);
net = trainNetwork(X, Y, layers, options);
% Continue training
options2 = trainingOptions('adam', ...
    'MaxEpochs', 50, ...
    'InitialLearnRate', 1e-5);
net = trainNetwork(X, Y, net.Layers, options2);
```

## Examples

Train and evaluate digit classifier:

```matlab
digitDatasetPath = fullfile(matlabroot, 'toolbox', 'nnet', 'nndemos', 'digitDataset');
imds = imageDatastore(digitDatasetPath, 'IncludeSubfolders', true, 'LabelSource', 'foldernames');
[imdsTrain, imdsTest] = splitEachLabel(imds, 0.7, 'randomized');
layers = [
    imageInputLayer([28 28 1])
    convolution2dLayer(5, 6)
    reluLayer
    maxPooling2dLayer(2)
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer];
options = trainingOptions('sgdm', 'MaxEpochs', 10);
net = trainNetwork(imdsTrain, layers, options);
predLabels = classify(net, imdsTest);
accuracy = mean(predLabels == imdsTest.Labels);
fprintf('Test accuracy: %.2f%%\n', accuracy * 100);
```

## Related Errors

- [MATLAB Deep Learning Error](matlab-deep-learning-v2) — custom training loops
- [MATLAB Image Processing Error](matlab-image-processing-error) — image preprocessing
- [MATLAB Machine Learning Error](matlab-machine-learning) — classical ML models
