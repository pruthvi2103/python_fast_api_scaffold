"""Python setup.py for python_fast_api_scaffold package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("python_fast_api_scaffold", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="python_fast_api_scaffold",
    version=read("python_fast_api_scaffold", "VERSION"),
    description="Awesome python_fast_api_scaffold created by pruthvi2103",
    url="https://github.com/pruthvi2103/python_fast_api_scaffold/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="pruthvi2103",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["python_fast_api_scaffold = python_fast_api_scaffold.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
