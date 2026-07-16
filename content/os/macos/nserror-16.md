---
title: "[Solution] macOS NSFileStreamErrorMaximum (NSCocoaErrorDomain Code 2095) — Stream Error Maximum"
description: "Fix macOS NSFileStreamErrorMaximum (NSCocoaErrorDomain Code 2095). Resolve Foundation stream error maximum boundary errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["nsfstreamerrormaximum", "nscocoaerrordomain", "code-2095", "stream", "cocoa", "foundation"]
weight: 5
---

# macOS NSFileStreamErrorMaximum (NSCocoaErrorDomain Code 2095) — Stream Error Maximum

NSFileStreamErrorMaximum (error code 2095 in NSCocoaErrorDomain) is the upper bound of the `NSStream` error code range. This error indicates that a stream-related operation has failed with a code at the maximum end of the stream error range (2048–2095). It typically represents a fatal or unrecoverable stream condition such as a broken pipe, unexpected end of stream, or critical I/O failure.

## Common Causes

- The stream encountered a fatal I/O error that cannot be recovered from
- A broken pipe or unexpected stream termination occurred
- The stream's underlying file descriptor or socket was closed unexpectedly
- A critical resource (memory, file handle) became unavailable during stream processing
- The stream operation was performed on a stream in an invalid state

## How to Fix NSFileStreamErrorMaximum

### 1. Retrieve the Actual Error Code

Extract the specific error from the stream's `streamError` property:

```swift
if let streamError = outputStream.streamError as NSError? {
    print("Error domain: \(streamError.domain)")
    print("Error code: \(streamError.code)")
    print("userInfo: \(streamError.userInfo)")
}
```

### 2. Check Stream State Before Operations

Verify the stream is open and in a valid state before performing operations:

```swift
guard stream.streamStatus == .open else {
    print("Stream is not open. Status: \(stream.streamStatus.rawValue)")
    if let error = stream.streamError {
        print("Error: \(error.localizedDescription)")
    }
    return
}
```

### 3. Implement Robust Error Handling in Delegates

Handle all stream events including error conditions:

```swift
func stream(_ aStream: Stream, handle eventCode: Stream.Event) {
    switch eventCode {
    case .errorOccurred:
        aStream.close()
        aStream.remove(from: .current, forMode: .default)
        print("Fatal stream error: \(aStream.streamError?.localizedDescription ?? "unknown")")
    case .endEncountered:
        aStream.close()
    case .hasSpaceAvailable, .hasBytesAvailable:
        // Proceed with read/write
        break
    default:
        break
    }
}
```

### 4. Monitor File Descriptors

Check for file descriptor exhaustion on the system:

```bash
# Check open file descriptors for the process
lsof -p <PID> | wc -l

# Check system-wide file descriptor limits
sysctl kern.maxfiles
sysctl kern.maxfilesperproc
```

### 5. Implement Graceful Stream Recovery

Close and recreate the stream on fatal errors:

```swift
func recreateStream(url: URL) -> InputStream? {
    stream?.close()
    stream?.remove(from: .current, forMode: .default)
    let newStream = InputStream(url: url)
    newStream?.schedule(in: .current, forMode: .default)
    newStream?.open()
    return newStream
}
```

## Examples

This error commonly occurs when:

- A socket stream is forcefully disconnected during a large data transfer
- A file stream encounters the end of the underlying file during a blocking read
- The system runs out of file descriptors, preventing stream operations
- A stream delegate is deallocated while the stream is still active

## Related Error Codes

- NSFileStreamErrorMinimum (NSCocoaErrorDomain Code 2048) — [Stream Error Minimum](/os/macos/nserror-15/)
- NSFileReadCorruptFile (NSCocoaErrorDomain Code 512) — [Corrupt File](/os/macos/nserror-5/)
- NSFileWriteUnknownError (NSCocoaErrorDomain Code 513) — [Write Unknown Error](/os/macos/nserror-2/)
- NSFileReadUnknownError (NSCocoaErrorDomain Code 256) — [Read Unknown Error](/os/macos/nserror-1/)
