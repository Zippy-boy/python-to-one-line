from setuptools import setup

setup(
    name='python_to_one_line',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/Zippy-boy/python-to-one-line',
    author='Zippy-boy',
    author_email='zippy-boy@outlook.com',
    license='BSD 2-clause',
    scripts=['scripts/python-to-one-line'],
    packages=['python_to_one_line'],
    install_requires=['mpi4py>=2.0',
                      'argparse',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)


print("DONE")