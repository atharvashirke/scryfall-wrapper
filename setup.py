from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name = "scryfall_wrapper",
    version = "0.1.0",
    author = "Atharva Shirke",
    author_email = "atharvashirke@berkeley.edu",
    description = "A wrapper for intuitive use of the Scryfall API",
    long_description=README,
    long_description_content_type="text/markdown",
    url = "https://github.com/atharvashirke/scryfall-wrapper",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    package_dir ={"": "scryfall_wrapper"},
    packages=find_packages(where="scryfall_wrapper"),
    license = "MIT",
    keywords = ["Scryfall", "Wrapper", "Magic the Gathering", "TCG"],
    python_requires=">=3.6"
)