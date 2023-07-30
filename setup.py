from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT="-e ."
def get_requirements(filepath:str)-> List[str]:
    reqs = []
    with open(filepath) as f:
        requirements = f.readlines()
        reqs = [ req.replace("\n","") for req in requirements]

    if(HYPHEN_E_DOT in reqs):
        reqs.remove(HYPHEN_E_DOT)

    return reqs

setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)