import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PasswordChecker",
    version="0.0.1",
    author="Amogh Jhamb",
    author_email="amogh100109@gmail.com",
    description="A password validity checker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ammo78/PasswordChecker",
    project_urls={
        "Bug Tracker": "https://github.com/Ammo78/PasswordChecker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "PasswordChecker"},
    packages=setuptools.find_packages(where="PasswordChecker"),
    python_requires=">=3.6",
)
