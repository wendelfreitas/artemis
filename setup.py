from setuptools import setup, find_packages

def read(filename):
        return [req for req in open(filename)]

setup(
    name="artemis",
    version="0.1.0",
    description="artemis - IA and music app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_requires={
        "dev": read("requirements-dev.txt")
    }
)