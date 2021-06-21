from setuptools import setup

setup(
    name="ur3_robotlab",
    version="0.11.2",
    description="Python library to control an UR robot",
    author="Olivier Roulet-Dubonnet",
    author_email="olivier.roulet@gmail.com",
    url='https://github.com/oroulet/python-urx',
    packages=["ur3_robotlab"],
    provides=["ur3_robotlab"],
    install_requires=["numpy", "math3d"],
    license="GNU Lesser General Public License v3",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
