from setuptools import setup, find_packages

setup(
    name="python-rule-engine",
    version="0.1.0",
    license="MIT",
    author="Santiago Alvarez",
    author_email="santiagoalvarez264@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/santalvarez/python-rule-engine",
    keywords="rule engine json",
    install_requires=[
          "pydantic",
      ],

)