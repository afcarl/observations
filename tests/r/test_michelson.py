from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.michelson import michelson


def test_michelson():
  """Test module michelson.py by downloading
   michelson.csv and testing shape of
   extracted data has 100 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = michelson(test_path)
  try:
    assert x_train.shape == (100, 1)
  except:
    shutil.rmtree(test_path)
    raise()
