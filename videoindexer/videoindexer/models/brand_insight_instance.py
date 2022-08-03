# coding: utf-8

"""
    Operations

    The Operations API contains all the Azure Video Indexer APIs, like Upload video, Get insights and more, as well as authorization operations to get access tokens for calling the other operations. For Azure Resource Manager (ARM)-based accounts, some REST APIs like generating an access token, list of all accounts, and updating existing accounts <a href=\"https://aka.ms/avam-arm-api\" target=\"_blank\">can be found here</a>.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BrandInsightInstance(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'adjusted_end': 'str',
        'adjusted_start': 'str',
        'brand_type': 'InstanceSource',
        'end': 'str',
        'instance_source': 'InstanceSource',
        'start': 'str'
    }

    attribute_map = {
        'adjusted_end': 'adjustedEnd',
        'adjusted_start': 'adjustedStart',
        'brand_type': 'brandType',
        'end': 'end',
        'instance_source': 'instanceSource',
        'start': 'start'
    }

    def __init__(self, adjusted_end=None, adjusted_start=None, brand_type=None, end=None, instance_source=None, start=None):  # noqa: E501
        """BrandInsightInstance - a model defined in Swagger"""  # noqa: E501
        self._adjusted_end = None
        self._adjusted_start = None
        self._brand_type = None
        self._end = None
        self._instance_source = None
        self._start = None
        self.discriminator = None
        if adjusted_end is not None:
            self.adjusted_end = adjusted_end
        if adjusted_start is not None:
            self.adjusted_start = adjusted_start
        if brand_type is not None:
            self.brand_type = brand_type
        if end is not None:
            self.end = end
        if instance_source is not None:
            self.instance_source = instance_source
        if start is not None:
            self.start = start

    @property
    def adjusted_end(self):
        """Gets the adjusted_end of this BrandInsightInstance.  # noqa: E501


        :return: The adjusted_end of this BrandInsightInstance.  # noqa: E501
        :rtype: str
        """
        return self._adjusted_end

    @adjusted_end.setter
    def adjusted_end(self, adjusted_end):
        """Sets the adjusted_end of this BrandInsightInstance.


        :param adjusted_end: The adjusted_end of this BrandInsightInstance.  # noqa: E501
        :type: str
        """

        self._adjusted_end = adjusted_end

    @property
    def adjusted_start(self):
        """Gets the adjusted_start of this BrandInsightInstance.  # noqa: E501


        :return: The adjusted_start of this BrandInsightInstance.  # noqa: E501
        :rtype: str
        """
        return self._adjusted_start

    @adjusted_start.setter
    def adjusted_start(self, adjusted_start):
        """Sets the adjusted_start of this BrandInsightInstance.


        :param adjusted_start: The adjusted_start of this BrandInsightInstance.  # noqa: E501
        :type: str
        """

        self._adjusted_start = adjusted_start

    @property
    def brand_type(self):
        """Gets the brand_type of this BrandInsightInstance.  # noqa: E501


        :return: The brand_type of this BrandInsightInstance.  # noqa: E501
        :rtype: InstanceSource
        """
        return self._brand_type

    @brand_type.setter
    def brand_type(self, brand_type):
        """Sets the brand_type of this BrandInsightInstance.


        :param brand_type: The brand_type of this BrandInsightInstance.  # noqa: E501
        :type: InstanceSource
        """

        self._brand_type = brand_type

    @property
    def end(self):
        """Gets the end of this BrandInsightInstance.  # noqa: E501


        :return: The end of this BrandInsightInstance.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this BrandInsightInstance.


        :param end: The end of this BrandInsightInstance.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def instance_source(self):
        """Gets the instance_source of this BrandInsightInstance.  # noqa: E501


        :return: The instance_source of this BrandInsightInstance.  # noqa: E501
        :rtype: InstanceSource
        """
        return self._instance_source

    @instance_source.setter
    def instance_source(self, instance_source):
        """Sets the instance_source of this BrandInsightInstance.


        :param instance_source: The instance_source of this BrandInsightInstance.  # noqa: E501
        :type: InstanceSource
        """

        self._instance_source = instance_source

    @property
    def start(self):
        """Gets the start of this BrandInsightInstance.  # noqa: E501


        :return: The start of this BrandInsightInstance.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this BrandInsightInstance.


        :param start: The start of this BrandInsightInstance.  # noqa: E501
        :type: str
        """

        self._start = start

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BrandInsightInstance, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BrandInsightInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
