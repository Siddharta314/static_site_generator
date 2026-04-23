import sys

from generate_page import generate_pages_recursive
from utils import copy_recursive_directory, safe_delete_directory


def main():
    base_path = "./"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    src_path = "./static"
    dest_path = "./docs"
    safe_delete_directory(dest_path)
    copy_recursive_directory(src_path, dest_path)
    generate_pages_recursive("content/", "template.html", dest_path, base_path)



if __name__ == "__main__":
    main()
