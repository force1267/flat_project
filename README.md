# Flat Project
Flatten project codebase into one file. recursively add every file's content from a directory to a file. this script can be used to generate input for Large Language Models (LLM) like ChatGPT, GPT4 and LLaMA.

## Usage
```bash
python flat_project.py [-h] [--exclude [EXCLUDE ...]] [--include [INCLUDE ...]] project_dir
```
### Positional Arguments
  - `project_dir`: Project directory

### Options
  - `-h`, `--help`: Shows help message and exit
  - `--exclude [EXCLUDE ...]`: Files/Directories to exclude
  - `--include [INCLUDE ...]`: Files to include

### Output
The script outputs to stdout. you need to append the result to a file

```bash
python flat_project.py ./my_project/ > my_project.txt
```

