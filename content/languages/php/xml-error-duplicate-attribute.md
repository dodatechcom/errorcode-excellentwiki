---
title: "[Solution] PHP XML_ERROR_DUPLICATE_ATTRIBUTE — Same Attribute Appears Twice"
description: "Fix PHP XML_ERROR_DUPLICATE_ATTRIBUTE by removing duplicate attributes, checking attribute names, and validating XML structure. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 8
---

# PHP XML_ERROR_DUPLICATE_ATTRIBUTE — Same Attribute Appears Twice

XML_ERROR_DUPLICATE_ATTRIBUTE occurs when the same attribute name appears twice in a single XML element. XML specification requires that each attribute name must be unique within an element. This error is common when generating XML programmatically or when concatenating XML fragments.

## Common Causes

```php
// Programmatic duplication
$xml = '<?xml version="1.0"?><root id="1" id="2">Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_DUPLICATE_ATTRIBUTE
```

```php
// Template concatenation error
$template = '<root %s>%s</root>';
$attributes = 'id="1" id="2"';
$xml = sprintf($template, $attributes, 'Content');
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_DUPLICATE_ATTRIBUTE
```

```php
// Merge conflict in XML
$xml = '<?xml version="1.0"?><root id="1" id="2" name="test">Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_DUPLICATE_ATTRIBUTE
```

```php
// Incorrect attribute building
$xml = '<root';
$xml .= ' id="1"';
$xml .= ' id="2"'; // Duplicate
$xml .= '>Content</root>';
```

```php
// Copy-paste error
$xml = '<?xml version="1.0"?><item name="test" name="duplicate" value="10">Content</item>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_DUPLICATE_ATTRIBUTE
```

## How to Fix

### Fix 1: Remove Duplicate Attributes

Check and remove duplicates before parsing:

```php
function removeDuplicateAttributes($xml) {
    preg_match_all('/<(\w+)([^>]*)>/', $xml, $matches);
    
    foreach ($matches[0] as $index => $element) {
        $attrs = $matches[2][$index];
        preg_match_all('/(\w+)=/', $attrs, $attrMatches);
        
        $seen = [];
        $uniqueAttrs = '';
        preg_match_all('/(\w+="[^"]*")/', $attrs, $attrPairs);
        
        foreach ($attrPairs[1] as $attr) {
            preg_match('/^(\w+)=/', $attr, $nameMatch);
            $name = $nameMatch[1];
            
            if (!isset($seen[$name])) {
                $seen[$name] = true;
                $uniqueAttrs .= ' ' . $attr;
            }
        }
        
        $newElement = '<' . $matches[1][$index] . $uniqueAttrs . '>';
        $xml = str_replace($element, $newElement, $xml);
    }
    
    return $xml;
}
```

### Fix 2: Check Attribute Names

Validate attribute uniqueness before assembly:

```php
function buildXmlElement($tag, $attributes) {
    $seen = [];
    $attrString = '';
    
    foreach ($attributes as $name => $value) {
        if (isset($seen[$name])) {
            continue; // Skip duplicate
        }
        $seen[$name] = true;
        $attrString .= " $name=\"" . htmlspecialchars($value) . "\"";
    }
    
    return "<$tag$attrString/>";
}
```

### Fix 3: Validate XML Structure

Use DOM to validate attribute uniqueness:

```php
function validateAttributeUniqueness($xml) {
    libxml_use_internal_errors(true);
    $doc = new DOMDocument();
    $result = $doc->loadXML($xml);
    $errors = libxml_get_errors();
    libxml_clear_errors();
    
    $duplicateErrors = array_filter($errors, function($error) {
        return strpos($error->message, 'duplicate') !== false;
    });
    
    return empty($duplicateErrors);
}
```

### Fix 4: Use Array for Attributes

Build attributes using arrays to prevent duplicates:

```php
$attributes = [
    'id' => '1',
    'name' => 'test',
    'value' => '10'
];

// Automatically prevents duplicates
$attrString = '';
foreach ($attributes as $key => $value) {
    $attrString .= " $key=\"" . htmlspecialchars($value) . "\"";
}

$xml = "<root$attrString>Content</root>";
```

### Fix 5: Merge Attributes

Combine duplicate attributes intelligently:

```php
function mergeDuplicateAttributes($xml) {
    preg_match_all('/<(\w+)([^>]*)>/', $xml, $matches);
    
    foreach ($matches[0] as $index => $element) {
        $attrs = $matches[2][$index];
        $merged = [];
        
        preg_match_all('/(\w+)="([^"]*)"/', $attrs, $attrMatches, PREG_SET_ORDER);
        
        foreach ($attrMatches as $attr) {
            $merged[$attr[1]] = $attr[2]; // Last value wins
        }
        
        $newAttrs = '';
        foreach ($merged as $key => $value) {
            $newAttrs .= " $key=\"$value\"";
        }
        
        $newElement = '<' . $matches[1][$index] . $newAttrs . '>';
        $xml = str_replace($element, $newElement, $xml);
    }
    
    return $xml;
}
```

## Examples

```php
// Basic duplicate attribute detection
$xml = '<?xml version="1.0"?><root id="1" id="2">Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_DUPLICATE_ATTRIBUTE) {
    echo "Duplicate attribute found";
}
xml_parser_free($parser);
```

```php
// Find and report duplicates
function findDuplicateAttributes($xml) {
    $duplicates = [];
    
    preg_match_all('/<(\w+)([^>]*)>/', $xml, $matches);
    
    foreach ($matches[0] as $index => $element) {
        $attrs = $matches[2][$index];
        preg_match_all('/(\w+)="([^"]*)"/', $attrs, $attrMatches, PREG_SET_ORDER);
        
        $seen = [];
        foreach ($attrMatches as $attr) {
            if (isset($seen[$attr[1]])) {
                $duplicates[] = [
                    'element' => $matches[1][$index],
                    'attribute' => $attr[1]
                ];
            }
            $seen[$attr[1]] = true;
        }
    }
    
    return $duplicates;
}

$xml = '<?xml version="1.0"?><root id="1" id="2">Content</root>';
$duplicates = findDuplicateAttributes($xml);
print_r($duplicates);
```

```php
// Safe XML builder with duplicate prevention
class XmlBuilder {
    private $elements = [];
    
    public function addElement($tag, $attributes) {
        $unique = [];
        foreach ($attributes as $key => $value) {
            if (!isset($unique[$key])) {
                $unique[$key] = $value;
            }
        }
        
        $this->elements[] = [
            'tag' => $tag,
            'attributes' => $unique
        ];
    }
    
    public function build() {
        $xml = '<?xml version="1.0" encoding="UTF-8"?>';
        $xml .= '<root>';
        
        foreach ($this->elements as $element) {
            $attrs = '';
            foreach ($element['attributes'] as $key => $value) {
                $attrs .= " $key=\"" . htmlspecialchars($value) . "\"";
            }
            $xml .= "<{$element['tag']}$attrs/>";
        }
        
        $xml .= '</root>';
        return $xml;
    }
}
```

## Related Errors

- [XML_ERROR_SYNTAX](xml-error-syntax.md) - XML syntax error
- [XML_ERROR_INVALID_TOKEN](xml-error-invalid-token.md) - Invalid token in XML
- [XML_ERROR_TAG_MISMATCH](xml-error-tag-mismatch.md) - Opening and closing tags don't match