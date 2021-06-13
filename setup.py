from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='BetterPrinting',
    version='0.0.1',
    description='A all in one print function',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/Butter-mit-Brot/BetterPrinting',
    author='Max "Butter" W.',
    author_email='maxwbusinesspypi@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['betterprint', 'print', 'betterprinting', 'printing'],
    packages=find_packages(),
    install_requires=[]
)