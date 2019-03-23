from setuptools import find_packages, setup


def main():
    """Setup"""
    setup(
        name='{{cookiecutter.namespace}}',
        version='1.0.0',
        author='{{cookiecutter.author}}',
        author_email='{{cookiecutter.author_email}}',
        packages=find_packages(exclude=("tests",)),
        install_requires=[
            'click',
        ],
        extras_require={
            'test': ['pytest', 'flake8', 'pytest-cov', 'pytest-flake8', 'flake8-import-order',
                     'flake8-docstrings'],
        },
        entry_points='''
            [console_scripts]
            {{cookiecutter.namespace}}={{cookiecutter.namespace}}.main:cli
        ''',
    )


if __name__ == '__main__':
    main()
