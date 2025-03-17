from setuptools import setup, find_packages

setup(
    name="poultry_innovate",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.32.0",
        "pandas>=2.2.0",
        "numpy>=1.26.0",
        "plotly>=5.18.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "scikit-learn>=1.4.0",
        "pillow>=10.2.0",
        "streamlit-option-menu>=0.3.12",
        "streamlit-extras>=0.4.0",
        "streamlit-lottie>=0.0.5"
    ],
) 