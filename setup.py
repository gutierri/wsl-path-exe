from setuptools import setup, find_packages
import io


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="wsl-path-exe",
    version="0.0.1",
    long_description=long_description,
    download_url='https://github.com/gutierri/wsl-path-exe',
    author='Gutierri Barb0za',
    author_email='me@gutierri.me',
    license='',
    packages=find_packages(),
    entry_points = {
        'console_scripts': (
            'wsl-path-exe = wsl_path_exe.__main__:main'
        )
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console'
        'Topic :: Software Development',
        'Operating System :: Microsoft :: Windows :: Windows 10'
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ]
)
