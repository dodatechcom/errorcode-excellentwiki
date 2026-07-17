---
title: "[Solution] macOS NSFileWriteUnsupportedEncoding (NSCocoaErrorDomain Code 518) — Unsupported Encoding"
description: "Fix macOS NSFileWriteUnsupportedEncoding (NSCocoaErrorDomain Code 518). Resolve Foundation unsupported encoding write errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS NSFileWriteUnsupportedEncoding (NSCocoaErrorDomain Code 518) — Unsupported Encoding

NSFileWriteUnsupportedEncoding (error code 518 in NSCocoaErrorDomain) indicates that the string encoding used for writing is not supported by the target file format or system. This error occurs when an invalid or unsupported encoding is specified for the write operation, or the target format cannot accommodate the chosen encoding.

## Common Causes

- The specified encoding is not valid for the target file format (e.g., writing UTF-32 to a format that only supports UTF-8)
- A deprecated or obsolete encoding was used that is no longer supported by the system
- The encoding identifier is invalid or incorrectly specified
- The file format (e.g., binary plist) restricts which text encodings are allowed
- The encoding was incorrectly set on the string or data conversion

## How to Fix NSFileWriteUnsupportedEncoding

### 1. Use a Supported Encoding

Switch to a standard encoding such as UTF-8:

```bash
# Check the file's current encoding
file -I /path/to/file

# Convert to UTF-8
iconv -f CURRENT_ENCODING -t UTF-8 /path/to/file > /path/to/file.utf8
```

### 2. Specify UTF-8 in Code

Use UTF-8 as the encoding for write operations:

```swift
// Use UTF-8 for all text writes
let data = string.data(using: .utf8)
try data?.write(to: fileURL)
```

### 3. List Supported Encodings

Identify which encodings are available on the system:

```bash
# List all supported encodings
iconv -l

# Check available CFString encodings
python3 -c "import codecs; print([c[0] for c in codecs.lookup_error if isinstance(c, tuple)])"
```

### 4. Validate Encoding Before Writing

Check encoding compatibility before performing the write:

```swift
guard let data = string.data(using: .utf8) else {
    print("String cannot be encoded in UTF-8")
    return
}
try data.write(to: fileURL)
```

### 5. Handle Encoding in File Formats

When writing to specific formats, match the encoding to the format requirements:

```swift
// Property list files should use UTF-8
let plistData = try PropertyListSerialization.data(fromPropertyList: dict, format: .xml, options: 0)
try plistData.write(to: fileURL)
```

## Examples

This error commonly occurs when:

- Writing a file with an encoding that the target application does not support
- Specifying a legacy encoding (e.g., EUC-JP) for a format that requires UTF-8
- Attempting to write binary plist data using a text-only encoding
- An application incorrectly sets the encoding when converting between formats

## Related Error Codes

- NSFileWriteIncompatibleEncoding (NSCocoaErrorDomain Code 517) — [Incompatible Encoding](/os/macos/nserror-8/)
- NSFileReadUnsupportedEncoding (NSCocoaErrorDomain Code 261) — [Read Unsupported Encoding](/os/macos/nserror-13/)
- NSFileWriteUnknownError (NSCocoaErrorDomain Code 513) — [Unknown Write Error](/os/macos/nserror-2/)
- NSFileWriteNoPermission (NSCocoaErrorDomain Code 516) — [No Permission](/os/macos/nserror-4/)
