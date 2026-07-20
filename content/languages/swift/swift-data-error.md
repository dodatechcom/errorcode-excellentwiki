---
title: "[Solution] Swift Data Error — Count, Bridging & Memory Mapping"
description: "Fix Swift Data errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 123
---

`Data` errors occur when count/length validation fails, NSData bridging produces incorrect results, or memory mapping operations fail.

## Common Causes

```swift
// Out of bounds access
let data = Data([0x01, 0x02])
let byte = data[5] // Crash: index out of bounds

// NSData bridging issues
let nsData: NSData = NSData()
let data: Data = nsData as Data // May copy unexpectedly
```

## How to Fix

**1. Safe Data access**

```swift
let data = Data([0x01, 0x02, 0x03])

if data.indices.contains(2) {
    let byte = data[2]
    print(byte)
}

// Use subdata
let sub = data.subdata(in: 1..<3)
```

**2. Append Data safely**

```swift
var data = Data()
data.append(Data([0x01]))
data.append(contentsOf: [0x02, 0x03])
data.append(Data([0x04]))
```

**3. Convert between Data and bytes**

```swift
let bytes: [UInt8] = [0x48, 0x65, 0x6C, 0x6C, 0x6F]
let data = Data(bytes)

let backToBytes = [UInt8](data)
print(String(bytes: backToBytes, encoding: .utf8) ?? "")
```

**4. Memory mapped Data**

```swift
let url = URL(fileURLWithPath: "/path/to/file")
let data = try Data(contentsOf: url, options: .mappedIfSafe)
// Data is memory-mapped, not copied
```

**5. Validate Data before processing**

```swift
func process(_ data: Data) throws {
    guard data.count >= 4 else {
        throw DataError.insufficientData(expected: 4, actual: data.count)
    }
    
    let header = data.prefix(4)
    // Process header
}
```

## Examples

Complete Data handling:
```swift
struct DataProcessor {
    static func combine(_ datas: [Data]) -> Data {
        var result = Data()
        for data in datas {
            result.append(data)
        }
        return result
    }
    
    static func chunk(_ data: Data, size: Int) -> [Data] {
        stride(from: 0, to: data.count, by: size).map { start in
            let end = min(start + size, data.count)
            return data.subdata(in: start..<end)
        }
    }
    
    static func hex(_ data: Data) -> String {
        data.map { String(format: "%02x", $0) }.joined()
    }
}
```

## Related Errors

- [JSONDecoder Error](/languages/swift/swift-jsondecoder-error)
- [Property List Error](/languages/swift/swift-property-list-error)
- [CryptoKit Error](/languages/swift/swift-cryptokit-error)
