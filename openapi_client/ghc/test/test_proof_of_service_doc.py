"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ghc_client
from ghc_client.model.upload import Upload
globals()['Upload'] = Upload
from ghc_client.model.proof_of_service_doc import ProofOfServiceDoc


class TestProofOfServiceDoc(unittest.TestCase):
    """ProofOfServiceDoc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProofOfServiceDoc(self):
        """Test ProofOfServiceDoc"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProofOfServiceDoc()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
