from setuptools import setup

setup(
    name='logChecker',
    version='4.0.1',  
    description='A simple log analysis tool',
    long_description='A parsing tool to easily perform pre and post check comparisons after a maintenance window.',
    long_description_content_type='text/x-rst',
    url='https://github.com/laimaretto/logChecker',
    author='Lucas Aimaretto',
    author_email='laimaretto@gmail.com',
    license='BSD 3-clause',
    packages=['src/logChecker'],
    install_requires=['textfsm==1.1.3',
                      'pandas>=1.5.2,<=2.0.3',
                      'XlsxWriter>=3.0.3,<=3.2.0',
                      'ttp>=0.9.0,<=0.9.5',
                      ],
    python_requires='>=3.8',
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['logChecker=src.logChecker.logChecker:main'],
    },
    project_urls={
        'Templates':'https://github.com/laimaretto/logTemplates',
    },
)