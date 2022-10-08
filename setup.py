from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    "Environment :: Console",
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='BetterPrinting',
    version='0.7.0',
    description='An set of printing tools',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/Butter-mit-Brot/BetterPrinting',
    author='Max "Butter" W.',
    author_email='wrussmax@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['betterprint', 'print', 'betterprinting', 'printing', 'better', 'stringmanipulation', 'instaprint', 'sysinfo', 'systeminfo', 'terminal', 'ui', 'terminal ui', 'color', 'terminal color', 'rainbow', 'terminal draw'],
    packages=find_packages(),
    install_requires=[]
)