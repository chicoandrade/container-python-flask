from setuptools import setup

setup(
    name='hello',
    packages=['src'],
    include_package_data=True,
    version='0.0.1',
    install_requires=[
        'flask',
        'python-decouple'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
