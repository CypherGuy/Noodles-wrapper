import setuptools
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name = 'noodleswrapper', #Name user sees
    version = '0.1.2',
    author = 'Kabir Ghai',
    author_email = 'KabirGhai18@gmail.com',
    description = 'A wrapper used for meme generating using Discord API',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
     install_requires=[
  'Discord.py>=1.7',
    ], 
    python_requires='>=3.8',
    packages = ['noodles_wrapper'],#pip install ...
    include_package_data = True,
    url = 'https://www.frenchnoodles.xyz/',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
        ],
    py_modules=['noodleswrapper'],
)