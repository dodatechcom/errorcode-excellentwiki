---
title: "[Solution] Rails Active Storage Upload Error"
description: "Fix Rails Active Storage file upload failures. Resolve active_storage_direct_uploads error in Rails applications."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Active Storage fails to upload a file due to misconfiguration, storage service issues, or file size limits.

## Common Causes

- Storage service not configured in `config/storage.yml`
- Disk service directory does not exist or has wrong permissions
- File exceeds `ActiveStorage::Blob` size limit
- Direct upload JavaScript not properly configured
- S3 bucket does not exist or credentials are wrong

## How to Fix

1. Configure storage in `config/storage.yml`:

```yaml
local:
  service: Disk
  root: <%= Rails.root.join("storage") %>

amazon:
  service: S3
  access_key_id: <%= ENV["AWS_ACCESS_KEY_ID"] %>
  secret_access_key: <%= ENV["AWS_SECRET_ACCESS_KEY"] %>
  region: us-east-1
  bucket: your-bucket-name
```

2. Set the active service in the environment:

```ruby
# config/environments/production.rb
config.active_storage.service = :amazon
```

3. Add file size validation:

```ruby
class User < ApplicationRecord
  has_one_attached :avatar

  validate :avatar_size

  private

  def avatar_size
    if avatar.attached? && avatar.byte_size > 5.megabytes
      errors.add(:avatar, "must be less than 5MB")
    end
  end
end
```

4. Ensure the storage directory exists:

```bash
mkdir -p storage
chmod 775 storage
```

## Examples

```ruby
# Upload fails without configured service
user.avatar.attach(params[:avatar])
# ActiveStorage::FileNotFoundError: Disk storage cannot find file

# S3 upload fails with wrong credentials
user.avatar.attach(params[:upload])
# Aws::S3::Errors::InvalidAccessKeyId: The AWS Access Key Id you provided does not exist
```
