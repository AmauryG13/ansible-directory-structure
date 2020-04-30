import os, setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def get_metadata():
    """Get version and version_info from ads/__meta__.py file."""
    module_path = os.path.join(os.path.dirname('__file__'), 'src/ads', '__meta__.py')

    import importlib.util
    spec = importlib.util.spec_from_file_location('__meta__', module_path)
    meta = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(meta)
    return meta.__version__, meta.__author__, meta.__package__

__version__, __author__, __package__ = get_metadata()

setuptools.setup(
    name=__package__,
    version=__version__,
    author=__author__,
    author_email="amauryguillermin@gmail.com",
    description="Package to generate the convinent Ansible directory structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts=['bin/ansible-structure'],
    package_dir={'':'src'},
    packages=setuptools.find_packages('src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3'
)
