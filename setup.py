from os.path import dirname, join
from setuptools import setup, find_packages


with open(join(dirname(__file__), 'ants/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='Scale-Crawl',
    version=version,
    url='https://github.com/wcong/scale-crawl',
    description='A Scale Crawler from ants',
    long_description=open('README.rst').read(),
    author='Scrapy developers',
    maintainer='Wcong',
    maintainer_email='wc19920415@gmail.com',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['ants = ants.cmdline:execute']
    },
    classifiers=[
        'Framework :: Scrapy',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'Twisted>=10.0.0',
        'w3lib>=1.8.0',
        'queuelib',
        'lxml',
        'pyOpenSSL',
        'cssselect>=0.9',
        'six>=1.5.2',
    ],
)
