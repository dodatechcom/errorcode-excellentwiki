---
title: "NFC Beam Error"
description: "Fix Android NFC Android Beam and data transfer errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Android Beam fails to transfer data between devices

## Common Causes

- NfcAdapter not initialized
- CreateNfcBeamCallback not implemented
- Data payload too large for beam
- Devices not held close enough

## Fixes

- Initialize NfcAdapter in onCreate
- Implement createNdefMessageCallback
- Keep payload small, use URI or text records
- Hold devices back-to-back until beam completes

## Code Example

```kotlin
val nfcAdapter = NfcAdapter.getDefaultAdapter(this)
nfcAdapter.setNdefPushMessageCallback(object : NfcAdapter.CreateNdefMessageCallback {
    override fun createNdefMessage(event: NfcEvent): NdefMessage {
        val text = "Hello from my app"
        val record = NdefRecord.createText("en", text.toByteArray())
        return NdefMessage(arrayOf(record))
    }
}, this)
```

# Android Beam deprecated in API 30+
# Use alternative sharing for modern apps
