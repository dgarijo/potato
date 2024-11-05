from setuptools import find_packages, setup  # type: ignore
import os

def read(fname):
    print("installing potato")
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open('requirements.txt', 'r') as f:
    install_requires = list()
    dependency_links = list()
    for line in f:
        re = line.strip()
        if re:
            if re.startswith('git+') or re.startswith('svn+') or re.startswith('hg+'):
                dependency_links.append(re)
            else:
                install_requires.append(re)

packages = find_packages()

version = {}
with open("src/__init__.py") as fp:
    exec(fp.read(), version)

setup(
    name='potato',
    version=version["__version__"],
    packages=packages,
    url='https://github.com/dgarijo/potato/',
    license='Apache-2',
    author='Daniel Garijo',
    description='Small script for retrieving Person info from an ORCID using Wikidata',
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    python_requires=">=3.9",
    entry_points={
        'console_scripts': [
            'potato = src.__main__:main',
        ],
    }
)
