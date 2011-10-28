#####################################
# Copyright 2011 MERS Technologies. #
#####################################

Python API library for Subuno API.

OVERVIEW
--------
The Subuno API allows developers to integrate Subuno's fraud screening service and gain access to multiple fraud prevention solutions. Transactions can then be passed to Subuno and screened based on the rules setup in the SaaS. 

Subuno provides a fraud screening software-as-a-service (SaaS) platform that allows merchants to leverage multiple fraud detection solutions in a rules based and multi-layered approach. Without requiring technical knowledge, Subuno helps users easily automate their fraud screening flow and speed up the manual review process by bringing relevant fraud screening tools together on the same review screen.'

URL: http://www.subuno.com/developers.html 
Email: support@subuno.com


PREREQUISITES
-------------
The Subuno Python API requires json module (Python 2.6 or 2.7 will be fine).
  (http://docs.python.org/library/json.html)
  
  
INSTALLATION
------------
We recommend you use the `pip` installer:
    pip install subuno

If this doesn't work for you, you can also download the latest version at:
    http://www.subuno.com/developers.html

Then uncompress it and run setup.py:
    tar xvfz subuno-1.x.tar.gz
    cd subuno-1.x/
    python setup.py install


USAGE
-----
Once the library is installed to your python path, you can import the subuno
manager object easily and invoke the run() method:
    from subuno import subuno
    subuno.run(...)


EXAMPLES
--------

See contents of the ./examples/ directory.

Feel free to edit the example and put in your own Subuno API license key.
To execute examples:
    cd ./examples/
    python example1.py

