---
title: "[Solution] C Modbus Error — How to Fix"
description: "Fix C Modbus protocol errors including CRC, function codes, and timeout handling."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Modbus Error — How to Fix

Modbus errors include CRC mismatch, illegal function code, and response timeout.

## Common Error Messages

- `Modbus CRC error`
- `Illegal function code`
- `Response timeout`
- `Illegal data address`

## How to Fix It

### Calculate CRC16

uint16_t modbus_crc16(uint8_t *data, uint16_t len) {
    uint16_t crc = 0xFFFF;
    for (uint16_t i = 0; i < len; i++) {
        crc ^= data[i];
        for (int j = 0; j < 8; j++) {
            if (crc & 1) crc = (crc >> 1) ^ 0xA001;
            else crc >>= 1;
        }
    }
    return crc;
}

### Build read request

uint16_t build_read_holding(uint8_t *buf, uint8_t addr, uint16_t reg, uint16_t count) {
    buf[0] = addr;
    buf[1] = 0x03;
    buf[2] = reg >> 8;
    buf[3] = reg & 0xFF;
    buf[4] = count >> 8;
    buf[5] = count & 0xFF;
    uint16_t crc = modbus_crc16(buf, 6);
    buf[6] = crc & 0xFF;
    buf[7] = crc >> 8;
    return 8;
}

### Verify response CRC

int verify_response(uint8_t *buf, uint16_t len) {
    if (len < 4) return -1;
    uint16_t recv_crc = buf[len-2] | (buf[len-1] << 8);
    uint16_t calc_crc = modbus_crc16(buf, len - 2);
    if (recv_crc != calc_crc) return -2;
    if (buf[1] & 0x80) return -3;
    return 0;
}

### Handle timeout

int modbus_send_recv(uint8_t *req, uint16_t req_len,
                     uint8_t *resp, uint16_t *resp_len, int timeout_ms) {
    uart_send(req, req_len);
    return uart_recv_timeout(resp, resp_len, timeout_ms);
}

## Common Scenarios

### Scenario 1: CRC mismatch between master and slave

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Slave receives unsupported function code

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: No response within timeout period

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Always verify CRC on received messages
- **Tip 2:** Return error response for unsupported functions
- **Tip 3:** Implement proper timeout handling
