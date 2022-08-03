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

class TranscriptLineInsight(object):
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
        'id': 'int',
        'instances': 'list[InsightInstance]',
        'language': 'OneOfTranscriptLineInsightLanguage',
        'speaker_id': 'int',
        'text': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'id': 'id',
        'instances': 'instances',
        'language': 'language',
        'speaker_id': 'speakerId',
        'text': 'text'
    }

    def __init__(self, confidence=None, id=None, instances=None, language=None, speaker_id=None, text=None):  # noqa: E501
        """TranscriptLineInsight - a model defined in Swagger"""  # noqa: E501
        self._confidence = None
        self._id = None
        self._instances = None
        self._language = None
        self._speaker_id = None
        self._text = None
        self.discriminator = None
        if confidence is not None:
            self.confidence = confidence
        if id is not None:
            self.id = id
        if instances is not None:
            self.instances = instances
        if language is not None:
            self.language = language
        if speaker_id is not None:
            self.speaker_id = speaker_id
        if text is not None:
            self.text = text

    @property
    def confidence(self):
        """Gets the confidence of this TranscriptLineInsight.  # noqa: E501


        :return: The confidence of this TranscriptLineInsight.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TranscriptLineInsight.


        :param confidence: The confidence of this TranscriptLineInsight.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

    @property
    def id(self):
        """Gets the id of this TranscriptLineInsight.  # noqa: E501


        :return: The id of this TranscriptLineInsight.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TranscriptLineInsight.


        :param id: The id of this TranscriptLineInsight.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def instances(self):
        """Gets the instances of this TranscriptLineInsight.  # noqa: E501


        :return: The instances of this TranscriptLineInsight.  # noqa: E501
        :rtype: list[InsightInstance]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this TranscriptLineInsight.


        :param instances: The instances of this TranscriptLineInsight.  # noqa: E501
        :type: list[InsightInstance]
        """

        self._instances = instances

    @property
    def language(self):
        """Gets the language of this TranscriptLineInsight.  # noqa: E501


        :return: The language of this TranscriptLineInsight.  # noqa: E501
        :rtype: OneOfTranscriptLineInsightLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TranscriptLineInsight.


        :param language: The language of this TranscriptLineInsight.  # noqa: E501
        :type: OneOfTranscriptLineInsightLanguage
        """

        self._language = language

    @property
    def speaker_id(self):
        """Gets the speaker_id of this TranscriptLineInsight.  # noqa: E501


        :return: The speaker_id of this TranscriptLineInsight.  # noqa: E501
        :rtype: int
        """
        return self._speaker_id

    @speaker_id.setter
    def speaker_id(self, speaker_id):
        """Sets the speaker_id of this TranscriptLineInsight.


        :param speaker_id: The speaker_id of this TranscriptLineInsight.  # noqa: E501
        :type: int
        """

        self._speaker_id = speaker_id

    @property
    def text(self):
        """Gets the text of this TranscriptLineInsight.  # noqa: E501


        :return: The text of this TranscriptLineInsight.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TranscriptLineInsight.


        :param text: The text of this TranscriptLineInsight.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(TranscriptLineInsight, dict):
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
        if not isinstance(other, TranscriptLineInsight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
