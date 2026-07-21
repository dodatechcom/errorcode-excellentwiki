---
title: "NFC NDEF Error"
description: "Fix Android NFC NDEF tag reading and writing errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
NFC tag reading or NDEF message writing fails

## Common Causes

- NFC not enabled on device
- Tag does not contain NDEF data
- NDEF message not properly constructed
- NFC permission not declared in manifest

## Fixes

- Check NFC availability with PackageManager.FEATURE_NFC
- Verify tag supports NDEF with Ndef.get(tag)
- Build NdefMessage with NdefRecord
- Add NFC permission in manifest

## Code Example

```kotlin
<!-- Manifest -->
<uses-feature android:name="android.hardware.nfc" android:required="false" />
<uses-permission android:name="android.permission.NFC" />

// Read NDEF:
override fun onNewIntent(intent: Intent) {
    if (NfcAdapter.ACTION_NDEF_DISCOVERED == intent.action) {
        val rawMessages = intent.getParcelableArrayExtra(NfcAdapter.EXTRA_NDEF_MESSAGES)
        rawMessages?.forEach { msg ->
            val ndefMessage = msg as NdefMessage
            val record = ndefMessage.records[0]
            val payload = String(record.payload)
        }
    }
}
```

# Foreground dispatch for tag detection:
# nfcAdapter.enableForegroundDispatch(this, pendingIntent, filters, techLists)
