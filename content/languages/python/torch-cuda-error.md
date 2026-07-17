---
title: "[Solution] PyTorch RuntimeError: CUDA Out of Memory Fix"
description: "Fix PyTorch RuntimeError: CUDA out of memory. Free GPU memory, reduce batch size, and use mixed precision training."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["pytorch", "cuda", "gpu", "out-of-memory", "torch"]
weight: 5
---

# RuntimeError: CUDA Out of Memory — PyTorch Fix

A `RuntimeError: CUDA out of memory` is raised when PyTorch cannot allocate enough GPU memory for a tensor or operation. This is the most common GPU error in deep learning workflows.

## What This Error Means

Common messages:

- `RuntimeError: CUDA out of memory. Tried to allocate X MiB`
- `RuntimeError: CUDA error: out of memory`
- `torch.cuda.OutOfMemoryError: CUDA out of memory`

PyTorch attempted to allocate GPU memory for a new tensor but the GPU has insufficient free VRAM. Existing tensors, cached memory, or other processes consuming GPU resources leave too little room.

## Common Causes

```python
# Cause 1: Batch size too large for GPU VRAM
model = MyModel().cuda()
for batch in dataloader:  # batch size 512 on a 4GB GPU
    output = model(batch.cuda())  # CUDA out of memory

# Cause 2: Accumulated gradients never freed
for batch in dataloader:
    loss = model(batch.cuda()).loss
    loss.backward()  # Gradients accumulate each iteration
    # Optimizer step never called — memory grows unbounded

# Cause 3: Large tensors held in memory
activations = []
for batch in dataloader:
    out = model(batch.cuda())
    activations.append(out)  # List grows, never freed

# Cause 4: Multiple models or processes on same GPU
model_a = LargeModel().cuda()  # GPU 0
model_b = LargeModel().cuda()  # GPU 0 — both compete for VRAM
```

## How to Fix

### Fix 1: Reduce batch size

```python
# Wrong — too large for available VRAM
dataloader = DataLoader(dataset, batch_size=256)

# Correct — fit within GPU memory
dataloader = DataLoader(dataset, batch_size=32)
```

### Fix 2: Use mixed precision training

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
for batch in dataloader:
    with autocast():
        output = model(batch.cuda())
        loss = criterion(output, target)
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

### Fix 3: Use gradient accumulation for effective large batches

```python
accumulation_steps = 8
optimizer.zero_grad()
for i, batch in enumerate(dataloader):
    loss = model(batch.cuda()) / accumulation_steps
    loss.backward()
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

### Fix 4: Clear GPU memory explicitly

```python
import torch
import gc

# Delete tensors and call garbage collector
del output, loss
gc.collect()
torch.cuda.empty_cache()
```

### Fix 5: Use gradient checkpointing

```python
from torch.utils.checkpoint import checkpoint

class LargeModel(nn.Module):
    def forward(self, x):
        x = checkpoint(self.layer1, x)
        x = checkpoint(self.layer2, x)
        return x
```

### Fix 6: Monitor GPU memory usage

```python
print(f"Allocated: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
print(f"Reserved:  {torch.cuda.memory_reserved() / 1e9:.2f} GB")
```

## Related Errors

- {{< relref "memoryerror" >}} — Python out-of-memory for CPU RAM.
- {{< relref "importerror-torch" >}} — PyTorch import or installation issue.
