from setuptools import setup

setup(name='C_The_Payne',
      version='1.1',
      description='Tools for interpolating spectral models with neural networks.',
      author='Yuan-Sen Ting',
      author_email='ting@ias.edu',
      license='MIT',
      url='https://github.com/highzclouds/C_The_Payne',
      package_dir = {},
      packages=['C_The_Payne'],
      package_data={'C_The_Payne':['other_data/*.npz','neural_nets/*.npz']},
      dependency_links = [],
      install_requires=['torch', 'torchvision'])
