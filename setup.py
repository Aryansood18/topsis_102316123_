from setuptools import setup, find_packages

setup(
    name="Topsis-Vansh-102316118",
    version="1.0.0",
    author="Vansh",
    description="TOPSIS implementation in Python",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
)
