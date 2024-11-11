
#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Ensure that the required environment variables are set
if [ -z "$PYPI_USERNAME" ] || [ -z "$PYPI_PASSWORD" ]; then
  echo "PYPI_USERNAME and PYPI_PASSWORD environment variables must be set"
  exit 1
fi

# Upgrade pip and install build and twine
python -m pip install --upgrade pip
pip install build twine

# Build the package
python -m build

# Upload the package to PyPI
twine upload dist/* -u "$PYPI_USERNAME" -p "$PYPI_PASSWORD"