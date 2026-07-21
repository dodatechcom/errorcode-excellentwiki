---
title: "[Solution] R Bioconductor Error"
description: "Bioconductor package errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Bioconductor Error

Bioconductor package errors.

### Common Causes
Wrong install method; BiocManager missing

### How to Fix
```r
if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install("GenomicFeatures")
```

### Examples
```r
BiocManager::install(c("DESeq2", "edgeR"))
```
