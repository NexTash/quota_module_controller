from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in quota_module_controller/__init__.py
from quota_module_controller import __version__ as version

setup(
	name="quota_module_controller",
	version=version,
	description="App to manage erpnext sites usage to enable sass functions",
	author="NexTash",
	author_email="support@nextash.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
