---
title: "[Solution] C Embedded Systems Error — How to Fix"
description: "Fix embedded C errors including register access and resource constraints."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Embedded Systems Error — How to Fix

Embedded errors include uninitialized peripherals, volatile misuse, and stack overflow.

## Common Error Messages

- `Hard fault from bad memory access`
- `Watchdog timeout from infinite loop`
- `Stack overflow in ISR`
- `Register alignment fault`

## How to Fix It

### Volatile for registers

#include <stdint.h>
#define GPIO_ODR (*(volatile uint32_t *)0x48000014)
#define GPIO_IDR (*(volatile uint32_t *)0x48000010)
void set_pin(int p) { GPIO_ODR |= (1 << p); }
int read_pin(int p) { return (GPIO_IDR >> p) & 1; }

### Bit macros

#include <stdint.h>
#define SET_BIT(r,b) ((r) |= (1<<(b)))
#define CLR_BIT(r,b) ((r) &= ~(1<<(b)))
#define RD_BIT(r,b) (((r)>>(b))&1)

### Static alloc

static uint8_t big_buf[4096];
void process(void) { /* use big_buf */ }

### ISR pattern

volatile int flag = 0;
void timer_isr(void) { flag = 1; }
int main(void) {
    while (1) { if (flag) { flag = 0; /* handle */ } }
}

## Common Scenarios

### Scenario 1: Hard fault from unmapped memory

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Watchdog reset from slow loop

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: Race between ISR and main

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Use volatile for HW registers
- **Tip 2:** Static alloc in ISR context
- **Tip 3:** Disable interrupts for shared vars
