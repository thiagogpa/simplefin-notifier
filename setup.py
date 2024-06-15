from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simplefin-notifier",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple project to fetch data from SimpleFIN and send notifications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/simplefin-notifier",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
        "python-dotenv",
        "gotify-python",
    ],
)
