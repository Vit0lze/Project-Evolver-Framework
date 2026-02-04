import os
import argparse

def ensure_drafts_dir(base_path="drafts"):
    """Creates the drafts directory if it doesn't exist."""
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"Created directory: {base_path}")
    else:
        print(f"Directory already exists: {base_path}")

def count_tokens_approx(text):
    """Approximates token count (1 token ~= 4 chars)."""
    return len(text) // 4

def split_file(file_path, chunk_size_tokens=30000):
    """Splits a file into chunks of approximately chunk_size_tokens."""
    if not os.path.isfile(file_path):
        print(f"Error: File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    total_tokens = count_tokens_approx(content)
    print(f"File: {file_path}")
    print(f"Total approximate tokens: {total_tokens}")

    chunk_size_chars = chunk_size_tokens * 4
    
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    ensure_drafts_dir()

    num_chunks = (len(content) // chunk_size_chars) + 1
    
    for i in range(num_chunks):
        start = i * chunk_size_chars
        end = start + chunk_size_chars
        chunk_content = content[start:end]
        
        chunk_filename = os.path.join("drafts", f"{name}_part{i+1:03d}{ext}")
        with open(chunk_filename, 'w', encoding='utf-8') as chunk_file:
            chunk_file.write(chunk_content)
        
        print(f"Created chunk: {chunk_filename} ({count_tokens_approx(chunk_content)} tokens)")

def main():
    parser = argparse.ArgumentParser(description="Split large files into safe context windows.")
    parser.add_argument("files", nargs='+', help="Files to split")
    parser.add_argument("--size", type=int, default=30000, help="Chunk size in tokens (default: 30000)")
    args = parser.parse_args()

    for file_path in args.files:
        split_file(file_path, args.size)

if __name__ == "__main__":
    main()
