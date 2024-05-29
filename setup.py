from setuptools import setup, find_packages

setup(
    name="rvvup-sdk",
    version="0.1.0",
    description="SDK for interacting with the Rvvup API",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
