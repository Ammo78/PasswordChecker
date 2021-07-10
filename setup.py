import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PasswordValidityChecker",
    version="0.0.1",
    author="Amogh Jhamb",
    author_email="amogh100109@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ammo78/PasswordValidityChecker",
    project_urls={
        "Bug Tracker": "https://github.com/Ammo78/PasswordValidityChecker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "PasswordValidityChecker"},
    packages=setuptools.find_packages(where="PasswordValidityChecker"),
    python_requires=">=3.6",
)
