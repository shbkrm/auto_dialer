from setuptools import setup, find_packages

setup(
    name="auto_dialer",
    version="0.0.1",
    description="Auto Dialer for ERPNext using Tata Smartflo",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "auto_dialer = auto_dialer.hooks"
        ]
    }
)
