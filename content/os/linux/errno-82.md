---
title: "[Solution] Linux EILSEQ (errno 82) — Invalid or Incomplete Multibyte Fix"
description: "Fix Linux EILSEQ (errno 82) Invalid or incomplete multibyte or wide-character error. Solutions for wide-character encoding issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eilseq", "encoding", "errno-82", "multibyte", "wchar"]
weight: 5
---

# Linux EILSEQ (errno 82) — Invalid or Incomplete Multibyte

EILSEQ (errno 82) means an invalid or incomplete multibyte or wide character was encountered. This error occurs when wide-character functions like `wcrtomb()` or `mbsrtowcs()` encounter byte sequences that cannot be converted. It is distinct from EILSEQ (errno 52) because errno 82 is the POSIX definition used by wide-character functions specifically.

## Common Causes

- Invalid byte sequence in wide-character conversion
- Truncated multibyte sequence at end of buffer
- Incorrect locale setting for the character encoding
- Data from external source with incompatible encoding

## How to Fix EILSEQ

### 1. Verify Locale Configuration

Check the current locale and character encoding:

```bash
locale
locale -a
echo $LC_CTYPE
```

### 2. Set Correct Locale

Ensure UTF-8 locale is configured:

```bash
export LC_CTYPE=en_US.UTF-8
export LANG=en_US.UTF-8
```

### 3. Convert Data to Correct Encoding

Convert input data before processing:

```bash
iconv -f ISO-8859-1 -t UTF-8 input.txt > output.txt
```

### 4. Use iconv in Applications

Handle encoding conversion programmatically:

```bash
# In shell: convert before processing
file -i input.txt
iconv -f $(file -i input.txt | cut -d= -f2) -t UTF-8 input.txt | process
```

### 5. Handle Truncated Sequences

Check for and handle incomplete multibyte sequences:

```bash
# Detect partial sequences at end of file
tail -c 4 file.txt | xxd
```

## Verification

After correcting the encoding, confirm conversion succeeds:

```bash
LC_ALL=en_US.UTF-8 wc -m file.txt
iconv -f UTF-8 -t UTF-8 file.txt > /dev/null
```

## Related Error Codes

- [EINVAL (errno 22)](/os/linux/errno-22/) — Invalid argument
- [EILSEQ (errno 52)](/os/linux/errno-52/) — Invalid or incomplete multibyte
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
