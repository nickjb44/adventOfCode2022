import math

class Directory:

    def __init__(self, name, parent=None):
        self.parent = parent
        self.files = []
        self.subdirectories = []
        self.name = name
        self.size = 0
        self.type = "directory"

    def calculate_size(self):
        for file in self.files:
            self.size += int(file.size)
        for directory in self.subdirectories:
            self.size += int(directory.calculate_size())
        return self.size

    def add_file(self, new_file):
        name_collision = False
        for file in self.files:
            if new_file.name == file.name:
                name_collision = True
                print(f"{new_file.name} already exists in directory, ignoring")
        if not name_collision:
            self.files.append(new_file)
        return

    def add_directory(self, new_directory):
        name_collision = False
        for directory in self.subdirectories:
            if new_directory.name == directory.name:
                name_collision = True
                print(f"{new_directory.name} already exists in directory, ignoring")
        if not name_collision:
            self.subdirectories.append(new_directory)
        return

    def get_list_of_subdirectories(self, list_of_directories):
        for directory in self.subdirectories:
            list_of_directories = directory.get_list_of_subdirectories(list_of_directories)
            list_of_directories.append(directory)
        return list_of_directories


class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size


def update_current_directory(current_directory, input):
    ls_line = input.readline()
    while "$" not in ls_line and ls_line:
        components = ls_line.split()
        if components[0] == "dir":
            directory = Directory(name=components[1], parent=current_directory)
            current_directory.add_directory(directory)
        else:
            file = File(name=components[1], size=components[0])
            current_directory.add_file(file)
        ls_line = input.readline()
    return ls_line


def navigate_file_directory(current_directory, location):
    if location == "..":
        if not current_directory.parent:
            raise Exception(f"Directory {current_directory.name} has no parent, may be root or not configured correctly")
        else:
            new_current_directory = current_directory.parent
    else:
        is_in_subdirectories = False
        for directory in current_directory.subdirectories:
            if directory.name == location:
                is_in_subdirectories = True
                new_current_directory = directory
        if not is_in_subdirectories:
            new_current_directory = Directory(name=location, parent=current_directory)
            current_directory.add_directory(new_current_directory)

    return new_current_directory


input_file = "data/input_1.txt"
root_directory = Directory("/")
with open(input_file) as input:
    current_directory = root_directory
    line = input.readline()
    while line:
            command_components = line.split()
            if command_components[1] == "ls":
                line = update_current_directory(current_directory, input)
            elif command_components[1] == "cd":
                new_location = command_components[2]
                current_directory = navigate_file_directory(current_directory, new_location)
                line = input.readline()

root_directory.calculate_size()

list_of_directories = []
list_of_directories = root_directory.get_list_of_subdirectories(
    list_of_directories
)
total_space_used = root_directory.size

free_space_needed = 30000000
total_capacity = 70000000
min_space_to_delete = total_space_used - (total_capacity - free_space_needed)
print(f"we're using {total_space_used} and need to delete {min_space_to_delete}")
most_deletable_directory_size = math.inf

for i, directory in enumerate(list_of_directories):
    if min_space_to_delete <= directory.size < most_deletable_directory_size:
        most_deletable_directory_size = directory.size

print(f"the most deletable directory's total size is {most_deletable_directory_size}")
