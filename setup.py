
with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

setuptools.setup(
    name="tprint",
    description=" tprint allows you to print letters in a cool way.",
    url="https://github.com/execution/tprint",
    packages=["tprint"],
    license="",
    install_requires=requirements,
    version=0.1,
    long_description="",
)
