# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import unittest
import numpy as np
from skl2onnx.common.data_types import FloatTensorType
from skl2onnx import convert_sklearn
from test_utils import create_tensor
from test_utils import dump_data_and_model
from sklearn.decomposition import TruncatedSVD


class TestTruncatedSVD(unittest.TestCase):
    
    def setUp(self):
        np.random.seed(0)        

    def test_truncated_svd(self):
        N, C, K = 2, 3, 2
        x = create_tensor(N, C)

        svd = TruncatedSVD(n_components=K)
        svd.fit(x)
        model_onnx = convert_sklearn(svd, initial_types=[('input', FloatTensorType(shape=[1, C]))])
        self.assertTrue(model_onnx is not None)
        dump_data_and_model(x, svd, model_onnx, basename="SklearnTruncatedSVD")


if __name__ == "__main__":
    unittest.main()
