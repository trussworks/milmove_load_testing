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
from ghc_client.model.report_violation import ReportViolation
globals()['ReportViolation'] = ReportViolation
from ghc_client.model.report_violations import ReportViolations


class TestReportViolations(unittest.TestCase):
    """ReportViolations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReportViolations(self):
        """Test ReportViolations"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ReportViolations()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
