"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import internal_client
from internal_client.model.upload_payload import UploadPayload
globals()['UploadPayload'] = UploadPayload
from internal_client.model.document_payload import DocumentPayload


class TestDocumentPayload(unittest.TestCase):
    """DocumentPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDocumentPayload(self):
        """Test DocumentPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DocumentPayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()