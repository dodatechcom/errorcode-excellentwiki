---
title: "[Solution] C UART Error — How to Fix"
description: "Fix C UART communication errors including baud rate, framing errors, and buffer overflow."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C UART Error — How to Fix

UART errors include baud rate mismatch, framing errors from noise, and RX buffer overrun.

## Common Error Messages

- `UART framing error`
- `UART overrun error`
- `Baud rate mismatch`
- `RX buffer overflow`

## How to Fix It

### Set baud rate correctly

void uart_init(uint32_t periph_hz, uint32_t baud) {
    uint32_t divider = periph_hz / baud;
    UART->BRR = divider;
}

### Enable interrupts for RX

#define RX_BUF_SIZE 256
volatile uint8_t rx_buf[RX_BUF_SIZE];
volatile uint32_t rx_head = 0;

void uart_rx_isr(void) {
    rx_buf[rx_head] = UART->DR;
    rx_head = (rx_head + 1) % RX_BUF_SIZE;
}

### Check status flags

int uart_send_byte(uint8_t b) {
    int timeout = 10000;
    while (!(UART->SR & UART_TXE) && --timeout) {}
    if (!timeout) return -1;
    UART->DR = b;
    return 0;
}

### Handle framing error

void uart_error_isr(void) {
    if (UART->SR & UART_FE) {
        (void)UART->DR;  // clear flag by reading
    }
}

## Common Scenarios

### Scenario 1: Baud rate does not match between devices

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Noise on line causes framing errors

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: RX interrupt not enabled causes data loss

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Verify baud rate settings match on both sides
- **Tip 2:** Check wiring and add pull-ups for noisy lines
- **Tip 3:** Enable RX interrupt and use ring buffer
