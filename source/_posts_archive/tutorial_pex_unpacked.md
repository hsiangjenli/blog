---
title: "[tutorial] PEX Unpacked: Building and Executing Python Executables with Ease"
date: 2024-08-15
created_at: 2024-08-15
tags: python
toc: true
---

## What is "PEX"?

The full name of PEX is Python Executable. This is an open-source tool for building a virtual environment to execute your Python code. However, be cautious when using PEX because it does not include a Python interpreter; thus, your computer must have a Python environment installed.

<!-- more -->

<!-- The full name of PEX is Python Executable. This is an open-source tool for building a virtual environment to execute your Python code. However, be cautious when using PEX because it does not include a Python interpreter. Therefore, your computer must have a Python environment installed. -->

<!-- PEX, which stands for Python Executable, is an open-source tool that packages Python projects into executable files. It simplifies the process of creating a virtual environment and running Python code within that isolated environment. -->

### The process of executing `.pex`

When you run a `.pex` file, the system reads the shebang line at the top of the file, `#!/usr/bin/env python`, to invoke the Python interpreter to execute the script.

<!-- When you run `.pex` file, the system will reading the top of your file `#!/usr/bin/env python` to 調用 python interpretable to run python. -->

<!-- When you run a .pex file, the system reads the shebang line at the top of the file, #!/usr/bin/env python, to invoke the Python interpreter to execute the script. -->

## Practice

### Install PEX
```python
pip install pex
```

### Enter Interpretable pex environemt

Easy way

```python
# Enter an interpretable Pex environment without specifying a Python version
pex 

# Enter an interpretable Pex environment specifying a specific Python version
pex --python=python3.12 # specific python version

---
Pex 2.16.1 ephemeral hermetic environment with no dependencies.
Exit the repl (type quit()) and run `pex -h` for Pex CLI help.
Python 3.11.4 (main, Jul  5 2023, 08:40:20) [Clang 14.0.6 ] on darwin
Type "help", "pex", "copyright", "credits" or "license" for more information.
>>> 
```

Advanced

```python
# Specifying requirements
pex pandas

---
Pex 2.16.1 ephemeral hermetic environment with 1 requirement and 6 activated distributions.
Python 3.11.4 (main, Jul  5 2023, 08:40:20) [Clang 14.0.6 ] on darwin
Type "help", "pex", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
```

### Package `.py` into pex file

```python
# demo.py

import pandas as pd

def main():
    print(f"Hello, World! The pandas version is {pd.__version__}")

if __name__ == "__main__":
    main()
```

```python
pex -D . -e demo:main -o demo.pex -r requirements.txt
```

```python
# Execute PEX script
./demo.pex

>>> Hello, World! The pandas version is 2.2.2
```
- `-D`: Source directory
- `-e`: Entry point for the PEX application
- `-o`: Output file name for the PEX file
- `-r`: Specifies requirements file that lists the dependencies


## Reference
- [探索PEX：高效且可移植的Python环境解决方案](https://blog.csdn.net/gitblog_00001/article/details/138744439)
- [Specifying entry points](https://docs.pex-tool.org/buildingpex.html#specifying-entry-points)