---
title: "[Solution] AWS S3 Object Not Found"
description: "NoSuchKey error when the specified object does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Object Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Object key is incorrect or case-sensitive
- Object was deleted
- Object is in a different bucket
- Versioning enabled and specific version ID does not exist

## How to Fix

### Check object exists

```bash
aws s3api head-object --bucket my-bucket --key path/to/file.txt
```
### List objects with prefix

```bash
aws s3 ls s3://my-bucket/path/to/ --recursive
```
### List object versions

```bash
aws s3api list-object-versions --bucket my-bucket --prefix path/to/file.txt
```

## Examples

- Accessing /path/to/file.txt but object is at /Path/To/File.txt
- Object deleted with trailing space in key

## Related Errors

- [S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General S3 errors
- [Bucket Not Found]({{< relref "/cloud/aws/aws-s3-bucket-not-found" >}}) -- Bucket not found
