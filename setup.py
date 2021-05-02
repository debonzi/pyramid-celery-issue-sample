from setuptools import setup, find_packages

requires = [
    "celery==5.0.5",
    "pyramid==2.0",
    "pyramid-celery==4.0.0",
]


setup(
    name="demo",
    version="0.0.1",
    install_requires=requires,
    packages=find_packages(exclude=['tests']),
    entry_points={
        "paste.app_factory": [
            "main = demo:main",
        ],
    },
)
