## This setup.py will be responsible in creating my machine learning project/application as a package. U can also install this package
# in ur projects u can also use it. With the help of setup.py i will be able to build my entire machine learning application as a package and even deploy in pypi(python pypi --> pip).
## from there any body can do the installation and anybody can use it.
## setup.py --> building our application as a package itself.
from setuptools import find_packages,setup ## This will automatically find all the packages that are available in the present current directory where we are creating our machine learning application.
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]: ## This function will return list of libraries
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() ## Whenever we try to use readlines that /n is also recorded over there
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        

## Whenever i m trying to install this requirements.txt at that point of time this setup.py should also run to build the packages, so for enabling that we need to write "-e ." in requirements.txt --> This will automatically trigger setup.py file.        

## When u do : pip install -r "requirements.txt" --> Here all the installation will happen and at the end we know there is "-e ." in requirements.txt , this is mapped to the setup.py file --> automatically this entire package will be built. A folder will be created with packages detail.

setup(
name='mlproject',
version='0.0.1', ## Whenever my next version will come i will just keep on updating this and automatically that entire packages will be built and it will be going to the pypi where u can also use it.
author='Shubham',
author_email='amritanshubhardwaj12crosary@gmail.com',
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn']  --> Just a way of installing the packages
install_requires=get_requirements('requirements.txt') ## This function the main work is that whatever path i m giving over here it should takes this up and whatever libraries will be there will get installed.
)
## How setup.py will be able to find out how many packages are there or not ??
## Create a new folder in the current directory, name it is : src --> source , now if u want this src to be found out as a pacakge
## what we need to do is that inside this src folder we will try to create a file which is called as : __init__.py 
## Now w.r.t what will happen -> whenever this setup.py the find_packages is running right , it will go and see in how many folders u have this __init__.py , so it will directly consider this src as a package itself.
## Then it will try to build it , once it builds it will probably import this wherever u want, like how we import seaborn, pandas but for that we need to put this in the pypi package itself.
## My entire project development will be happening inside this src folder.
## Whenever we create a new folder/internal folder there also we will create the __init__.py file so that it also behaves like a package.
## There will be scenarios where u will require around 100 packages to be installed , so there u can't write the way the above packages are written.