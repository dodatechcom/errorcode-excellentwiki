---
title: "[Solution] MATLAB xmlread/xmlwrite — DOM Parse, XPath, Namespace"
description: "Fix MATLAB xmlread/xmlwrite errors: DOM parsing, XPath queries, XML namespaces, and Java interop."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 143
---

## Common Causes

- Malformed XML causing `xmlread` parse failure
- XPath expression not finding nodes due to namespace issues
- `xmlwrite` producing invalid XML from incomplete DOM
- Java DOM API errors from incorrect node manipulation
- Namespace prefixes not registered before XPath queries

## How to Fix

```matlab
% WRONG: xmlread on malformed XML
doc = xmlread('invalid.xml');  % Error: not well-formed

% CORRECT: Validate XML first
try
    doc = xmlread('data.xml');
catch ME
    error('Invalid XML: %s', ME.message);
end
```

```matlab
% WRONG: XPath without namespace handling
doc = xmlread('namespaced.xml');
nodes = doc.getElementsByTagName('item');  % Empty if namespaced

% CORRECT: Use XPath with namespace
import javax.xml.xpath.*
factory = XPathFactory.newInstance;
xpath = factory.newXPath;

% Register namespace
namespaceContext = javax.xml.namespace.SimpleNamespaceContext;
namespaceContext.addNamespace('ns', 'http://example.com/schema');
xpath.setNamespaceContext(namespaceContext);

expression = xpath.compile('//ns:item');
nodes = expression.evaluate(doc, XPathConstants.NODESET);
```

```matlab
% CORRECT: Create XML from scratch with proper structure
docNode = com.mathworks.xml.XMLUtils.createDocument('root');
docRootNode = docNode.getDocumentElement;

% Add child element
itemNode = docNode.createElement('item');
itemNode.setAttribute('id', '1');
itemNode.appendChild(docNode.createTextNode('value'));
docRootNode.appendChild(itemNode);

% Write to file
xmlwrite('output.xml', docNode);
```

```matlab
% CORRECT: Read XML attributes
doc = xmlread('data.xml');
items = doc.getElementsByTagName('item');
for k = 0:items.getLength-1
    item = items.item(k);
    id = char(item.getAttribute('id'));
    value = char(item.getTextContent);
    fprintf('id=%s, value=%s\n', id, value);
end
```

```matlab
% CORRECT: Parse XML to struct
function S = xml2struct(filename)
    doc = xmlread(filename);
    S = parseNode(doc.getDocumentElement);
end

function S = parseNode(node)
    S = struct();
    S.name = char(node.getTagName);
    S.attributes = struct();
    attrs = node.getAttributes;
    for k = 0:attrs.getLength-1
        attr = attrs.item(k);
        S.attributes.(char(attr.getName)) = char(attr.getValue);
    end
end
```

## Examples

```matlab
% Example: Extract data from XML configuration
doc = xmlread('config.xml');
root = doc.getDocumentElement;
servers = root.getElementsByTagName('server');

for k = 0:servers.getLength-1
    server = servers.item(k);
    host = char(server.getAttribute('host'));
    port = str2double(char(server.getAttribute('port')));
    fprintf('Server: %s:%d\n', host, port);
end
```

## Related Errors

- [HDF5 Error](matlab-hdf5-error) — structured data files
- [fopen Error](matlab-fopen) — file access
- [textscan](matlab-textscan) — text parsing
