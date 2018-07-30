from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='aalog',
    version='0.1',
    # py_modules=['aalog'],
    # packages=['aalog'],
    #this will attempt to autofind packages, but not convinced this works :(
    packages=find_packages(), 
    # packages=['aalog', 'click', 'peewee', colorama],
    # include_package_data=True,
    description='Adventurous Activities Log',
    long_description=readme,
    author='Matt Smith',
    author_email='hellboy1975@gmail.com',
    url='https://github.com/hellboy1975/aalog',
    license=license,
    entry_points='''
        [console_scripts]
        aalog=aalog.cli:cli
    ''',
)
