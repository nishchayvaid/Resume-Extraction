from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path: str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=[file.replace("\n","") for file in file_obj.readlines()]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='Career Recommendation System',
    version=1.0,
    author="Nishchay",
    author_email="Nishchay89@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)