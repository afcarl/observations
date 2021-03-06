from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.budget_uk import budget_uk


def test_budget_uk():
  """Test module budget_uk.py by downloading
   budget_uk.csv and testing shape of
   extracted data has 1519 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = budget_uk(test_path)
  try:
    assert x_train.shape == (1519, 10)
  except:
    shutil.rmtree(test_path)
    raise()
