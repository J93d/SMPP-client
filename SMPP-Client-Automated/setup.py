import os
import urllib.request
import subprocess
import sys
from setuptools import setup, find_packages

# Helper function to check for internet connectivity
def is_internet_available():
    try:
        # Trying to connect to PyPI (or any reliable site)
        urllib.request.urlopen("https://pypi.org", timeout=5)
        return True
    except urllib.error.URLError:
        return False

# Check if pip is installed
def is_pip_installed():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'], stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

# Helper function to use easy_install if pip is not available
def install_with_easy_install(package_path):
    from setuptools.command.easy_install import main as easy_install
    easy_install([package_path])

# Check internet connectivity and pip availability
internet_available = is_internet_available()
pip_installed = is_pip_installed()

# Specify the local dependencies folder
local_deps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.dependencies'))

# Define install_requires with your dependencies
install_requires = [
    'et_xmlfile',
    'openpyxl',
]

# If internet is not available or pip is not installed, use local dependencies
if not pip_installed:
    print("Pip not installed, using easy_install for dependencies.")
    if not internet_available:
        print("No internet available, using local dependencies.")

        # Manually install dependencies using easy_install from the local folder
        local_packages = os.listdir(local_deps_path)
        for package in local_packages:
            package_path = os.path.join(local_deps_path, package)
            install_with_easy_install(package_path)

    else:
        print("Internet available but pip not installed, using easy_install.")
        # easy_install will automatically fetch from PyPI if internet is available

# If pip is installed and internet is available, proceed normally
if pip_installed and internet_available:
    print("Pip installed, using PyPI for dependencies.")

# Fallback to using setup() to install the package itself
setup(
    name='your_project_name',
    version='1.0',
    packages=find_packages(),
    
    install_requires=install_requires,

    # Other metadata and configurations
    author='Your Name',
    author_email='your_email@example.com',
    description='Your project description',
)
