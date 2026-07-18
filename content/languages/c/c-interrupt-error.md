---
title: "[Solution] C Interrupt Handling Error — How to Fix"
description: "Fix ISR errors including latency, stack usage, and shared data races."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Interrupt Handling Error — How to Fix

ISR errors include long execution time, non-reentrant function calls, and uncleared flags.

## Common Error Messages

- `Interrupt latency too high`
- `ISR calling non-async-safe function`
- `Race on shared variable`
- `Infinite ISR loop from uncleared flag`

## How to Fix It

### Keep ISRs short

volatile int data_ready = 0;
volatile int buf[32];
void isr(void) {
    for (int i = 0; i < 32; i++) buf[i] = read_hw();
    data_ready = 1;
}
int main(void) {
    while (1) {
        if (data_ready) {
            data_ready = 0;
            process(buf);
        }
    }
}

### Clear interrupt flag

void isr(void) {
    if (!interrupt_pending()) return;
    // handle interrupt
    clear_interrupt_flag();
}

### Disable interrupts for critical section

#include <stdint.h>
volatile uint32_t shared = 0;
void isr(void) { shared++; }
int main(void) {
    while (1) {
        disable_interrupts();
        uint32_t val = shared;
        enable_interrupts();
        // use val safely
    }
}

### Use atomic operations

#include <stdatomic.h>
atomic_int counter = ATOMIC_VAR_INIT(0);
void isr(void) { atomic_fetch_add(&counter, 1); }

## Common Scenarios

### Scenario 1: ISR too long causing missed interrupts

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: ISR calls malloc/printf which are not reentrant

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: Shared variable modified in ISR and main without protection

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Keep ISRs minimal
- **Tip 2:** Never call non-async-safe functions in ISR
- **Tip 3:** Protect shared data with disable_interrupts or atomics
