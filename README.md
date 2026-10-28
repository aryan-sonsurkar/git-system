# git-system

**A mini Git implementation in pure Python - built to understand how Git actually works.**

## Why

Git feels like magic until you build one. This project reimplements Git's
core object model from first principles, using only the Python standard
library (hashlib, zlib, pathlib) - no Git binaries, no libraries.

## What's implemented

| Command | What it does |
|---|---|
| `mygit init` | Creates the `.mygit` repository structure (objects, refs, HEAD, index) |
| `mygit add <file>` | Creates a blob object: header + content, SHA-1 addressed, zlib-compressed - exactly like real Git |
| `mygit cat-file <hash>` | Decompresses and prints an object's content by its SHA-1 hash |

## What it teaches

- **Content-addressable storage** - every object is identified by the SHA-1 of its own bytes
- **The blob model** - how Git stores file snapshots, not diffs
- **Compression and addressing** - why the same file always produces the same hash
- **Repository layout** - `objects/`, `refs/`, `HEAD`, and the index

## Usage

```bash
python git.py
# then, at the prompt:
$ mygit init
$ mygit add a.txt
$ mygit cat-file <hash>
```

## Roadmap

The natural next steps, in Git's own order: trees and commits on top of
blobs, then a staging index, then branches as mutable refs.

## License

MIT - see [LICENSE](LICENSE).
