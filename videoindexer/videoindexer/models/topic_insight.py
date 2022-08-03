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

class TopicInsight(object):
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
        'full_name': 'str',
        'iab_name': 'str',
        'id': 'int',
        'instances': 'list[InsightInstance]',
        'iptc_name': 'str',
        'language': 'OneOfTopicInsightLanguage',
        'name': 'str',
        'reference_id': 'str',
        'reference_type': 'TopicReferenceType',
        'reference_url': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'full_name': 'fullName',
        'iab_name': 'iabName',
        'id': 'id',
        'instances': 'instances',
        'iptc_name': 'iptcName',
        'language': 'language',
        'name': 'name',
        'reference_id': 'referenceId',
        'reference_type': 'referenceType',
        'reference_url': 'referenceUrl'
    }

    def __init__(self, confidence=None, full_name=None, iab_name=None, id=None, instances=None, iptc_name=None, language=None, name=None, reference_id=None, reference_type=None, reference_url=None):  # noqa: E501
        """TopicInsight - a model defined in Swagger"""  # noqa: E501
        self._confidence = None
        self._full_name = None
        self._iab_name = None
        self._id = None
        self._instances = None
        self._iptc_name = None
        self._language = None
        self._name = None
        self._reference_id = None
        self._reference_type = None
        self._reference_url = None
        self.discriminator = None
        if confidence is not None:
            self.confidence = confidence
        if full_name is not None:
            self.full_name = full_name
        if iab_name is not None:
            self.iab_name = iab_name
        if id is not None:
            self.id = id
        if instances is not None:
            self.instances = instances
        if iptc_name is not None:
            self.iptc_name = iptc_name
        if language is not None:
            self.language = language
        if name is not None:
            self.name = name
        if reference_id is not None:
            self.reference_id = reference_id
        if reference_type is not None:
            self.reference_type = reference_type
        if reference_url is not None:
            self.reference_url = reference_url

    @property
    def confidence(self):
        """Gets the confidence of this TopicInsight.  # noqa: E501


        :return: The confidence of this TopicInsight.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TopicInsight.


        :param confidence: The confidence of this TopicInsight.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

    @property
    def full_name(self):
        """Gets the full_name of this TopicInsight.  # noqa: E501


        :return: The full_name of this TopicInsight.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this TopicInsight.


        :param full_name: The full_name of this TopicInsight.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def iab_name(self):
        """Gets the iab_name of this TopicInsight.  # noqa: E501


        :return: The iab_name of this TopicInsight.  # noqa: E501
        :rtype: str
        """
        return self._iab_name

    @iab_name.setter
    def iab_name(self, iab_name):
        """Sets the iab_name of this TopicInsight.


        :param iab_name: The iab_name of this TopicInsight.  # noqa: E501
        :type: str
        """

        self._iab_name = iab_name

    @property
    def id(self):
        """Gets the id of this TopicInsight.  # noqa: E501


        :return: The id of this TopicInsight.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TopicInsight.


        :param id: The id of this TopicInsight.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def instances(self):
        """Gets the instances of this TopicInsight.  # noqa: E501


        :return: The instances of this TopicInsight.  # noqa: E501
        :rtype: list[InsightInstance]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this TopicInsight.


        :param instances: The instances of this TopicInsight.  # noqa: E501
        :type: list[InsightInstance]
        """

        self._instances = instances

    @property
    def iptc_name(self):
        """Gets the iptc_name of this TopicInsight.  # noqa: E501


        :return: The iptc_name of this TopicInsight.  # noqa: E501
        :rtype: str
        """
        return self._iptc_name

    @iptc_name.setter
    def iptc_name(self, iptc_name):
        """Sets the iptc_name of this TopicInsight.


        :param iptc_name: The iptc_name of this TopicInsight.  # noqa: E501
        :type: str
        """

        self._iptc_name = iptc_name

    @property
    def language(self):
        """Gets the language of this TopicInsight.  # noqa: E501


        :return: The language of this TopicInsight.  # noqa: E501
        :rtype: OneOfTopicInsightLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TopicInsight.


        :param language: The language of this TopicInsight.  # noqa: E501
        :type: OneOfTopicInsightLanguage
        """

        self._language = language

    @property
    def name(self):
        """Gets the name of this TopicInsight.  # noqa: E501


        :return: The name of this TopicInsight.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TopicInsight.


        :param name: The name of this TopicInsight.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reference_id(self):
        """Gets the reference_id of this TopicInsight.  # noqa: E501


        :return: The reference_id of this TopicInsight.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this TopicInsight.


        :param reference_id: The reference_id of this TopicInsight.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def reference_type(self):
        """Gets the reference_type of this TopicInsight.  # noqa: E501


        :return: The reference_type of this TopicInsight.  # noqa: E501
        :rtype: TopicReferenceType
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this TopicInsight.


        :param reference_type: The reference_type of this TopicInsight.  # noqa: E501
        :type: TopicReferenceType
        """

        self._reference_type = reference_type

    @property
    def reference_url(self):
        """Gets the reference_url of this TopicInsight.  # noqa: E501


        :return: The reference_url of this TopicInsight.  # noqa: E501
        :rtype: str
        """
        return self._reference_url

    @reference_url.setter
    def reference_url(self, reference_url):
        """Sets the reference_url of this TopicInsight.


        :param reference_url: The reference_url of this TopicInsight.  # noqa: E501
        :type: str
        """

        self._reference_url = reference_url

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
        if issubclass(TopicInsight, dict):
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
        if not isinstance(other, TopicInsight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other