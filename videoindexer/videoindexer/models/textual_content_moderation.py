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

class TextualContentModeration(object):
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
        'banned_words_count': 'int',
        'banned_words_ratio': 'float',
        'id': 'int',
        'instances': 'list[InsightInstance]'
    }

    attribute_map = {
        'banned_words_count': 'bannedWordsCount',
        'banned_words_ratio': 'bannedWordsRatio',
        'id': 'id',
        'instances': 'instances'
    }

    def __init__(self, banned_words_count=None, banned_words_ratio=None, id=None, instances=None):  # noqa: E501
        """TextualContentModeration - a model defined in Swagger"""  # noqa: E501
        self._banned_words_count = None
        self._banned_words_ratio = None
        self._id = None
        self._instances = None
        self.discriminator = None
        if banned_words_count is not None:
            self.banned_words_count = banned_words_count
        if banned_words_ratio is not None:
            self.banned_words_ratio = banned_words_ratio
        if id is not None:
            self.id = id
        if instances is not None:
            self.instances = instances

    @property
    def banned_words_count(self):
        """Gets the banned_words_count of this TextualContentModeration.  # noqa: E501


        :return: The banned_words_count of this TextualContentModeration.  # noqa: E501
        :rtype: int
        """
        return self._banned_words_count

    @banned_words_count.setter
    def banned_words_count(self, banned_words_count):
        """Sets the banned_words_count of this TextualContentModeration.


        :param banned_words_count: The banned_words_count of this TextualContentModeration.  # noqa: E501
        :type: int
        """

        self._banned_words_count = banned_words_count

    @property
    def banned_words_ratio(self):
        """Gets the banned_words_ratio of this TextualContentModeration.  # noqa: E501


        :return: The banned_words_ratio of this TextualContentModeration.  # noqa: E501
        :rtype: float
        """
        return self._banned_words_ratio

    @banned_words_ratio.setter
    def banned_words_ratio(self, banned_words_ratio):
        """Sets the banned_words_ratio of this TextualContentModeration.


        :param banned_words_ratio: The banned_words_ratio of this TextualContentModeration.  # noqa: E501
        :type: float
        """

        self._banned_words_ratio = banned_words_ratio

    @property
    def id(self):
        """Gets the id of this TextualContentModeration.  # noqa: E501


        :return: The id of this TextualContentModeration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TextualContentModeration.


        :param id: The id of this TextualContentModeration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def instances(self):
        """Gets the instances of this TextualContentModeration.  # noqa: E501


        :return: The instances of this TextualContentModeration.  # noqa: E501
        :rtype: list[InsightInstance]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this TextualContentModeration.


        :param instances: The instances of this TextualContentModeration.  # noqa: E501
        :type: list[InsightInstance]
        """

        self._instances = instances

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
        if issubclass(TextualContentModeration, dict):
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
        if not isinstance(other, TextualContentModeration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
