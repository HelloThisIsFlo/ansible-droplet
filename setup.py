from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='ansible-droplet',
    version='0.1.2',
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
    author_email='shockn745@gmail.com',
    packages=['ansible_droplet'],
    license='MIT',
    scripts=['bin/ansible-droplet'],
    install_requires=[
        'ansible',
        'dopy==0.3.5',
        'click'
    ],
    include_package_data=True,
    zip_safe=False
)
# TODO: Investigate the `zip_safe` option
