from setuptools import find_packages, setup

setup(
    name='ogr2osm',
    version='0.1.0',

    author='Paul Norman, Andrew Guertin, Ivan Ortega',
    description='A tool for converting ogr-readable files like shapefiles '
                'into .osm data',
    entry_points={
        'console_scripts': [
            'ogr2osm = ogr2osm.main:main'
        ]
    },
    extras_require=dict(
        test=[
            'cram>=0.7',
            'lxml>=3.4.4'
        ],
        speed=['lxml>=3.4.4']
    ),
    install_requires=['gdal>=1.10.0'],
    license='Beerware/MIT',
    long_description=open('Readme.md').read(),
    packages=find_packages(),
    url='https://github.com/pnorman/ogr2osm'
)
