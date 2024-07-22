from setuptools import setup, find_packages

setup(
    name='majestic-cli',
    version='0.1.0',
    packages=find_packages(),
    py_modules=['majestic_cli'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        majestic-cli=majestic_cli:cli
    ''',
)
