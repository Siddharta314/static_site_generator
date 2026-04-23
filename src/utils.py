import os
import shutil


def copy_recursive_directory(src_path: str, dest_path: str):
    if not os.path.exists(src_path):
        raise ValueError(f"Source path {src_path} does not exist")

    if not os.path.exists(dest_path):
        print(f"Creating destination directory: {dest_path}")
        os.mkdir(dest_path)

    for item in os.listdir(src_path):
        item_path = os.path.join(src_path, item)
        dest_item_path = os.path.join(dest_path, item)
        if os.path.isdir(item_path):
            copy_recursive_directory(item_path, dest_item_path)
        else:
            print(f"Copying {item_path} to {dest_item_path}")
            shutil.copy(item_path, dest_item_path)


def safe_delete_directory(path: str):
    if os.path.exists(path):
        print(f"Deleting {path} directory...")
        shutil.rmtree(path)
