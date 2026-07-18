---
title: "[Solution] Conda Pip Mix Error - Fix Mixing pip and conda Breaking Environments"
description: "Fix errors caused by mixing pip and conda in the same environment. Learn why pip-conda mixing breaks dependency resolution and how to fix it."
tools: ["conda"]
error-types: ["pip-mix-error"]
severities: ["warning"]
weight: 5
---

This error means mixing `pip install` and `conda install` in the same environment has corrupted the dependency graph. conda and pip track packages separately, so each tool becomes unaware of what the other installed.

## What This Error Means

When you install packages with both conda and pip, conda only tracks packages it installed. Packages installed via pip appear in conda's environment but conda cannot manage or remove them. This leads to errors like:

```
RemoveError: 'setuptools' is a dependency of conda and cannot be removed
# or
CondaError: The target prefix is the base prefix. Aborting.
# or pip errors when a conda-installed package conflicts
ERROR: pip's dependency resolver does not take into account all the packages that are installed.
```

The two package managers overwrite each other's metadata, causing unpredictable failures.

## Why It Happens

- You run `pip install` inside a conda environment without first installing packages via conda
- A `requirements.txt` is used inside a conda environment instead of conda environment files
- A tutorial instructs mixing both without warning about consequences
- conda packages are installed on top of pip packages, overwriting shared files
- Different versions of the same package exist in conda and pip metadata
- Build tools like `pip install -e .` run inside conda environments

## How to Fix It

### Rebuild the environment from scratch

The most reliable fix is starting over:

```bash
conda deactivate
conda remove --name myenv --all
conda create -n myenv python=3.11
conda activate myenv
conda install <packages-from-conda>
pip install <packages-from-pip>
```

Install conda packages first, then pip packages last.

### Use conda-forge for pip-only packages

Many packages on pip are also on conda-forge:

```bash
conda config --add channels conda-forge
conda install <package>
```

### Track pip packages separately

If you must use pip, record what was installed:

```bash
pip install <package>
pip freeze > pip-requirements.txt
```

Then restore them cleanly later.

### Use environment.yml instead of requirements.txt

```yaml
name: myenv
dependencies:
  - python=3.11
  - numpy
  - pandas
  - pip:
    - some-pip-only-package
```

This lets conda manage the full environment while acknowledging pip packages.

### Remove conda-installed packages via pip carefully

```bash
pip uninstall <package>
conda install <package>=correct_version
```

Never run `pip install` to overwrite a conda package.

## Common Mistakes

- Running `pip install -r requirements.txt` without first installing conda packages
- Installing conda packages after pip has already set up the environment
- Not isolating pip-only packages into the `pip:` section of environment.yml
- Assuming `conda install --force` will fix pip contamination
- Using `pip install --upgrade` on packages that conda manages

## Related Pages

- [Conda Solver Error]({{< relref "/tools/conda/conda-solver-error" >}}) -- solver failures from mixed packages
- [Conda Package Not Found]({{< relref "/tools/conda/conda-package-not-found" >}}) -- package availability issues
- [Conda Conflict Error]({{< relref "/tools/conda/conda-conflict-error" >}}) -- dependency conflicts
