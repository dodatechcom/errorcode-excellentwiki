---
title: "[Solution] R Keras Tensor Shape Mismatch Error Fix"
description: "Fix 'Keras: tensor shape mismatch' in R. Resolve tensor dimension errors in Keras model training and prediction."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# R Keras Tensor Shape Mismatch Error Fix

The `Keras: tensor shape mismatch` error occurs when the input data shape does not match the expected shape of a Keras model layer, during training or prediction.

## What This Error Means

Keras models have fixed input shapes defined at model creation. When you feed data with different dimensions (wrong number of features, batch size, or time steps), the tensor shapes do not match.

A typical error:

```
Error: Input 0 of layer "dense" is incompatible with the layer: 
expected axis -1 of input shape to have value 10 but received input with shape [32, 5]
```

## Why It Happens

Common causes include:

- **Wrong input shape** — Data has different number of features than model expects.
- **Missing batch dimension** — Single sample needs batch axis.
- **Reshape not applied** — Data needs reshaping for CNN/RNN layers.
- **Feature count mismatch** — Training and test data have different features.
- **Model architecture change** — Modified model without retraining.

## How to Fix It

### Fix 1: Check input shape

```r
# RIGHT: Check model expected input
library(keras)
model <- load_model("my_model.h5")
model$input_shape

# Check actual data shape
dim(x_train)
```

### Fix 2: Reshape data to match model

```r
# RIGHT: Reshape for dense layers
x_train <- array(x_train, dim = c(nrow(x_train), ncol(x_train)))

# RIGHT: Reshape for CNN (add channel dimension)
x_train <- array(x_train, dim = c(nrow(x_train), 28, 28, 1))

# RIGHT: Reshape for RNN (add time steps)
x_train <- array(x_train, dim = c(nrow(x_train), 10, ncol(x_train)))
```

### Fix 3: Add batch dimension for single sample

```r
# RIGHT: Single sample prediction
sample <- x_test[1, ]
dim(sample)  # (10,)

# Add batch dimension
sample <- array_reshape(sample, c(1, length(sample)))
predict(model, sample)
```

### Fix 4: Use Input layer with correct shape

```r
# RIGHT: Define model with explicit input shape
model <- keras_model_sequential() %>%
    layer_dense(units = 64, activation = "relu", input_shape = c(10)) %>%
    layer_dense(units = 1)

summary(model)
```

### Fix 5: Pad sequences for RNN

```r
# RIGHT: Pad sequences to same length
library(keras)
x_train <- pad_sequences(x_train, maxlen = 100, padding = "post")
```

## Common Mistakes

- **Forgetting that Keras expects 4D arrays for CNNs** — Batch, Height, Width, Channels.
- **Not using `array_reshape`** — R matrices are column-major, Keras expects row-major.
- **Mixing training and prediction shapes** — Ensure consistency.

## Related Pages

- [R Package Not Found](r-package-not-found) — Package installation issues
- [R Object Not Found](r-object-not-found) — Undefined variable errors
- [R Type Error](r-type-error) — Type conversion errors
