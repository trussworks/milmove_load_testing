"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import ghc_client
from ghc_client.api.report_violations_api import ReportViolationsApi  # noqa: E501


class TestReportViolationsApi(unittest.TestCase):
    """ReportViolationsApi unit test stubs"""

    def setUp(self):
        self.api = ReportViolationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_associate_report_violations(self):
        """Test case for associate_report_violations

        Associate violations with an evaluation report  # noqa: E501
        """
        pass

    def test_get_report_violations_by_report_id(self):
        """Test case for get_report_violations_by_report_id

        Fetch the report violations for an evaluation report  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
