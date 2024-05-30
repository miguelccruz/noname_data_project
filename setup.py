from typing import List
from setuptools import find_packages, setup

SETUP_FILE_CALL = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    Gets packages from requirements.txt in List form
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", " ") for req in requirements]

        if SETUP_FILE_CALL in requirements:
            requirements.remove(SETUP_FILE_CALL)

setup(
    name='noname_data_project',
    version='0.0.1',
    author='Miguel',
    author_email='cruzmiguelbon@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)