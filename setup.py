from setuptools import setup, find_packages

setup(
    name="logisticpca",
    version="0.1",
    packages=find_packages(),
    install_requires=["torch", "numpy"],
    author="Reda Abouzaid",
    author_email="azaidr00@gmail.com",
    description="A Python implementation of PCA for binary data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourgithub/logisticpca",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
