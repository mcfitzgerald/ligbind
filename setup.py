import setuptools

setuptools.setup(
    name="ligbind",
    version="0.1.0",
    url="https://github.com/mcfitzgerald/ligbind",

    author="Michael Fitzgerald",
    author_email="michael.craig.fitzgerald@gmail.com",

    description="Tools to simulate and fit ligand binding isotherms",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
