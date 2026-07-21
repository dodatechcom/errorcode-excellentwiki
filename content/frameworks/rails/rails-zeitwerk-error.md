---
title: "[Solution] Rails Zeitwerk Autoloader Error"
description: "Fix Rails Zeitwerk autoloading errors. Resolve expected file to define constant mismatch in Rails autoloading."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when the Zeitwerk autoloader finds a file whose path does not match the constant it defines.

## Common Causes

- File named `payment_processor.rb` defines `class Payment` instead of `PaymentProcessor`
- Constant defined in a subdirectory that does not match its namespace
- File was renamed but the constant inside was not updated
- Module nesting does not match directory structure
- Custom inflections cause path-constant mismatch

## How to Fix

1. Ensure file name and constant name match:

```ruby
# app/services/payment_processor.rb
class PaymentProcessor  # matches file name
  def call
    # ...
  end
end
```

2. For namespaced classes, match the directory:

```ruby
# app/services/billing/invoice_generator.rb
module Billing
  class InvoiceGenerator  # matches Billing::InvoiceGenerator
    def generate
      # ...
    end
  end
end
```

3. Add custom inflections if needed:

```ruby
# config/initializers/inflections.rb
ActiveSupport::Inflector.inflections do |inflect|
  inflect.acronym 'API'
  inflect.acronym 'SSL'
end
```

4. Check autoloader paths are correct:

```ruby
# config/application.rb
config.autoload_paths << Rails.root.join('app', 'services')
```

## Examples

```ruby
# Bad: file name does not match constant
# app/services/exporter.rb
class DataExport  # expected Exporter
  # ...
end
# Zeitwerk::NameError: expected file .../exporter.rb to define constant Exporter, got DataExport

# Fix:
class Exporter
  # ...
end
```
