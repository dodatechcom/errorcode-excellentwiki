---
title: "[Solution] macOS NSFileWriteIncompatibleEncoding (NSCocoaErrorDomain Code 517) — Incompatible Encoding"
description: "Fix macOS NSFileWriteIncompatibleEncoding (NSCocoaErrorDomain Code 517). Resolve Foundation incompatible encoding write errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS NSFileWriteIncompatibleEncoding (NSCocoaErrorDomain Code 517) — Incompatible Encoding

NSFileWriteIncompatibleEncoding (error code 517 in NSCocoaErrorDomain) indicates that the string encoding specified for writing is incompatible with the file's existing encoding or the target format. This error occurs when attempting to write a string using an encoding that cannot represent the characters in the string, or when the file format does not support the chosen encoding.

## Common Causes

- The string contains characters not representable in the chosen encoding (e.g., writing UTF-8 characters to an ASCII-only file)
- An existing file was opened with one encoding and the write operation uses a different, incompatible encoding
- The target file format (e.g., plist binary format) does not support the specified text encoding
- A character set conversion lossy mapping is required and the operation was not configured to allow data loss

## How to Fix NSFileWriteIncompatibleEncoding

### 1. Use UTF-8 Encoding

Switch to UTF-8, which supports all Unicode characters:

```bash
# Convert a file to UTF-8
iconv -f OLD_ENCODING -t UTF-8 /path/to/file > /path/to/file.utf8
mv /path/to/file.utf8 /path/to/file
```

### 2. Specify UTF-8 in Code

Ensure the write operation uses UTF-8 encoding:

```swift
// Writing with explicit UTF-8 encoding
let data = string.data(using: .utf8)
try data?.write(to: fileURL)
```

### 3. Detect Existing File Encoding

Determine the encoding of the existing file before writing:

```bash
# Detect file encoding
file -I /path/to/file
chardetect /path/to/file

# Use iconv to list supported encodings
iconv -l
```

### 4. Handle Encoding Conversion in Code

When converting between encodings, use lossy conversion if appropriate:

```swift
if let data = string.data(using: .utf8, allowLossyConversion: true) {
    try data.write(to: fileURL)
}
```

### 5. Preserve Original Encoding

If the file format requires a specific encoding, match it:

```swift
// Write using the same encoding as the original file
if let data = string.data(using: .isoLatin1) {
    try data.write(to: fileURL, options: .atomic)
}
```

## Examples

This error commonly occurs when:

- Writing Unicode emoji to a file opened with ASCII encoding
- Converting a UTF-16 file to a format that requires UTF-8
- Saving localized text with characters outside Latin-1 to a legacy format
- An application uses the wrong string encoding when writing a property list

## Related Error Codes

- NSFileWriteUnsupportedEncoding (NSCocoaErrorDomain Code 518) — [Unsupported Encoding](/os/macos/nserror-12/)
- NSFileReadUnsupportedEncoding (NSCocoaErrorDomain Code 261) — [Read Unsupported Encoding](/os/macos/nserror-13/)
- NSFileWriteUnknownError (NSCocoaErrorDomain Code 513) — [Unknown Write Error](/os/macos/nserror-2/)
- NSFileWriteNoPermission (NSCocoaErrorDomain Code 516) — [No Permission](/os/macos/nserror-4/)
