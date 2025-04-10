from setuptools import setup, find_packages

setup(
    name="occrq-juejin-python-sdk",
    version="0.1.0",
    description="Python SDK for Juejin API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="occrq",
    author_email="1310874029@qq.com ",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
