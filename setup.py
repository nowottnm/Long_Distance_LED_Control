import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Long_Distance_LED_Control",
    version="1.0",
    author="Maximilian Nowottnick",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nowottnm/Long_Distance_LED_Control",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
        "numpy"
    ],
    entry_points = {
        'console_scripts': ['led_control=RaspiController.app.app:main'],
    }
)
