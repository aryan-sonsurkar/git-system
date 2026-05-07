from pathlib import Path
import os
import hashlib

def gitinit():
    Path(".mygit").mkdir(exist_ok=True)
    Path(".mygit/objects").mkdir(parents=True)
    Path(".mygit/refs").mkdir(exist_ok=True)
    Path(".mygit/HEAD").write_text("ref: refs/main")
    Path(".mygit/index").write_text("")
    print("Initialized empty repository")

def gitadd(filename):
    content = Path(filename).read_text()
    content = content.encode()
    size = len(content)
    header = f"blob {size}\0".encode()
    blob_data = header + content
    object_id = hashlib.sha1(blob_data).hexdigest()
    print(object_id)
    object_path = ".mygit/objects/" + object_id
    Path(object_path).write_bytes(blob_data)
    
cmd = input("$")
parts=cmd.split()

if len(parts) > 1 and parts[1]=="init" and parts[0]=="mygit":

    if os.path.exists(".mygit"):
        print("Repository already initialized")
    else:
        gitinit()

if len(parts) > 2 and parts[0]=="mygit" and parts[1]=="add":
    gitadd(parts[2])