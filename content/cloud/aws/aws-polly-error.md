---
title: "[Solution] AWS Polly Error — speech/lexicon/synthesis failures"
description: "Fix AWS Polly errors. Resolve speech synthesis, lexicon, and voice issues."
error-types: ["api-error"]
severities: ["error"]
weight: 167
---

An AWS Polly error occurs when speech synthesis fails, custom lexicons are invalid, or voice output encounters errors. Polly converts text to speech but requires correct input format and voice selection.

## Common Causes

- Input text exceeds 3000 bytes per request (SSML)
- Voice not supported for the selected engine
- Custom lexicon pronunciation file invalid
- Audio format not supported for the use case
- SSML tags malformed

## How to Fix

### Synthesize Speech

```bash
aws polly synthesize-speech \
  --text "Hello, this is a test." \
  --output-format mp3 \
  --voice-id Joanna \
  --engine standard \
  speech.mp3
```

### List Voices

```bash
aws polly describe-voices \
  --engine standard \
  --query 'Voices[*].{Name:Name,Language:LanguageCode,Gender:Gender}'
```

### Put Lexicon

```bash
aws polly put-lexicon \
  --name my-lexicon \
  --content '<lexicon version="1.0" xmlns="http://www.w3.org/2001/01/phonetic-alphabet-metadata"><lexeme><grapheme>hello</grapheme><phoneme>hɛˈloʊ</phoneme></lexeme></lexicon>'
```

### Get Lexicon

```bash
aws polly get-lexicon --name my-lexicon
```

### List Lexicons

```bash
aws polly list-lexicons
```

## Examples

```bash
# Example 1: Voice not found
# InvalidParameterValueException: Voice not found
# Fix: use list-voices to check available voices

# Example 2: SSML error
# SSML parsing failed: Invalid SSML tag
# Fix: validate SSML syntax before synthesis
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 output errors
