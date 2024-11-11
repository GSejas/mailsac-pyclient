from setuptools import setup, find_packages

setup(
    name='mailsac-client',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A client library to interact with the Mailsac REST API',
    packages=find_packages(),
    install_requires=[
        'requests',  # Assuming requests is needed for API calls
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)