# Python Virtual Environments (venv)

```bash
# Create a virtual environment
python -m venv myenv

# Activate virtual environment (Windows)
myenv\Scripts\activate

# Activate virtual environment (Linux/Mac)
source myenv/bin/activate

# Deactivate virtual environment
deactivate

# Check installed packages
pip list

# Install a package inside virtual environment
pip install requests

# Freeze installed packages to a requirements file
pip freeze > requirements.txt

# Install packages from requirements file
pip install -r requirements.txt
