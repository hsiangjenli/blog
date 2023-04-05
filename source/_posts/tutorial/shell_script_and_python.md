---
title: "[Tutorial] Combining Shell Script and Python for Efficient Automation"
date: 2023-04-05
tags: Python
toc: true
cover: 
thumbnail: 
---
## **🚀 Example-1**

```python
# demo-1.py
print("This is demo 1.")
```
### How write and run shell script
1. Write a shell script similar to the example below and save it as `run.sh`
    ```shell
    # run.sh
    python demo-1.py
    ```
1. Open Git Bash in the Terminal
1. `bash run.sh`

## **🚀 Example-2**
```python
# demo-2.py
string = input("type something.....")

print(f"""

    String = {string}

""")
```
```shell
# run.sh
echo "hello world - 1" | python demo-2.py
echo "hello cat - 2" | python demo-2.py
```
![](https://i.imgur.com/VeXN5GO.png)


> **💡Error** `run.sh: line 1: python: command not found`
> 1. Configure the path to your Python executable
>    - To find the path of your Python exe, you can use the command `where python`
> ```shell
> # run.sh
> PYTHON=/mnt/c/Miniconda3/python.exe
> "$PYTHON" demo-1.py
> ```
