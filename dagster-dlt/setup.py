from setuptools import find_packages, setup

setup(
    name="dagster_dlt",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-embedded-elt",
        "dagster-gcp",
        "dlt"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
