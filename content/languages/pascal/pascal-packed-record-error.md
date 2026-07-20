---
title: "[Solution] Pascal Packed Record Error — How to Fix"
description: "Fix packed record errors in Pascal when bit-level packing causes alignment or access issues."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1081
---

# Packed Record Error

A `packed record` removes alignment padding between fields, reducing size but potentially causing misaligned access. Errors occur when accessing packed fields that cross word boundaries, or when casting packed records to pointers.

## Common Causes

- Accessing a packed field at a non-aligned address causes performance loss or fault
- Misinterpreting packed record layout when different compiler settings are used
- Casting packed record fields to pointers (alignment violation)
- Bitpacked records with bit-level field access causing unexpected values

## How to Fix

### Solution 1 — Use packed for network/file formats

```pascal
program PackedFix;

type
  TNetworkHeader = packed record
    Version: Byte;
    Flags: Byte;
    Length: Word;
    Checksum: Cardinal;
  end;

var
  H: TNetworkHeader;
begin
  FillChar(H, SizeOf(H), 0);
  H.Version := 1;
  H.Length := 1024;
  WriteLn('Size: ', SizeOf(TNetworkHeader));  // 8, not 12
end.
```

### Solution 2 — Be aware of alignment requirements

```pascal
program AlignmentAware;

type
  TAligned = record
    A: Byte;
    B: Integer;
  end;

  TPacked = packed record
    A: Byte;
    B: Integer;
  end;

begin
  WriteLn('Aligned: ', SizeOf(TAligned));    // 8 (with padding)
  WriteLn('Packed: ', SizeOf(TPacked));      // 5 (no padding)
end.
```

### Solution 3 — Use bitpacked records for bit fields

```pascal
program BitPacked;

type
  TFlags = bitpacked record
    Active: 0..1;
    Visible: 0..1;
    Enabled: 0..1;
    Reserved: 0..29;
  end;

var
  F: TFlags;
begin
  F.Active := 1;
  F.Visible := 0;
  F.Enabled := 1;
  WriteLn('Active: ', F.Active);
end.
```

### Solution 4 — Verify packed layout with assertions

```pascal
program VerifyLayout;

type
  TFileRec = packed record
    ID: Word;           // offset 0
    Timestamp: Cardinal; // offset 2
    Value: Byte;        // offset 6
  end;

begin
  Assert(SizeOf(TFileRec) = 7);
  Assert(OffsetOf(TFileRec.Timestamp) = 2);
end.
```

## Examples

A protocol parser uses a packed record to map incoming bytes. Field access is slower because the CPU must use byte-by-byte reads instead of aligned word reads. For performance-critical code, aligning fields (removing `packed`) may be faster despite the larger size.

## Related Errors

- [Variant Record Error](/languages/pascal/pascal-variant-record-error) — overlapping fields
- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — type compatibility
- [Array Bounds Error](/languages/pascal/pascal-array-bounds-error) — memory access
