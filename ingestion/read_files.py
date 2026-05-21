import os

Excluded_folders = ["node_modules", "_pycache_", "venv", ".git"]
Allowed_extensions = [".py", ".js", ".jsx", ".ts", ".tsx", ".md", ".txt"]

def read_files(repo_path):
    all_chunks = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in Excluded_folders]
        for file in files:
            if any(file.endswith(ext) for ext in Allowed_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        all_chunks.append({          # ← was: all_chunks.append(content)
                            "content": content,
                            "metadata": {"source": file_path}
                        })
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return all_chunks