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
from ghc_client.model.document import Document
from ghc_client.model.upload import Upload
globals()['Document'] = Document
globals()['Upload'] = Upload
from ghc_client.model.pro_gear_weight_ticket_document import ProGearWeightTicketDocument


class TestProGearWeightTicketDocument(unittest.TestCase):
    """ProGearWeightTicketDocument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProGearWeightTicketDocument(self):
        """Test ProGearWeightTicketDocument"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProGearWeightTicketDocument()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
