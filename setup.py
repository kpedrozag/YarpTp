import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Yarptp",
    version="0.1.0",
    author="Universidad Tecnológica de Bolívar",
    author_email="dirsis@utb.edu.co",
    description="YarpTp module for Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IngenieriaDeSistemasUTB/YarpTp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 3 - Alpha",
    ],
)
