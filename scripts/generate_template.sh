#!/usr/bin/env bash

set -e

OUTPUT_FILE="auto_generated_template.sh"

echo "Generating ${OUTPUT_FILE} from current project structure..."

# -------------------------------
# Header
# -------------------------------
cat << 'EOF' > ${OUTPUT_FILE}
#!/usr/bin/env bash

set -e  # exit immediately if a command fails

echo "Creating project structure"

# creating the directories
EOF

# -------------------------------
# Directories
# -------------------------------
find . \
  -type d \
  ! -path "*/.git*" \
  ! -path "*/.venv*" \
  ! -path "*/venv*" \
  ! -path "*/env*" \
  ! -path "*/.env/*" \
  ! -path "*/__pycache__*" \
  ! -path "*/data/assets*" \
  ! -path "*/data/pdfs*" \
  ! -path "*/data/texts*" \
  ! -path "*/scripts*" \
  ! -path "*/.streamlit*" \
| sed 's|^\./||' \
| sort \
| awk '{print "mkdir -p " $0}' >> ${OUTPUT_FILE}

cat << 'EOF' >> ${OUTPUT_FILE}

echo "Creating files"

# python + config files
EOF

# -------------------------------
# Files: .py, __init__.py, .toml, .ini
# -------------------------------
find . \
  -type f \
  \( -name "__init__.py" -o -name "*.py" -o -name "*.toml" -o -name "*.ini" \) \
  ! -path "*/.git*" \
  ! -path "*/.venv*" \
  ! -path "*/venv*" \
  ! -path "*/env*" \
  ! -path "*/.env/*" \
  ! -path "*/__pycache__*" \
  ! -path "*/scripts*" \
| sed 's|^\./||' \
| sort \
| awk '{print "touch " $0}' >> ${OUTPUT_FILE}

cat << 'EOF' >> ${OUTPUT_FILE}

echo "Project scaffold created successfully!"
EOF

chmod +x ${OUTPUT_FILE}

echo "Done. ${OUTPUT_FILE} regenerated."
