import zipfile
import pathlib


def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("C:/Users/Frederick Akam/Desktop/60 Days Python Program/app1/bonus/archive_extractor/compressed.zip",
"C:/Users/Frederick Akam/Desktop/60 Days Python Program/app1/bonus\dest")
