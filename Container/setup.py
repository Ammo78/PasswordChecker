import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Password_Validity_Checker",
    version="0.0.1",
    author="Amogh Jhamb",
    author_email="amogh100109@gmail.com",
    description="A password validity checker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ammo78/Password_Validity_Checker",
    project_urls={
        "Bug Tracker": "https://github.com/Ammo78/Password_Validity_Checker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "Password_Validity_Checker"},
    packages=setuptools.find_packages(where="Password_Validity_Checker"),
    python_requires=">=3.6",
)
