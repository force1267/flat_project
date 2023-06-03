import argparse
import os
import fnmatch

def parse_args():
    parser = argparse.ArgumentParser(description='Flatten project codebase')
    parser.add_argument('project_dir', help='Project directory')
    parser.add_argument('--exclude', nargs='*', default=[], help='Files/Directories to exclude')
    parser.add_argument('--include', nargs='*', default=[], help='Files to include')
    return parser.parse_args()

def get_files(project_dir, excludes):
    abs_project_dir = os.path.abspath(project_dir)
    abs_excludes = [os.path.abspath(exclude) for exclude in excludes]
    matches = []
    for root, dirnames, filenames in os.walk(abs_project_dir):
        for filename in filenames:
            filepath = os.path.join(abs_project_dir, root, filename)
            if not any(
                fnmatch.fnmatch(filepath, exclude) or filepath.startswith(exclude)
                for exclude in abs_excludes
            ):
                matches.append(filepath)
    matches = [os.path.relpath(filepath, abs_project_dir) for filepath in matches]
    return matches

def include_files(files, includes):
    for file in includes:
        if os.path.isfile(file):
            files.append(file)
    return files

def print_files(files):
    for file in files:
        print("###")
        print(f"# {file}")
        print("###")
        with open(file, 'r') as f:
            print(f.read())
        print("\n\n")

def main():
    args = parse_args()
    files = get_files(args.project_dir, args.exclude)
    files = include_files(files, args.include)
    print_files(files)

if __name__ == "__main__":
    main()
