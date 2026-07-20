---
title: "[Solution] PHP XML_ERROR_NONE — No Error During Parsing"
description: "Fix PHP XML_ERROR_NONE by ensuring proper parser initialization. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 0
---

# PHP XML_ERROR_NONE — No Error During Parsing

XML_ERROR_NONE indicates that no error occurred during XML parsing. This is the success code (value 0) returned by `xml_get_error_code()` when parsing completes without issues. While not an error itself, encountering this code confirms your XML parser is functioning correctly.

## Common Causes

```php
// Proper parser initialization
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser); // Returns XML_ERROR_NONE (0)
```

```php
// Valid XML document parsing
$xml = '<?xml version="1.0"?><root><child>Content</child></root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser); // Returns XML_ERROR_NONE (0)
```

```php
// Complete XML document with proper structure
$xml = '<?xml version="1.0" encoding="UTF-8"?>
<catalog>
    <book>
        <title>Example Book</title>
    </book>
</catalog>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser); // Returns XML_ERROR_NONE (0)
```

```php
// Checking for success after parsing
$parser = xml_parser_create();
$result = xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_NONE) {
    echo "Parsing successful!";
}
```

```php
// Multi-byte safe parsing
$xml = '<?xml version="1.0" encoding="UTF-8"?><root><text>Hello World</text></root>';
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $xml);
$error = xml_get_error_code($parser); // Returns XML_ERROR_NONE (0)
```

## How to Fix

### Fix 1: Confirm Parser Initialization

Ensure the parser is properly created before use:

```php
$parser = xml_parser_create();
if ($parser === false) {
    die("Failed to create parser");
}
xml_parse($parser, $xml);
if (xml_get_error_code($parser) === XML_ERROR_NONE) {
    echo "No errors found";
}
xml_parser_free($parser);
```

### Fix 2: Validate XML Before Parsing

Check that your XML string is valid before passing to the parser:

```php
$xml = trim($xml);
if (empty($xml)) {
    die("Empty XML string");
}
$parser = xml_parser_create();
xml_parse($parser, $xml);
if (xml_get_error_code($parser) === XML_ERROR_NONE) {
    echo "Parsing successful";
}
xml_parser_free($parser);
```

## Examples

```php
// Basic success check
$parser = xml_parser_create();
xml_parse($parser, '<root/>');
$code = xml_get_error_code($parser);
var_dump($code); // int(0) - XML_ERROR_NONE
xml_parser_free($parser);
```

```php
// Complete workflow
$xml = '<?xml version="1.0" encoding="UTF-8"?><data><item id="1">Value</item></data>';
$parser = xml_parser_create();
xml_set_element_handler($parser, 'startElement', 'endElement');
xml_parse($parser, $xml);
if (xml_get_error_code($parser) === XML_ERROR_NONE) {
    echo "Parsed successfully with " . xml_get_current_line_number($parser) . " lines";
}
xml_parser_free($parser);
```

```php
// Loop checking multiple documents
$documents = [
    '<root>Doc1</root>',
    '<root>Doc2</root>',
    '<root>Doc3</root>'
];
foreach ($documents as $xml) {
    $parser = xml_parser_create();
    xml_parse($parser, $xml);
    if (xml_get_error_code($parser) === XML_ERROR_NONE) {
        echo "Document parsed successfully\n";
    }
    xml_parser_free($parser);
}
```

## Related Errors

- [XML_ERROR_NO_MEMORY](xml-error-no-memory.md) - Parser ran out of memory
- [XML_ERROR_SYNTAX](xml-error-syntax.md) - XML syntax error
- [XML_ERROR_NO_ELEMENTS](xml-error-no-elements.md) - No elements found in XML