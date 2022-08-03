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

class LanguageModelEdit(object):
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
        'create_date': 'datetime',
        'current_value': 'str',
        'id': 'int',
        'line_id': 'int',
        'linguistic_training_data_groups_id': 'int',
        'original_value': 'str',
        'video_id': 'str',
        'video_name': 'str'
    }

    attribute_map = {
        'create_date': 'createDate',
        'current_value': 'currentValue',
        'id': 'id',
        'line_id': 'lineId',
        'linguistic_training_data_groups_id': 'linguisticTrainingDataGroupsId',
        'original_value': 'originalValue',
        'video_id': 'videoId',
        'video_name': 'videoName'
    }

    def __init__(self, create_date=None, current_value=None, id=None, line_id=None, linguistic_training_data_groups_id=None, original_value=None, video_id=None, video_name=None):  # noqa: E501
        """LanguageModelEdit - a model defined in Swagger"""  # noqa: E501
        self._create_date = None
        self._current_value = None
        self._id = None
        self._line_id = None
        self._linguistic_training_data_groups_id = None
        self._original_value = None
        self._video_id = None
        self._video_name = None
        self.discriminator = None
        if create_date is not None:
            self.create_date = create_date
        if current_value is not None:
            self.current_value = current_value
        if id is not None:
            self.id = id
        if line_id is not None:
            self.line_id = line_id
        if linguistic_training_data_groups_id is not None:
            self.linguistic_training_data_groups_id = linguistic_training_data_groups_id
        if original_value is not None:
            self.original_value = original_value
        if video_id is not None:
            self.video_id = video_id
        if video_name is not None:
            self.video_name = video_name

    @property
    def create_date(self):
        """Gets the create_date of this LanguageModelEdit.  # noqa: E501


        :return: The create_date of this LanguageModelEdit.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this LanguageModelEdit.


        :param create_date: The create_date of this LanguageModelEdit.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def current_value(self):
        """Gets the current_value of this LanguageModelEdit.  # noqa: E501


        :return: The current_value of this LanguageModelEdit.  # noqa: E501
        :rtype: str
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """Sets the current_value of this LanguageModelEdit.


        :param current_value: The current_value of this LanguageModelEdit.  # noqa: E501
        :type: str
        """

        self._current_value = current_value

    @property
    def id(self):
        """Gets the id of this LanguageModelEdit.  # noqa: E501


        :return: The id of this LanguageModelEdit.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LanguageModelEdit.


        :param id: The id of this LanguageModelEdit.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def line_id(self):
        """Gets the line_id of this LanguageModelEdit.  # noqa: E501


        :return: The line_id of this LanguageModelEdit.  # noqa: E501
        :rtype: int
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this LanguageModelEdit.


        :param line_id: The line_id of this LanguageModelEdit.  # noqa: E501
        :type: int
        """

        self._line_id = line_id

    @property
    def linguistic_training_data_groups_id(self):
        """Gets the linguistic_training_data_groups_id of this LanguageModelEdit.  # noqa: E501


        :return: The linguistic_training_data_groups_id of this LanguageModelEdit.  # noqa: E501
        :rtype: int
        """
        return self._linguistic_training_data_groups_id

    @linguistic_training_data_groups_id.setter
    def linguistic_training_data_groups_id(self, linguistic_training_data_groups_id):
        """Sets the linguistic_training_data_groups_id of this LanguageModelEdit.


        :param linguistic_training_data_groups_id: The linguistic_training_data_groups_id of this LanguageModelEdit.  # noqa: E501
        :type: int
        """

        self._linguistic_training_data_groups_id = linguistic_training_data_groups_id

    @property
    def original_value(self):
        """Gets the original_value of this LanguageModelEdit.  # noqa: E501


        :return: The original_value of this LanguageModelEdit.  # noqa: E501
        :rtype: str
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        """Sets the original_value of this LanguageModelEdit.


        :param original_value: The original_value of this LanguageModelEdit.  # noqa: E501
        :type: str
        """

        self._original_value = original_value

    @property
    def video_id(self):
        """Gets the video_id of this LanguageModelEdit.  # noqa: E501


        :return: The video_id of this LanguageModelEdit.  # noqa: E501
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this LanguageModelEdit.


        :param video_id: The video_id of this LanguageModelEdit.  # noqa: E501
        :type: str
        """

        self._video_id = video_id

    @property
    def video_name(self):
        """Gets the video_name of this LanguageModelEdit.  # noqa: E501


        :return: The video_name of this LanguageModelEdit.  # noqa: E501
        :rtype: str
        """
        return self._video_name

    @video_name.setter
    def video_name(self, video_name):
        """Sets the video_name of this LanguageModelEdit.


        :param video_name: The video_name of this LanguageModelEdit.  # noqa: E501
        :type: str
        """

        self._video_name = video_name

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
        if issubclass(LanguageModelEdit, dict):
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
        if not isinstance(other, LanguageModelEdit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other