import os
import sys
from setuptools import setup

# For Python shipped with OpenOffice, python is a wrapper
# for python.bin that fixes the import and library path.  We should
# call python instead of python.bin. """
import os
import sys
if os.path.basename(sys.executable) == "python.bin":
    sys.executable = os.path.join(
        os.path.dirname(sys.executable), "python")

setup(name="mpresent",
      version="0.1",
      description="Office mobile presentation constroller",
      url="https://github.com/imacat/mpresent",
      author="imacat",
      author_email="imacat@mail.imacat.idv.tw",
      license="Apache License, Version 2.0",
      zip_safe=False,
      scripts=["bin/mpresent"])
