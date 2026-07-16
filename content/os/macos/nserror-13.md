---
title: "[Solution] macOS NSFileReadUnsupportedEncoding (NSCocoaErrorDomain Code 261) — Unsupported Encoding"
description: "Fix macOS NSFileReadUnsupportedEncoding (NSCocoaErrorDomain Code 261). Resolve Foundation unsupported encoding read errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["nsfilereadunsupportedencoding", "nscocoaerrordomain", "code-261", "file-read", "encoding", "cocoa", "foundation"]
weight: 5
---

# macOS NSFileReadUnsupportedEncoding (NSCocoaErrorDomain Code 261) — Unsupported Encoding

NSFileReadUnsupportedEncoding (error code 261 in NSCocoaErrorDomain) indicates that the string encoding used to read the file is not supported by the system or is incompatible with the file's actual encoding. This error occurs when the specified encoding cannot decode the file's byte sequence, or the encoding itself is invalid or obsolete.

## Common Causes

- The file's actual encoding does not match the encoding specified for reading
- The encoding is deprecated or no longer supported by the current macOS version
- The file contains invalid byte sequences for the chosen encoding
- A BOM (Byte Order Mark) in the file conflicts with the specified encoding
- The file uses an encoding that the application does not have a codec for

## How to Fix NSFileReadUnsupportedEncoding

### 1. Detect the File's Actual Encoding

Determine the encoding before attempting to read:

```bash
# Detect file encoding
file -I /path/to/file
chardetect /path/to/file

# Examine the file's BOM (if present)
xxd /path/to/file | head -1
```

### 2. Use UTF-8 as the Default Encoding

Read the file using UTF-8, which covers most modern content:

```bash
# Read a file with explicit UTF-8 encoding
iconv -f UTF-8 -t UTF-8 /path/to/file > /dev/null

# Convert from a detected encoding to UTF-8
iconv -f SHIFT_JIS -t UTF-8 /path/to/file > /path/to/file.utf8
```

### 3. Specify the Correct Encoding in Code

Match the encoding to the file's actual encoding:

```swift
// Read using a specific encoding
let data = try Data(contentsOf: fileURL)
if let string = String(data: data, encoding: .isoLatin1) {
    print(string)
}
```

### 4. Handle Multiple Encodings

Try multiple encodings and use the first successful one:

```swift
let encodings: [String.Encoding] = [.utf8, .isoLatin1, .japaneseEUC, .shiftJIS]
for encoding in encodings {
    if let string = String(data: data, encoding: encoding) {
        print("Successfully decoded with \(encoding)")
        break
    }
}
```

### 5. Use Universal Encoding Detection

Leverage the `NSString` encoding detection API:

```swift
let NSStringEncoding = NSString.stringEncoding(
    for: data,
    encodingOptions: nil,
    convertedString: nil,
    usedLossyConversion: nil
)
```

## Examples

This error commonly occurs when:

- Reading a Shift-JIS encoded file using UTF-8
- Opening a legacy MacRoman-encoded text file on a modern system
- Reading binary data with a text encoding
- The file's BOM indicates UTF-16 but the code specifies UTF-8

## Related Error Codes

- NSFileWriteUnsupportedEncoding (NSCocoaErrorDomain Code 518) — [Write Unsupported Encoding](/os/macos/nserror-12/)
- NSFileWriteIncompatibleEncoding (NSCocoaErrorDomain Code 517) — [Incompatible Encoding](/os/macos/nserror-8/)
- NSFileReadCorruptFile (NSCocoaErrorDomain Code 512) — [Corrupt File](/os/macos/nserror-5/)
- NSFileReadNoSuchFile (NSCocoaErrorDomain Code 260) — [File Not Found](/os/macos/nserror-6/)
