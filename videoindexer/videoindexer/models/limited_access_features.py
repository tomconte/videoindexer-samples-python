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

class LimitedAccessFeatures(object):
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
        'is_celebrity_recognition_enabled': 'bool',
        'is_face_detection_enabled': 'bool',
        'is_face_identification_enabled': 'bool'
    }

    attribute_map = {
        'is_celebrity_recognition_enabled': 'isCelebrityRecognitionEnabled',
        'is_face_detection_enabled': 'isFaceDetectionEnabled',
        'is_face_identification_enabled': 'isFaceIdentificationEnabled'
    }

    def __init__(self, is_celebrity_recognition_enabled=None, is_face_detection_enabled=None, is_face_identification_enabled=None):  # noqa: E501
        """LimitedAccessFeatures - a model defined in Swagger"""  # noqa: E501
        self._is_celebrity_recognition_enabled = None
        self._is_face_detection_enabled = None
        self._is_face_identification_enabled = None
        self.discriminator = None
        if is_celebrity_recognition_enabled is not None:
            self.is_celebrity_recognition_enabled = is_celebrity_recognition_enabled
        if is_face_detection_enabled is not None:
            self.is_face_detection_enabled = is_face_detection_enabled
        if is_face_identification_enabled is not None:
            self.is_face_identification_enabled = is_face_identification_enabled

    @property
    def is_celebrity_recognition_enabled(self):
        """Gets the is_celebrity_recognition_enabled of this LimitedAccessFeatures.  # noqa: E501


        :return: The is_celebrity_recognition_enabled of this LimitedAccessFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._is_celebrity_recognition_enabled

    @is_celebrity_recognition_enabled.setter
    def is_celebrity_recognition_enabled(self, is_celebrity_recognition_enabled):
        """Sets the is_celebrity_recognition_enabled of this LimitedAccessFeatures.


        :param is_celebrity_recognition_enabled: The is_celebrity_recognition_enabled of this LimitedAccessFeatures.  # noqa: E501
        :type: bool
        """

        self._is_celebrity_recognition_enabled = is_celebrity_recognition_enabled

    @property
    def is_face_detection_enabled(self):
        """Gets the is_face_detection_enabled of this LimitedAccessFeatures.  # noqa: E501


        :return: The is_face_detection_enabled of this LimitedAccessFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._is_face_detection_enabled

    @is_face_detection_enabled.setter
    def is_face_detection_enabled(self, is_face_detection_enabled):
        """Sets the is_face_detection_enabled of this LimitedAccessFeatures.


        :param is_face_detection_enabled: The is_face_detection_enabled of this LimitedAccessFeatures.  # noqa: E501
        :type: bool
        """

        self._is_face_detection_enabled = is_face_detection_enabled

    @property
    def is_face_identification_enabled(self):
        """Gets the is_face_identification_enabled of this LimitedAccessFeatures.  # noqa: E501


        :return: The is_face_identification_enabled of this LimitedAccessFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._is_face_identification_enabled

    @is_face_identification_enabled.setter
    def is_face_identification_enabled(self, is_face_identification_enabled):
        """Sets the is_face_identification_enabled of this LimitedAccessFeatures.


        :param is_face_identification_enabled: The is_face_identification_enabled of this LimitedAccessFeatures.  # noqa: E501
        :type: bool
        """

        self._is_face_identification_enabled = is_face_identification_enabled

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
        if issubclass(LimitedAccessFeatures, dict):
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
        if not isinstance(other, LimitedAccessFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
