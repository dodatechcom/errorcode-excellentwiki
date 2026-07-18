---
title: "[Solution] C CAN Bus Error — How to Fix"
description: "Fix C CAN bus communication errors including bit timing, error passive, and bus-off."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C CAN Bus Error — How to Fix

CAN bus errors include bit timing mismatch, error passive state, and bus-off from too many errors.

## Common Error Messages

- `CAN bus-off state`
- `CAN error passive`
- `CAN bus error (LEC)`
- `CAN arbitration lost`

## How to Fix It

### Configure bit timing

void can_set_timing(uint32_t pclk, uint32_t bitrate) {
    uint32_t tq_count = pclk / bitrate;
    uint32_t sjw = 1;
    uint32_t bs1 = tq_count * 7 / 8;
    uint32_t bs2 = tq_count - bs1 - 1;
    CAN->BTR = ((sjw-1) << 24) | ((bs1-1) << 16) | ((bs2-1) << 20);
}

### Check error state

int can_get_error_state(void) {
    uint32_t esr = CAN->ESR;
    if (esr & CAN_ESR_BOFF) return -2;  // bus-off
    if (esr & CAN_ESR_EPV) return -1;   // error passive
    return 0;  // error active
}

### Transmit a message

int can_send(uint32_t id, uint8_t *data, uint8_t len) {
    if (CAN->TSR & CAN_TSR_TME0) {
        CAN->sTxMailBox[0].TIR = (id << 3);
        CAN->sTxMailBox[0].TDTR = len;
        for (int i = 0; i < len; i++)
            CAN->sTxMailBox[0].TDLR = data[i];
        CAN->sTxMailBox[0].TIR |= CAN_TI0R_TXRQ;
        return 0;
    }
    return -1;
}

### Receive a message

int can_receive(uint32_t *id, uint8_t *data, uint8_t *len) {
    if (CAN->RF0R & CAN_RF0R_FMP0) {
        *id = (CAN->sFIFOMailBox[0].RIR >> 3) & 0x7FF;
        *len = CAN->sFIFOMailBox[0].RDTR & 0xF;
        data[0] = CAN->sFIFOMailBox[0].RDLR & 0xFF;
        CAN->RF0R |= CAN_RF0R_RFOM0;
        return 0;
    }
    return -1;
}

## Common Scenarios

### Scenario 1: Bit timing mismatch between nodes

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Bus-off from excessive error counters

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: TX mailbox full when trying to send

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Verify bit timing matches baud rate
- **Tip 2:** Handle bus-off by reinitializing CAN
- **Tip 3:** Check TX mailbox availability before sending
