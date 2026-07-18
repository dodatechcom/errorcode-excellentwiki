---
title: "[Solution] C I2C Error — How to Fix"
description: "Fix C I2C communication errors including NAK, bus arbitration, and address issues."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C I2C Error — How to Fix

I2C errors include NAK from device, bus stuck low (SDA/SCL), and wrong 7/10-bit addressing.

## Common Error Messages

- `I2C NAK from slave`
- `I2C bus stuck (SDA held low)`
- `I2C arbitration lost`
- `I2C timeout`

## How to Fix It

### Check ACK after address

int i2c_write_addr(uint8_t addr) {
    i2c_start();
    uint8_t status = i2c_send_byte(addr << 1);  // write
    if (status != I2C_ACK) {
        i2c_stop();
        return -1;  // NAK
    }
    return 0;
}

### Recover stuck bus

void i2c_recover_bus(void) {
    // Toggle SCL up to 9 times while SDA is monitored
    for (int i = 0; i < 9; i++) {
        scl_high();  // clock pulses
        delay_us(5);
        scl_low();
        delay_us(5);
    }
    i2c_start();
    i2c_stop();
}

### Read with ACK/NAK

uint8_t i2c_read_byte(int ack) {
    uint8_t byte = i2c_receive_byte();
    if (ack) i2c_send_ack();
    else i2c_send_nak();
    return byte;
}

### Write register sequence

int i2c_write_reg(uint8_t dev_addr, uint8_t reg, uint8_t val) {
    i2c_start();
    if (i2c_send_byte(dev_addr << 1) != I2C_ACK) goto fail;
    if (i2c_send_byte(reg) != I2C_ACK) goto fail;
    if (i2c_send_byte(val) != I2C_ACK) goto fail;
    i2c_stop();
    return 0;
fail:
    i2c_stop();
    return -1;
}

## Common Scenarios

### Scenario 1: Device does not ACK its address

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: SDA stuck low prevents all communication

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: Wrong register address causes read failure

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Always check ACK/NAK after sending
- **Tip 2:** Implement bus recovery (clock toggling)
- **Tip 3:** Verify device address and register map from datasheet
