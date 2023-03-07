import setuptools

setuptools.setup(
    name = 'MyPackage',
    version = '0.0.1',
    author = 'Me',
    author_email='amalroythopputhala@gmail.com',
    description='Calculations package',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.11',
)