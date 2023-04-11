from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 'Simple CLI to determine validity of pypi pakage name.'
  
setup(
        name ='validate_pypi_name',
        version ='1.0.3',
        author ='Pablo Hansen',
        author_email ='pablosfsanchz@gmail.com',
        url ='https://github.com/pablojosecodes/pypi_name_validator',
        description ='Simple CLI to determine validity of pypi pakage name.',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'valid = validate_pypi_name.validator:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='',
        install_requires = requirements,
        zip_safe = False
)
