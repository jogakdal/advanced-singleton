from setuptools import setup, find_packages

setup(
    name='advanced-python-singleton',
    version='1.2',
    description='Singleton & TtlSingleton meta-class',
    author='jogakdal',
    author_email='jogakdal@gmail.com',
    url='https://https://github.com/jogakdal/advanced-singleton',
    install_requires=['expiringdict'],
    packages=find_packages(exclude=[]),
    keywords=['jogakdal', 'Singleton', 'TTL', 'metaclass'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
