from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="regegigax",
    version="0.1.0",
    license="MIT",
    description="パッケージの説明",
    author="ShunDeveloper",
    url="https://github.com/ShunDeveloper/regegigax",
    packages=find_packages("src"),
    package_dir={"": "regegigax"},
    py_modules=[splitext(basename(path))[0]
                for path in glob('regegigax/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
