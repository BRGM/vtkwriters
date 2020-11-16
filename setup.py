from setuptools import setup
from pathlib import Path


class PackageInfo:
    def __init__(self, directory):
        import re

        directory = Path(directory)
        assert directory.exists()
        self.directory = directory
        init_file = directory / "__init__.py"
        assert init_file.is_file()
        for name, value in re.findall(
            r"""__([a-z]+)__ = "([^"]+)""", init_file.read_text(encoding="utf8")
        ):
            setattr(self, name, value)

    @property
    def name(self):
        return self.directory.name


package = PackageInfo("vtkwriters")

setup(
    name=package.name,
    version=package.version,
    author="Simon Lopez",
    author_email="s.lopez@brgm.fr",
    description="Pure python routines to write KitWare VTK files.",
    long_description="",
    license="GPL v.3",
    packages=[package.name],
    install_requires=["numpy>=1.17",],
)
