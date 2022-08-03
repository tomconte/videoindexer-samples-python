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

class ClapperboardInsight(object):
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
        'fields': 'list[ClapperboardDetails]',
        'id': 'int',
        'instances': 'list[InsightInstance]',
        'is_head_slate': 'bool',
        'thumbnail_id': 'str'
    }

    attribute_map = {
        'fields': 'fields',
        'id': 'id',
        'instances': 'instances',
        'is_head_slate': 'isHeadSlate',
        'thumbnail_id': 'thumbnailId'
    }

    def __init__(self, fields=None, id=None, instances=None, is_head_slate=None, thumbnail_id=None):  # noqa: E501
        """ClapperboardInsight - a model defined in Swagger"""  # noqa: E501
        self._fields = None
        self._id = None
        self._instances = None
        self._is_head_slate = None
        self._thumbnail_id = None
        self.discriminator = None
        if fields is not None:
            self.fields = fields
        if id is not None:
            self.id = id
        if instances is not None:
            self.instances = instances
        if is_head_slate is not None:
            self.is_head_slate = is_head_slate
        if thumbnail_id is not None:
            self.thumbnail_id = thumbnail_id

    @property
    def fields(self):
        """Gets the fields of this ClapperboardInsight.  # noqa: E501


        :return: The fields of this ClapperboardInsight.  # noqa: E501
        :rtype: list[ClapperboardDetails]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ClapperboardInsight.


        :param fields: The fields of this ClapperboardInsight.  # noqa: E501
        :type: list[ClapperboardDetails]
        """

        self._fields = fields

    @property
    def id(self):
        """Gets the id of this ClapperboardInsight.  # noqa: E501


        :return: The id of this ClapperboardInsight.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClapperboardInsight.


        :param id: The id of this ClapperboardInsight.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def instances(self):
        """Gets the instances of this ClapperboardInsight.  # noqa: E501


        :return: The instances of this ClapperboardInsight.  # noqa: E501
        :rtype: list[InsightInstance]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ClapperboardInsight.


        :param instances: The instances of this ClapperboardInsight.  # noqa: E501
        :type: list[InsightInstance]
        """

        self._instances = instances

    @property
    def is_head_slate(self):
        """Gets the is_head_slate of this ClapperboardInsight.  # noqa: E501


        :return: The is_head_slate of this ClapperboardInsight.  # noqa: E501
        :rtype: bool
        """
        return self._is_head_slate

    @is_head_slate.setter
    def is_head_slate(self, is_head_slate):
        """Sets the is_head_slate of this ClapperboardInsight.


        :param is_head_slate: The is_head_slate of this ClapperboardInsight.  # noqa: E501
        :type: bool
        """

        self._is_head_slate = is_head_slate

    @property
    def thumbnail_id(self):
        """Gets the thumbnail_id of this ClapperboardInsight.  # noqa: E501


        :return: The thumbnail_id of this ClapperboardInsight.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_id

    @thumbnail_id.setter
    def thumbnail_id(self, thumbnail_id):
        """Sets the thumbnail_id of this ClapperboardInsight.


        :param thumbnail_id: The thumbnail_id of this ClapperboardInsight.  # noqa: E501
        :type: str
        """

        self._thumbnail_id = thumbnail_id

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
        if issubclass(ClapperboardInsight, dict):
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
        if not isinstance(other, ClapperboardInsight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
