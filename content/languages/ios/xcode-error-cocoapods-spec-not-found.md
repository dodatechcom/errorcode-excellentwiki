---
title: "[Solution] Xcode Error: CocoaPods Spec Not Found"
description: "Resolve CocoaPods spec repository errors in Xcode projects."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: CocoaPods Spec Not Found

This error appears when CocoaPods cannot find a pod specification in the spec repository. The pod name may be misspelled or the pod may have been removed.

## Common Causes
- Pod name typo in Podfile
- Pod repository not updated locally
- Private pod repository not configured
- Pod removed from public spec repository

## How to Fix
1. Run `pod repo update` to refresh local spec repository
2. Verify the pod name on CocoaPods.org
3. For private pods, add the repository source to Podfile
4. Use the exact pod name from the spec repository

```ruby
# Update CocoaPods spec repository:
# $ pod repo update

# In your Podfile, specify the source if needed:
source 'https://github.com/CocoaPods/Specs.git'
source 'https://github.com/MyCompany/Specs.git'

# Then run:
# $ pod install
```

## Examples
```ruby
# Example Podfile with proper source configuration
source 'https://github.com/CocoaPods/Specs.git'

platform :ios, '15.0'
use_frameworks!

target 'MyApp' do
  pod 'Alamofire', '~> 5.8'
  pod 'Kingfisher', '~> 7.0'
end

post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '15.0'
    end
  end
end
```
