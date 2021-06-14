from setuptools import setup, find_packages

def create_long_description(sep:str = '\n\n', *args):
    long_description_parts = []
    for file in args:
        with open(file, 'r') as _h:
            long_description_parts.append(_h.read())

    return sep.join(long_description_parts)

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='BetterPrinting',
    version='0.1.1',
    description='A all in one print function',
    long_description=create_long_description('\n\n', 'README.txt', 'CHANGELOG.txt'),
    url='https://github.com/Butter-mit-Brot/BetterPrinting',
    author='Max "Butter" W.',
    author_email='maxwbusinesspypi@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['betterprint', 'print', 'betterprinting', 'printing'],
    packages=find_packages(),
    install_requires=['termcolor']
)