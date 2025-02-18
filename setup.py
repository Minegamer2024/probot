import setuptools

with open("README.md", "r") as f:
    description = f.read()

setuptools.setup(
    name="probotlib",
    version="1.5",
    author="Minegamer",
    description="A small library that helps verify credit transfers.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/Minegamer2024/probot.git",
    packages=setuptools.find_packages(where="src"),
    package_dir={"":"src"},
    python_requires=">=3.8,<=3.12.9",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    keywords="python, discord.py, discord, probotlib, probot discord, discord probot , bot, transfer"
)