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
from ghc_client.model.moving_expenses import MovingExpenses
from ghc_client.model.pro_gear_weight_tickets import ProGearWeightTickets
from ghc_client.model.weight_tickets import WeightTickets
globals()['MovingExpenses'] = MovingExpenses
globals()['ProGearWeightTickets'] = ProGearWeightTickets
globals()['WeightTickets'] = WeightTickets
from ghc_client.model.ppm_documents import PPMDocuments


class TestPPMDocuments(unittest.TestCase):
    """PPMDocuments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPPMDocuments(self):
        """Test PPMDocuments"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PPMDocuments()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
