"""Setup file for data-structures package."""


from setuptools import setup


setup(
    name="data-structures",
    description="Python data structures.",
    author=["Brendan Davis"],
    author_email=["brendanmd@gmail.com"],
    license="MIT",
    py_modules=["bst"],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
    }
)
