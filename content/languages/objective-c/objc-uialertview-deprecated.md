---
title: "Objective-C UIAlertView Deprecated iOS Error"
description: "Fix Objective-C UIAlertView deprecation errors by migrating to UIAlertController on iOS 8 and later."
languages: ["objective-c"]
error-types: ["compile-error"]
severities: ["warning"]
weight: 5
---

## Common Causes

- UIAlertView deprecated since iOS 8
- Using UIAlertView with block-based callbacks (never supported)
- Presentation on wrong view controller
- Not handling device rotation with UIAlertView
- UIActionSheet also deprecated, same migration needed

## How to Fix

```objc
// WRONG: Using deprecated UIAlertView
UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Error"
    message:@"Something went wrong"
    delegate:self
    cancelButtonTitle:@"OK"
    otherButtonTitles:nil];
[alert show];

// CORRECT: Use UIAlertController
UIAlertController *alert = [UIAlertController
    alertControllerWithTitle:@"Error"
    message:@"Something went wrong"
    preferredStyle:UIAlertControllerStyleAlert];
[alert addAction:[UIAlertAction actionWithTitle:@"OK"
    style:UIAlertActionStyleDefault handler:nil]];
[self presentViewController:alert animated:YES completion:nil];
```

```objc
// WRONG: UIAlertView delegate pattern
- (void)alertView:(UIAlertView *)alertView
    clickedButtonAtIndex:(NSInteger)buttonIndex {
    // deprecated pattern
}

// CORRECT: Action handler in block
UIAlertAction *okAction = [UIAlertAction actionWithTitle:@"OK"
    style:UIAlertActionStyleDefault
    handler:^(UIAlertAction *action) {
        [self handleConfirmation];
    }];
```

## Examples

```objc
// Example 1: Basic alert
UIAlertController *alert = [UIAlertController
    alertControllerWithTitle:@"Title"
    message:@"Message"
    preferredStyle:UIAlertControllerStyleAlert];
[alert addAction:[UIAlertAction actionWithTitle:@"OK"
    style:UIAlertActionStyleDefault handler:nil]];
[self presentViewController:alert animated:YES completion:nil];

// Example 2: Alert with text field
UIAlertController *alert = [UIAlertController
    alertControllerWithTitle:@"Login"
    message:@"Enter credentials"
    preferredStyle:UIAlertControllerStyleAlert];
[alert addTextFieldWithConfigurationHandler:^(UITextField *tf) {
    tf.placeholder = @"Username";
}];
UIAlertAction *login = [UIAlertAction actionWithTitle:@"Login"
    style:UIAlertActionStyleDefault handler:^(UIAlertAction *action) {
        NSString *user = alert.textFields.firstObject.text;
    }];
[alert addAction:login];
[self presentViewController:alert animated:YES completion:nil];

// Example 3: Action sheet
UIAlertController *sheet = [UIAlertController
    alertControllerWithTitle:@"Choose"
    message:nil
    preferredStyle:UIAlertControllerStyleActionSheet];
[sheet addAction:[UIAlertAction actionWithTitle:@"Camera"
    style:UIAlertActionStyleDefault handler:nil]];
[sheet addAction:[UIAlertAction actionWithTitle:@"Cancel"
    style:UIAlertActionStyleCancel handler:nil]];
[self presentViewController:sheet animated:YES completion:nil];
```

## Related Errors

- [UIKit error](objc-uikit-error) -- UIKit framework issues
- [Modal view error](objc-modal-view-error) -- presentation issues
