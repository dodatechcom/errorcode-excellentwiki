---
title: "[Solution] Dart Rune Error — Invalid Index, Characters, Grapheme Clusters"
description: "Fix Dart errors when accessing runes at invalid indices. Understand Unicode code units, grapheme clusters, and the characters package."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 104
---

Rune errors occur when accessing a character position in a string that does not correspond to a valid Unicode code point, especially with multi-byte characters like emoji.

## Common Causes

1. Treating `string[index]` as character-based when it uses UTF-16 code units.
2. Accessing a string index that splits a surrogate pair (emoji, CJK extensions).
3. Using `runes` property incorrectly — not converting to a list first.
4. Assuming `length` equals the number of visible characters.
5. Slicing strings at byte boundaries rather than code point boundaries.

## How to Fix It

**Solution 1: Use the `characters` package for grapheme-safe operations**

```dart
import 'package:characters/characters.dart';

void main() {
  String emoji = 'Hello 🌍';
  
  // Characters package treats grapheme clusters as single units
  print(emoji.characters.length); // 7 (not 9)
  print(emoji.characters.first);  // H
  print(emoji.characters.last);   // 🌍
}
```

**Solution 2: Work with `runes` as a list**

```dart
void main() {
  String text = 'Dart 🎯';
  
  List<int> runeList = text.runes.toList();
  print(runeList.length); // 6
  print(String.fromCharCode(runeList.last)); // 🎯
}
```

**Solution 3: Avoid splitting surrogate pairs**

```dart
void main() {
  String emoji = 'Hi 😀';
  
  // Wrong: string index splits the emoji
  // print(emoji[3]); // may produce garbage
  
  // Correct: use runes
  int rune = emoji.runes.elementAt(3);
  print(String.fromCharCode(rune)); // 😀
}
```

**Solution 4: Count visible characters correctly**

```dart
import 'package:characters/characters.dart';

void main() {
  String name = 'José 🇯🇵';
  
  print(name.length);               // 10 (code units)
  print(name.runes.length);         // 8 (code points)
  print(name.characters.length);    // 8 (grapheme clusters)
}
```

**Solution 5: Convert between code points and strings safely**

```dart
void main() {
  int codePoint = 0x1F600; // 😀
  
  String emoji = String.fromCharCode(codePoint);
  print(emoji); // 😀
  
  // For supplementary plane characters, use fromCharCodes
  String combined = String.fromCharCodes([0x1F1FA, 0x1F1F8]); // 🇺🇸
  print(combined);
}
```

## Examples

Dart strings are encoded in UTF-16. Characters outside the Basic Multilingual Plane (like most emoji) use two UTF-16 code units (a surrogate pair). `string[index]` accesses a single UTF-16 code unit, which may not be a complete character.

## Related Errors

- [Dart String Concat Error](/languages/dart/dart-string-concat-error/)
- [Dart URI Encode Error](/languages/dart/dart-uri-encode-error/)
- [Dart RegExp Error](/languages/dart/dart-regexp-error/)
