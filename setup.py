from setuptools import setup, find_packages

setup(
    name='pyfolio',
    version='0.0.1',
    description='A library to study quantitative finance using python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Santiago J. Vasconcello Acuña',
    author_email='santiago.vasconcello@usm.cl',
    url='https://github.com/sjvasconcello/pyfolio',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
