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

class AnimatedCharacterInsight(object):
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
        'confidence': 'float',
        'description': 'str',
        'id': 'int',
        'instances': 'list[AnimatedCharacterInsightInstance]',
        'name': 'str',
        'reference_id': 'str',
        'thumbnail_id': 'str',
        'thumbnails': 'list[AnimatedCharacterInsightThumbnail]'
    }

    attribute_map = {
        'confidence': 'confidence',
        'description': 'description',
        'id': 'id',
        'instances': 'instances',
        'name': 'name',
        'reference_id': 'referenceId',
        'thumbnail_id': 'thumbnailId',
        'thumbnails': 'thumbnails'
    }

    def __init__(self, confidence=None, description=None, id=None, instances=None, name=None, reference_id=None, thumbnail_id=None, thumbnails=None):  # noqa: E501
        """AnimatedCharacterInsight - a model defined in Swagger"""  # noqa: E501
        self._confidence = None
        self._description = None
        self._id = None
        self._instances = None
        self._name = None
        self._reference_id = None
        self._thumbnail_id = None
        self._thumbnails = None
        self.discriminator = None
        if confidence is not None:
            self.confidence = confidence
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if instances is not None:
            self.instances = instances
        if name is not None:
            self.name = name
        if reference_id is not None:
            self.reference_id = reference_id
        if thumbnail_id is not None:
            self.thumbnail_id = thumbnail_id
        if thumbnails is not None:
            self.thumbnails = thumbnails

    @property
    def confidence(self):
        """Gets the confidence of this AnimatedCharacterInsight.  # noqa: E501


        :return: The confidence of this AnimatedCharacterInsight.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this AnimatedCharacterInsight.


        :param confidence: The confidence of this AnimatedCharacterInsight.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

    @property
    def description(self):
        """Gets the description of this AnimatedCharacterInsight.  # noqa: E501


        :return: The description of this AnimatedCharacterInsight.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnimatedCharacterInsight.


        :param description: The description of this AnimatedCharacterInsight.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this AnimatedCharacterInsight.  # noqa: E501


        :return: The id of this AnimatedCharacterInsight.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnimatedCharacterInsight.


        :param id: The id of this AnimatedCharacterInsight.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def instances(self):
        """Gets the instances of this AnimatedCharacterInsight.  # noqa: E501


        :return: The instances of this AnimatedCharacterInsight.  # noqa: E501
        :rtype: list[AnimatedCharacterInsightInstance]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this AnimatedCharacterInsight.


        :param instances: The instances of this AnimatedCharacterInsight.  # noqa: E501
        :type: list[AnimatedCharacterInsightInstance]
        """

        self._instances = instances

    @property
    def name(self):
        """Gets the name of this AnimatedCharacterInsight.  # noqa: E501


        :return: The name of this AnimatedCharacterInsight.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnimatedCharacterInsight.


        :param name: The name of this AnimatedCharacterInsight.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reference_id(self):
        """Gets the reference_id of this AnimatedCharacterInsight.  # noqa: E501


        :return: The reference_id of this AnimatedCharacterInsight.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this AnimatedCharacterInsight.


        :param reference_id: The reference_id of this AnimatedCharacterInsight.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def thumbnail_id(self):
        """Gets the thumbnail_id of this AnimatedCharacterInsight.  # noqa: E501


        :return: The thumbnail_id of this AnimatedCharacterInsight.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_id

    @thumbnail_id.setter
    def thumbnail_id(self, thumbnail_id):
        """Sets the thumbnail_id of this AnimatedCharacterInsight.


        :param thumbnail_id: The thumbnail_id of this AnimatedCharacterInsight.  # noqa: E501
        :type: str
        """

        self._thumbnail_id = thumbnail_id

    @property
    def thumbnails(self):
        """Gets the thumbnails of this AnimatedCharacterInsight.  # noqa: E501


        :return: The thumbnails of this AnimatedCharacterInsight.  # noqa: E501
        :rtype: list[AnimatedCharacterInsightThumbnail]
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """Sets the thumbnails of this AnimatedCharacterInsight.


        :param thumbnails: The thumbnails of this AnimatedCharacterInsight.  # noqa: E501
        :type: list[AnimatedCharacterInsightThumbnail]
        """

        self._thumbnails = thumbnails

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
        if issubclass(AnimatedCharacterInsight, dict):
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
        if not isinstance(other, AnimatedCharacterInsight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
