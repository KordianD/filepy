from setuptools import setup

setup(
    name='filepy',
    packages=['filepy'],
    version='0.11',
    description='File converter',
    author='KordianD',
    author_email='not_valid@gmail.com',
    url='https://github.com/KordianD/filepy',
    keywords=['file', 'convert', 'extensions', 'csv', 'arff'],
    setup_requires=["numpy"],
    install_requires=['numpy'],
    long_description=open('README.md').read(),
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License'],
    long_description_content_type='text/markdown'
)
