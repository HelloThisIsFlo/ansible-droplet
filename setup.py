from setuptools import setup
from os.path import expanduser

HOME = expanduser("~")

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='ansible-droplet',
    version='0.4.7',
    description='A cli to Create / Destroy DigitalOcean Droplets',
    long_description=readme(),
    keywords='digitalocean digital ocean droplet ansible ssh provision',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities'
    ],
    url='https://github.com/FlorianKempenich/ansible-droplet',
    author='Florian Kempenich & Antonio Pires',
    author_email='Flori@nKempenich.com',
    packages=['ansible_droplet'],
    license='MIT',
    scripts=['bin/ansible-droplet'],
    install_requires=[
        'ansible>=2.6',
        'dopy==0.3.5',
        'click',
        'passlib'
    ],
    data_files=[(HOME, ['.ansible-droplet-inventory'])],
    include_package_data=True,
    zip_safe=False
)
