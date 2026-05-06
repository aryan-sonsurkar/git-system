from pathlib import Path

def gitinit():
    Path(".mygit").mkdir()
    Path(".mygit/objects").mkdir(parents=True)
    Path(".mygit/refs").mkdir()
    Path(".mygit/HEAD").write_text("ref: refs/main")
    Path(".mygit/index").write_text("")

cmd = input("$")

if cmd=="mygit init":
    gitinit()
