from setuptools import setup

setup(
    name='tenantsecrets',
    version='0.0.1',
    packages=('tenantsecrets',),
    url='https://github.com/Rigdon/pytenantsecrets',
    license='MIT',
    author='Ryan Rigdon',
    author_email='mr.rigdon@gmail.com',
    install_requires=(),
    tests_require=(),
    description=(
        'Tenant-Aware Secret Management and Access for Hashicorp Vault'),
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'))
