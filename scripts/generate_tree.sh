python - <<'EOF'
import os

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
    return any(name.endswith(suffix) for suffix in EXCLUDE_SUFFIXES)

def walk(path, prefix=""):
    entries = [
        e for e in os.listdir(path)
        if not should_exclude(e)
    ]
    for i, entry in enumerate(sorted(entries)):
        full = os.path.join(path, entry)
        is_last = i == len(entries) - 1
        print(prefix + ("└── " if is_last else "├── ") + entry)
        if os.path.isdir(full):
            walk(full, prefix + ("    " if is_last else "│   "))

print("RAG_project_2")
walk(".")
EOF
