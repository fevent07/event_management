from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in event_management/__init__.py
from event_management import __version__ as version

setup(
	name="event_management",
	version=version,
	description="Managing events and equipment rentals",
	author="EMC",
	author_email="info@eternal-media.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
