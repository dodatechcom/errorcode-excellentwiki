---
title: "[Solution] Pascal Variant Record Error — How to Fix"
description: "Fix variant record errors in Pascal when using overlapping fields in record variants incorrectly."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1065
---

# Variant Record Error

A variant record (case variant) allows different fields to share the same memory location. Errors occur when writing to one variant and reading from another, or when the case tag is invalid.

## Common Causes

- Writing to variant A then reading variant B (different data interpretation)
- Invalid case tag value when using discriminant variants
- Memory corruption from variant size mismatch
- Forgetting that all variants share the same memory

## How to Fix

### Solution 1 — Use correct variant for data

```pascal
program VariantRecordFix;

type
  TValue = record
    case Integer of
      0: (IntVal: Integer);
      1: (FloatVal: Double);
      2: (StrVal: string[20]);
  end;

var
  V: TValue;
begin
  V.IntVal := 42;        // write as integer
  WriteLn(V.IntVal);     // read as integer — correct

  V.FloatVal := 3.14;    // write as float
  WriteLn(V.FloatVal:0:2); // read as float — correct

  // WRONG: reading StrVal after writing FloatVal
  // WriteLn(V.StrVal);  // garbage — different variant
end.
```

### Solution 2 — Track active variant with tag

```pascal
program TaggedVariant;

type
  TShapeKind = (skCircle, skRect, skTriangle);

  TShape = record
    case Kind: TShapeKind of
      skCircle: (Radius: Double);
      skRect: (Width, Height: Double);
      skTriangle: (Base, Altitude: Double);
  end;

function Area(const S: TShape): Double;
begin
  case S.Kind of
    skCircle:   Result := Pi * S.Radius * S.Radius;
    skRect:     Result := S.Width * S.Height;
    skTriangle: Result := 0.5 * S.Base * S.Altitude;
  else
    Result := 0;
  end;
end;
```

### Solution 3 — Use size assertions

```pascal
program SizeCheck;

type
  TData = record
    case Byte of
      0: (Bytes: array[0..3] of Byte);
      1: (Int32: Integer);
  end;

begin
  Assert(SizeOf(TData) = SizeOf(Integer));
end.
```

### Solution 4 — Use packed records for alignment control

```pascal
program PackedVariant;

type
  TNetworkPacket = packed record
    case Byte of
      0: (Raw: array[0..3] of Byte);
      1: (Header: Word; Payload: Word);
  end;
```

## Examples

A network protocol parser uses a variant record to interpret packet headers. It writes to the `Header` variant (2 bytes) and reads from `Payload` (2 bytes). Since both share the same memory, reading `Payload` returns the raw header bytes. The fix is to use the correct variant after checking the packet type.

## Related Errors

- [Packed Record Error](/languages/pascal/pascal-packed-record-error) — memory layout
- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — type compatibility
- [Memory Leak](/languages/pascal/pascal-memory-leak-error) — allocation issues
