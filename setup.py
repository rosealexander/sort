from setuptools import setup


setup(
  name="sort",
  version="1.0.0",
  license="GPL-3.0",
  author="Alex Bewley",
  description="Simple, online, and realtime tracking of multiple objects in a video sequence.",
  url="https://github.com/abewley/sort",
  install_requires=['numpy', 'matplotlib', 'scikit-image', 'filterpy'],
  py_modules=['sort'],
)
