---
title: "Objective-C UIPickerView DataSource Error"
description: "Fix Objective-C UIPickerView datasource errors when returning invalid component or row counts."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- numberOfRowsInComponent returns wrong count
- titleForRow returns nil instead of NSString
- selectedRow in component exceeds actual row count
- Data source changes while picker is visible
- Not implementing all required UIPickerViewDataSource methods

## How to Fix

```objc
// WRONG: Returning nil from titleForRow
- (NSString *)pickerView:(UIPickerView *)pickerView
    titleForRow:(NSInteger)row
    forComponent:(NSInteger)component {
    return nil; // crash when picker displays
}

// CORRECT: Always return non-nil string
- (NSString *)pickerView:(UIPickerView *)pickerView
    titleForRow:(NSInteger)row
    forComponent:(NSInteger)component {
    return self.items[row] ?: @"";
}
```

```enrl
// WRONG: Data source array out of sync
- (NSInteger)pickerView:(UIPickerView *)pickerView
    numberOfRowsInComponent:(NSInteger)component {
    return self.items.count; // but self.items may be empty or nil
}

// CORRECT: Safe count
- (NSInteger)pickerView:(UIPickerView *)pickerView
    numberOfRowsInComponent:(NSInteger)component {
    return self.items.count;
}
```

## Examples

```objc
// Example 1: Complete picker delegate
- (NSInteger)numberOfComponentsInPickerView:(UIPickerView *)pickerView {
    return 1;
}

- (NSInteger)pickerView:(UIPickerView *)pickerView
    numberOfRowsInComponent:(NSInteger)component {
    return self.colors.count;
}

- (NSString *)pickerView:(UIPickerView *)pickerView
    titleForRow:(NSInteger)row
    forComponent:(NSInteger)component {
    return self.colors[row];
}

- (void)pickerView:(UIPickerView *)pickerView
    didSelectRow:(NSInteger)row
    inComponent:(NSInteger)component {
    self.selectedColor = self.colors[row];
}

// Example 2: Reload picker data
[self.colorPicker reloadAllComponents];
[self.colorPicker selectRow:0 inComponent:0 animated:YES];
```

## Related Errors

- [Picker view error](objc-uikit-error) -- UIPickerView issues
- [UITableView datasource error](objc-uitableview-error) -- data source problems
