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

class ComputerVisionConnectionInput(object):
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
        'endpoint': 'str',
        'prediction_key': 'str',
        'prediction_resource_id': 'str',
        'training_key': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'prediction_key': 'predictionKey',
        'prediction_resource_id': 'predictionResourceId',
        'training_key': 'trainingKey'
    }

    def __init__(self, endpoint=None, prediction_key=None, prediction_resource_id=None, training_key=None):  # noqa: E501
        """ComputerVisionConnectionInput - a model defined in Swagger"""  # noqa: E501
        self._endpoint = None
        self._prediction_key = None
        self._prediction_resource_id = None
        self._training_key = None
        self.discriminator = None
        self.endpoint = endpoint
        self.prediction_key = prediction_key
        self.prediction_resource_id = prediction_resource_id
        self.training_key = training_key

    @property
    def endpoint(self):
        """Gets the endpoint of this ComputerVisionConnectionInput.  # noqa: E501


        :return: The endpoint of this ComputerVisionConnectionInput.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ComputerVisionConnectionInput.


        :param endpoint: The endpoint of this ComputerVisionConnectionInput.  # noqa: E501
        :type: str
        """
        if endpoint is None:
            raise ValueError("Invalid value for `endpoint`, must not be `None`")  # noqa: E501

        self._endpoint = endpoint

    @property
    def prediction_key(self):
        """Gets the prediction_key of this ComputerVisionConnectionInput.  # noqa: E501


        :return: The prediction_key of this ComputerVisionConnectionInput.  # noqa: E501
        :rtype: str
        """
        return self._prediction_key

    @prediction_key.setter
    def prediction_key(self, prediction_key):
        """Sets the prediction_key of this ComputerVisionConnectionInput.


        :param prediction_key: The prediction_key of this ComputerVisionConnectionInput.  # noqa: E501
        :type: str
        """
        if prediction_key is None:
            raise ValueError("Invalid value for `prediction_key`, must not be `None`")  # noqa: E501

        self._prediction_key = prediction_key

    @property
    def prediction_resource_id(self):
        """Gets the prediction_resource_id of this ComputerVisionConnectionInput.  # noqa: E501


        :return: The prediction_resource_id of this ComputerVisionConnectionInput.  # noqa: E501
        :rtype: str
        """
        return self._prediction_resource_id

    @prediction_resource_id.setter
    def prediction_resource_id(self, prediction_resource_id):
        """Sets the prediction_resource_id of this ComputerVisionConnectionInput.


        :param prediction_resource_id: The prediction_resource_id of this ComputerVisionConnectionInput.  # noqa: E501
        :type: str
        """
        if prediction_resource_id is None:
            raise ValueError("Invalid value for `prediction_resource_id`, must not be `None`")  # noqa: E501

        self._prediction_resource_id = prediction_resource_id

    @property
    def training_key(self):
        """Gets the training_key of this ComputerVisionConnectionInput.  # noqa: E501


        :return: The training_key of this ComputerVisionConnectionInput.  # noqa: E501
        :rtype: str
        """
        return self._training_key

    @training_key.setter
    def training_key(self, training_key):
        """Sets the training_key of this ComputerVisionConnectionInput.


        :param training_key: The training_key of this ComputerVisionConnectionInput.  # noqa: E501
        :type: str
        """
        if training_key is None:
            raise ValueError("Invalid value for `training_key`, must not be `None`")  # noqa: E501

        self._training_key = training_key

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
        if issubclass(ComputerVisionConnectionInput, dict):
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
        if not isinstance(other, ComputerVisionConnectionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
