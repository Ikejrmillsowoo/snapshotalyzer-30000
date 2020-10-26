from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="Isaac Mills",
    author_email="poppymills2@gmail.com",
    description="snapshotalyzer 30000 is a tool to manage AWS EC@ snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/Ikejrmillsowoo/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
