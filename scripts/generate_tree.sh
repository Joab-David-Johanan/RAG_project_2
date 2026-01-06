python - <<'EOF'
import os, sys, io

# Force stdout to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ----- Exclusions (kept from your logic) -----
EXCLUDE_NAMES = {
    "__pycache__",
    ".git",
    ".venv",
    "venv",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
    "node_modules",
}

EXCLUDE_SUFFIXES = (
    ".egg-info",
    ".coverage",
)

def should_exclude(name: str) -> bool:
    if name in EXCLUDE_NAMES:
        return True
    return any(name.endswith(s) for s in EXCLUDE_SUFFIXES)

# ----- Presentation-oriented traversal -----
def walk(path, prefix="", is_root=False):

    all_entries = sorted(
        e for e in os.listdir(path)
        if not should_exclude(e)
    )

    # THIS is the key part
    dirs = [e for e in all_entries if os.path.isdir(os.path.join(path, e))]
    files = [e for e in all_entries if os.path.isfile(os.path.join(path, e))]

    ordered = dirs + files   # folders first always

    for i, entry in enumerate(ordered):
        full = os.path.join(path, entry)
        last = i == len(ordered) - 1

        connector = "└── " if last else "├── "
        print(prefix + connector + entry)

        if os.path.isdir(full):
            walk(full, prefix + ("    " if last else "│   "), is_root=False)

print("RAG_project_2")

# call with root flag only for first level
walk(".", prefix="", is_root=True)
EOF
