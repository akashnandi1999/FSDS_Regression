from setuptools import find_packages, setup
from typing import List


Hypen_E_Dot = '-e .'


def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() 
        requirements = [req.replace("\n", "") for req in requirements]

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)

    return requirements




setup(
    name = 'RegressorProject',
    version= 'o.1',
    author= 'Akash',
    author_email= 'akashnandi446@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages= find_packages()
)