import os

def create_project_dir(directory):

    if not os.path.exists(directory):
        print(f'Creating Project: {directory}')
        os.makedirs(directory)


def create_data_files(project_name, base_url):
 
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')

    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):

    try:
        with open(path, 'w') as file:
            file.write(data)
    except IOError as e:
        print(f"Error writing to file {path}: {e}")


def add_data_to_file(path, data):

    try:
        with open(path, 'a') as file:
            file.write(data + '\n')
    except IOError as e:
        print(f"Error appending to file {path}: {e}")


def delete_file_content(path):

    try:
        with open(path, 'w'):
            pass
    except IOError as e:
        print(f"Error clearing file {path}: {e}")


def file_to_set(file_name):

    results = set()
    try:
        with open(file_name, 'rt') as file:
            for line in file:
                results.add(line.strip())
    except IOError as e:
        print(f"Error reading file {file_name}: {e}")
    return results


def set_to_file(file_name, data_set):

    delete_file_content(file_name)
    for item in sorted(data_set):
        add_data_to_file(file_name, item)
