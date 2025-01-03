import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "1.0.0"  # Set a version aligned with semantic versioning

REPO_NAME = "MLproject-with-MLflow-and-AWSEC2"
AUTHOR_USER_NAME = "Aakash091-dark"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "sehrawataakash091@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A modern Python package for an ML app with MLflow and AWS EC2 integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Documentation": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}#readme",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.10",  # Updated to latest stable version
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",  # Specify Python 3.10 as minimum requirement
    install_requires=[
        "mlflow>=2.6.0",  # Latest MLflow version
        "boto3>=1.28.0",  # AWS SDK for Python
        "scikit-learn>=1.3.0",  # ML library
        "pandas>=2.0.0",  # Data manipulation library
        "numpy>=1.25.0",  # Numerical computations
    ],
    extras_require={
        "dev": ["pytest>=7.0", "black>=23.0", "flake8>=6.0"],  # Development dependencies
    },
    include_package_data=True,  # Include non-code files like README.md
    license="MIT",
    keywords="machine learning MLflow AWS EC2 Python package",
)
