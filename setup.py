from distutils.core import setup

setup(name='subuno',
      version='1.0',
      py_modules=['subuno.apilib'],
      description='Subuno Python API Library',
      author='MERS Technologies, LLC',
      author_email='support@subuno.com',
      url='http://www.subuno.com/developers.html',
      download_url="http://www.subuno.com/download/python/subuno-1.0.tar.gz",
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Development Status :: 4 - Beta",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],

      long_description="""\
Subuno API Library
------------------

The Subuno API allows developers to integrate Subuno's fraud screening service
and gain access to multiple fraud prevention solutions. Transactions can then
be passed to Subuno and screened based on the rules setup in the SaaS. 

Subuno provides a fraud screening software-as-a-service (SaaS) platform that
allows merchants to leverage multiple fraud detection solutions in a rules
based and multi-layered approach. Without requiring technical knowledge, Subuno
helps users easily automate their fraud screening flow and speed up the manual
review process by bringing relevant fraud screening tools together on the same
review screen.
"""
)
