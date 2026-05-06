from pathlib import Path
import os

def gitinit():
    Path(".mygit").mkdir(exist_ok=True)
    Path(".mygit/objects").mkdir(parents=True)
    Path(".mygit/refs").mkdir(exist_ok=True)
    Path(".mygit/HEAD").write_text("ref: refs/main")
    Path(".mygit/index").write_text("")
    print("Initialized empty repository")

cmd = input("$")
parts=cmd.split()

if len(parts) > 1 and parts[1]=="init" and parts[0]=="mygit":

    if os.path.exists(".mygit"):
        print("Repository already initialized")
    else:
        gitinit()
