---
title: "[Solution] Linux EILSEQ (errno 52) — Invalid or Incomplete Multibyte Fix"
description: "Fix Linux EILSEQ (errno 52) Invalid or incomplete multibyte or wide-character error. Solutions for character encoding issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EILSEQ (errno 52) — Invalid or Incomplete Multibyte

EILSEQ (errno 52) means an invalid multibyte character was encountered in a string. This error occurs when a function like `mbrtowc()` or `mbtowc()` encounters a byte sequence that does not form a valid character in the current locale encoding. It is distinct from EINVAL (errno 22) because EILSEQ specifically refers to encoding errors, not general argument problems.

## Common Causes

- File contents contain bytes invalid for the current locale encoding
- Data transferred between systems with different encodings (e.g., Latin-1 vs UTF-8)
- Corrupted file data in text processing operations
- Incorrect locale configuration on the system

## How to Fix EILSEQ

### 1. Check Current Locale Settings

Verify the active locale and encoding:

```bash
locale
echo $LANG
```

### 2. Set UTF-8 Locale

Ensure UTF-8 is configured:

```bash
sudo localectl set-locale LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### 3. Convert File Encoding

Convert files to the correct encoding:

```bash
# Convert from Latin-1 to UTF-8
iconv -f ISO-8859-1 -t UTF-8 input.txt > output.txt

# Convert from Windows CP1252 to UTF-8
iconv -f CP1252 -t UTF-8 input.txt > output.txt
```

### 4. Use Byte-Handling Mode

Process the file as raw bytes when encoding is unknown:

```bash
LC_ALL=C grep -P '[^\x00-\x7F]' file.txt
```

### 5. Detect File Encoding

Identify the actual encoding of a file:

```bash
file -i file.txt
chardetect file.txt
```

## Verification

After converting the encoding, confirm the file processes without error:

```bash
LC_ALL=en_US.UTF-8 cat file.txt
```

## Related Error Codes

- [EINVAL (errno 22)](/os/linux/errno-22/) — Invalid argument
- [EILSEQ (errno 84)](/os/linux/errno-84/) — Invalid or incomplete multibyte
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
