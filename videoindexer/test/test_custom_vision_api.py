# coding: utf-8

"""
    Operations

    The Operations API contains all the Azure Video Indexer APIs, like Upload video, Get insights and more, as well as authorization operations to get access tokens for calling the other operations. For Azure Resource Manager (ARM)-based accounts, some REST APIs like generating an access token, list of all accounts, and updating existing accounts <a href=\"https://aka.ms/avam-arm-api\" target=\"_blank\">can be found here</a>.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import videoindexer
from videoindexer.api.custom_vision_api import CustomVisionApi  # noqa: E501
from videoindexer.rest import ApiException


class TestCustomVisionApi(unittest.TestCase):
    """CustomVisionApi unit test stubs"""

    def setUp(self):
        self.api = CustomVisionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_connect_custom_vision_account(self):
        """Test case for connect_custom_vision_account

        Connect Custom Vision Account  # noqa: E501
        """
        pass

    def test_disconnect_custom_vision_account(self):
        """Test case for disconnect_custom_vision_account

        Disconnect Custom Vision Account  # noqa: E501
        """
        pass

    def test_get_custom_vision_account(self):
        """Test case for get_custom_vision_account

        Get Custom Vision Account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()