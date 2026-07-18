---
title: "[Solution] C GPIO Error — How to Fix"
description: "Fix C GPIO configuration and operation errors including direction, pull-ups, and mode."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C GPIO Error — How to Fix

GPIO errors include wrong direction (input vs output), missing pull-up/pull-down, and wrong alternate function selection.

## Common Error Messages

- `GPIO pin not responding`
- `Wrong direction configured`
- `GPIO alternate function incorrect`
- `GPIO port clock not enabled`

## How to Fix It

### Configure pin direction

void gpio_set_output(uint32_t port, int pin) {
    port->DDR |= (1 << pin);   // output
    port->CR1 |= (1 << pin);   // push-pull
}
void gpio_set_input(uint32_t port, int pin) {
    port->DDR &= ~(1 << pin);  // input
    port->CR2 |= (1 << pin);   // pull-up
}

### Read and write

int gpio_read(uint32_t port, int pin) {
    return (port->IDR >> pin) & 1;
}
void gpio_write(uint32_t port, int pin, int val) {
    if (val) port->ODR |= (1 << pin);
    else port->ODR &= ~(1 << pin);
}

### Enable port clock

void gpio_enable_clock(int port) {
    RCC->AHB1ENR |= (1 << port);  // STM32
}

### Set alternate function

void gpio_set_af(int port, int pin, int af) {
    GPIOA->MODER &= ~(3 << (pin * 2));
    GPIOA->MODER |= (2 << (pin * 2));
    GPIOA->AFR[pin / 8] &= ~(0xF << ((pin % 8) * 4));
    GPIOA->AFR[pin / 8] |= (af << ((pin % 8) * 4));
}

## Common Scenarios

### Scenario 1: Pin direction not set correctly

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Port clock not enabled before use

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: Wrong alternate function for peripheral pin

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Always enable GPIO port clock first
- **Tip 2:** Verify direction (DDR) setting
- **Tip 3:** Check alternate function mapping from datasheet
