from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_modules(file_path:str)->List[str]:

    requirements = []
    with open(file_path) as req_obj:
        requirements = req_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name = "Cancer-Predictor",
    version = "0.0.1",
    author = "kanishka Maurya",
    author_email = "kanishkamauryaofficial@gmail.com",
    packages = find_packages(),
    py_modules = get_modules("requirements.txt")

)