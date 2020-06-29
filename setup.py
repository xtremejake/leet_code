import setuptools

setuptools.setup(
    name="leetcode",
    version="0.1",
    description="Solutions for leetcode problems",
    url="https://github.com/xtremejake/leet_code",
    author="xtremejake",
    author_email="xtremejake.usa@gmail.com",
    license="Apache-2.0",
    include_package_metadata=True,
    include_package_data=True,
    package_dir={"leetcode": "leetcode"},
    install_requires=[
        "black==19.10b0",
    ],  # specifies dependencies of python packages in pip
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
