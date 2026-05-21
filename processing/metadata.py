import os

def create_metadata(repo_path):
    metadata = {
        "repo_name": os.path.basename(repo_path),
        "file_path": repo_path,
        "extension": os.path.splitext(repo_path)[1]
    }
    return metadata