import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="studentweb-average-grade-navjordj", # Replace with your own username
    version="0.0.1",
    author="Jørgen Navjord",
    author_email="navjordj@gmail.com",
    description="Package to calculate a weighted average grade from a Studentweb HTML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/navjordj/Studentweb-Average-Grade",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
