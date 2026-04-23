from generate_page import generate_pages_recursive
from utils import copy_recursive_directory, safe_delete_directory


def main():
    src_path = "./static"
    dest_path = "./public"
    safe_delete_directory(dest_path)
    copy_recursive_directory(src_path, dest_path)
    generate_pages_recursive("content/", "template.html", "public/")


if __name__ == "__main__":
    main()
