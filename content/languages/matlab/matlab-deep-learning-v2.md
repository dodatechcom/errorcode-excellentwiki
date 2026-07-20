---
title: "[Solution] MATLAB Deep Learning Custom Training Error — dlnetwork & dlgradient"
description: "Fix MATLAB dlnetwork, dlarray, and dlgradient errors for custom training loops, gradient computation, and data format issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 126
---

MATLAB's `dlnetwork` and `dlgradient` enable custom deep learning training loops. Errors occur when `dlarray` data is not on the correct device, gradients are not computed through the right variables, or the training loop does not converge.

## Common Causes

- `dlgradient` is called with `dlarray` inputs that do not require gradients
- Loss function returns a non-scalar `dlarray`
- `gpuArray` and `dlarray` are mixed incorrectly
- Custom layer does not implement `predict` and `forward` correctly
- Learning rate is too high, causing loss to diverge to `NaN`

## How to Fix

### Solution 1: Basic custom training loop

```matlab
layers = [
    featureInputLayer(2)
    fullyConnectedLayer(10)
    reluLayer
    fullyConnectedLayer(1)
    regressionLayer];
net = dlnetwork(layers);

numEpochs = 100;
learnRate = 0.01;
X = dlarray(randn(100, 2)', 'CB');
Y = dlarray(sum(X.data, 1) + 0.1*randn(1, 100), 'CB');

for epoch = 1:numEpochs
    [loss, grads] = dlfeval(@modelLoss, net, X, Y);
    net = updateParameters(net, grads, learnRate);
    if mod(epoch, 10) == 0
        fprintf('Epoch %d, Loss: %.6f\n', epoch, loss);
    end
end

function [loss, grads] = modelLoss(net, X, Y)
    YPred = forward(net, X);
    loss = mean((YPred - Y).^2, 'all');
    grads = dlgradient(loss, net.Learnables);
end
```

### Solution 2: Use adamupdate optimizer

```matlab
net = dlnetwork(layers);
avgGrad = []; avgSqGrad = [];
for epoch = 1:numEpochs
    [loss, grads] = dlfeval(@modelLoss, net, X, Y);
    [net, avgGrad, avgSqGrad] = adamupdate(net, grads, ...
        avgGrad, avgSqGrad, epoch, learnRate);
end
```

### Solution 3: Training on GPU

```matlab
X = dlarray(randn(100, 2)', 'CB', 'GPU');
Y = dlarray(randn(1, 100), 'CB', 'GPU');
[loss, grads] = dlfeval(@modelLoss, net, X, Y);
```

### Solution 4: Mini-batch training

```matlab
batchSize = 32;
for epoch = 1:numEpochs
    idx = randperm(size(X.data, 2), batchSize);
    Xbatch = dlarray(X.data(:, idx), 'CB');
    Ybatch = dlarray(Y.data(:, idx), 'CB');
    [loss, grads] = dlfeval(@modelLoss, net, Xbatch, Ybatch);
    net = updateParameters(net, grads, learnRate);
end
```

### Solution 5: Validate gradient computation

```matlab
Xtest = dlarray(randn(2, 1), 'CB');
[loss, grads] = dlfeval(@modelLoss, net, Xtest, dlarray(randn(1, 1), 'CB'));
fprintf('Gradient norm: %.6f\n', norm(grads.Value));
```

## Examples

Custom GAN training skeleton:

```matlab
genNet = dlnetwork([featureInputLayer(100); fullyConnectedLayer(256); reluLayer; fullyConnectedLayer(784); sigmoidLayer]);
discNet = dlnetwork([featureInputLayer(784); fullyConnectedLayer(256); reluLayer; fullyConnectedLayer(1); sigmoidLayer]);

for epoch = 1:100
    z = dlarray(randn(32, 100)', 'CB');
    fakeImg = forward(genNet, z);
    score = forward(discNet, fakeImg);
    genLoss = -mean(log(score + 1e-8));
    genGrad = dlgradient(genLoss, genNet.Learnables);
    genNet = updateParameters(genNet, genGrad, 0.001);
end
```

## Related Errors

- [MATLAB Neural Network Training Error](matlab-neural-network-train) — trainNetwork API
- [MATLAB GPU Error](matlab-gpu-error) — GPU memory and compatibility
- [MATLAB Machine Learning Error](matlab-machine-learning) — classical ML models
