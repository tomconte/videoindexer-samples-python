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
from videoindexer.models.computer_vision_model_input import ComputerVisionModelInput  # noqa: E501
from videoindexer.rest import ApiException


class TestComputerVisionModelInput(unittest.TestCase):
    """ComputerVisionModelInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testComputerVisionModelInput(self):
        """Test ComputerVisionModelInput"""
        # FIXME: construct object with mandatory attributes with example values
        # model = videoindexer.models.computer_vision_model_input.ComputerVisionModelInput()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()