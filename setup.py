import setuptools

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarize"
Author_Name = "Turvash Singh"
SRC_REPO = "Text-Summarization"
AUTHOR_EMAIL = "turvashsingh@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_Name,
    author_email=AUTHOR_EMAIL,
    description="A small package for Text Summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_Name}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_Name}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)