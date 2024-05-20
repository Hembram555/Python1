import os

def findfiles(directory):
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

# Example usage
for filepath in findfiles('.'):
    print(filepath)
