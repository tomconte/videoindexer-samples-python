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

class EmotionInsight(object):
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
        'id': 'int',
        'instances': 'list[EmotionInsightInstance]',
        'type': 'EmotionType'
    }

    attribute_map = {
        'id': 'id',
        'instances': 'instances',
        'type': 'type'
    }

    def __init__(self, id=None, instances=None, type=None):  # noqa: E501
        """EmotionInsight - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._instances = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if instances is not None:
            self.instances = instances
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this EmotionInsight.  # noqa: E501


        :return: The id of this EmotionInsight.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmotionInsight.


        :param id: The id of this EmotionInsight.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def instances(self):
        """Gets the instances of this EmotionInsight.  # noqa: E501


        :return: The instances of this EmotionInsight.  # noqa: E501
        :rtype: list[EmotionInsightInstance]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this EmotionInsight.


        :param instances: The instances of this EmotionInsight.  # noqa: E501
        :type: list[EmotionInsightInstance]
        """

        self._instances = instances

    @property
    def type(self):
        """Gets the type of this EmotionInsight.  # noqa: E501


        :return: The type of this EmotionInsight.  # noqa: E501
        :rtype: EmotionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmotionInsight.


        :param type: The type of this EmotionInsight.  # noqa: E501
        :type: EmotionType
        """

        self._type = type

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
        if issubclass(EmotionInsight, dict):
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
        if not isinstance(other, EmotionInsight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
