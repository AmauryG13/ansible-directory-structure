import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ansible-structure-assembler",
    version="0.0.1",
    author="Amaury Guillermin",
    author_email="amauryguillermin@gmail.com",
    description="Package to generate the convinent Ansible directory structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
