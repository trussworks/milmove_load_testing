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
from internal_client.model.backup_contact_permission import BackupContactPermission
globals()['BackupContactPermission'] = BackupContactPermission
from internal_client.model.service_member_backup_contact_payload import ServiceMemberBackupContactPayload


class TestServiceMemberBackupContactPayload(unittest.TestCase):
    """ServiceMemberBackupContactPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceMemberBackupContactPayload(self):
        """Test ServiceMemberBackupContactPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceMemberBackupContactPayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()