import setuptools

with open('readme.md' , 'r') as fh:
    long_description = fh.read()

setuptools.setup(name='PyTlin',
      description = 'Kotlin functions also, let, and run, as well as sh-like (and Mathematica-like) piping syntax',
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      url = 'https://github.com/frejonb/PyTlin',
      author = 'F. G. Rejon Barrera',
      author_email = 'f.g.rejonbarrera@gmail.com',
      license = 'MIT',
      version='1.0',
      py_modules=['PyTlin'],
      classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ),
    )
