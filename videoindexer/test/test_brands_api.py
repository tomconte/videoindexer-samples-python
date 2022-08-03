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
from videoindexer.api.brands_api import BrandsApi  # noqa: E501
from videoindexer.rest import ApiException


class TestBrandsApi(unittest.TestCase):
    """BrandsApi unit test stubs"""

    def setUp(self):
        self.api = BrandsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_brand(self):
        """Test case for create_brand

        Create Brand  # noqa: E501
        """
        pass

    def test_delete_brand(self):
        """Test case for delete_brand

        Delete Brand  # noqa: E501
        """
        pass

    def test_get_brand(self):
        """Test case for get_brand

        Get Brand  # noqa: E501
        """
        pass

    def test_get_brands(self):
        """Test case for get_brands

        Get Brands  # noqa: E501
        """
        pass

    def test_get_brands_model_settings(self):
        """Test case for get_brands_model_settings

        Get Brands Model Settings  # noqa: E501
        """
        pass

    def test_update_brand(self):
        """Test case for update_brand

        Update Brand  # noqa: E501
        """
        pass

    def test_update_brands_model_settings(self):
        """Test case for update_brands_model_settings

        Update Brands Model Settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
