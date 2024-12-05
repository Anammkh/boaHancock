from setuptools import setup, find_packages

setup(
    name='BoaHancock',
    version='1.0.0',
    author='Khoirul Anam',
    author_email='khoirlanaam4567@gmail.com',
    description='This is tools to make starter template python for create moduls or library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Anammkh/BoaHancock',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'boa start=boa.generator:main', 
        ],
    },
    install_requires=[
        'termcolor',
        'pyfiglet',
        'colorama',
    ],
    python_requires='>=3.6',
)

