---
title: "[Solution] C DMA Error — How to Fix"
description: "Fix C DMA transfer errors including alignment, buffer overflow, and completion handling."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C DMA Error — How to Fix

DMA errors include non-aligned buffers, wrong transfer size, and not waiting for completion before reuse.

## Common Error Messages

- `DMA transfer error`
- `DMA buffer not aligned`
- `DMA transfer incomplete`
- `Cache coherency issue`

## How to Fix It

### Align DMA buffers

__attribute__((aligned(32))) uint8_t dma_buf[1024];

void start_dma_transfer(void *src, void *dst, uint32_t len) {
    // configure DMA with src, dst, len
}

### Wait for completion

volatile int dma_done = 0;
void dma_complete_isr(void) { dma_done = 1; }

void transfer_and_wait(void *src, void *dst, uint32_t len) {
    dma_done = 0;
    start_dma_transfer(src, dst, len);
    while (!dma_done) {}  // wait
}

### Invalidate cache before CPU read

void cpu_read_after_dma(void *buf, uint32_t len) {
    // architecture-specific cache invalidation
    // SCB_InvalidateDCache_by_Addr(buf, len);  // ARM
    uint8_t *data = (uint8_t *)buf;
    // now safe to read
}

### Check DMA status register

int dma_transfer_ok(void) {
    uint32_t status = DMA->ISR;
    if (status & DMA_TC_FLAG) { DMA->IFCR = DMA_TC_FLAG; return 1; }
    if (status & DMA_ERR_FLAG) { DMA->IFCR = DMA_ERR_FLAG; return -1; }
    return 0;  // still in progress
}

## Common Scenarios

### Scenario 1: DMA buffer not aligned causes bus fault

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: CPU reads stale data from cache after DMA write

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: DMA transfer not complete before buffer reuse

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Align buffers to cache line size
- **Tip 2:** Invalidate/flush cache around DMA transfers
- **Tip 3:** Always wait for DMA completion before using buffer
