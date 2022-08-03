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

class AccountAmsInfo(object):
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
        'aad_application_id': 'str',
        'aad_tenant_id': 'str',
        'connected': 'bool',
        'event_grid_provider_registered': 'bool',
        'name': 'str',
        'resource_group': 'str',
        'streaming_endpoint_started': 'bool',
        'subscription_id': 'str'
    }

    attribute_map = {
        'aad_application_id': 'aadApplicationId',
        'aad_tenant_id': 'aadTenantId',
        'connected': 'connected',
        'event_grid_provider_registered': 'eventGridProviderRegistered',
        'name': 'name',
        'resource_group': 'resourceGroup',
        'streaming_endpoint_started': 'streamingEndpointStarted',
        'subscription_id': 'subscriptionId'
    }

    def __init__(self, aad_application_id=None, aad_tenant_id=None, connected=None, event_grid_provider_registered=None, name=None, resource_group=None, streaming_endpoint_started=None, subscription_id=None):  # noqa: E501
        """AccountAmsInfo - a model defined in Swagger"""  # noqa: E501
        self._aad_application_id = None
        self._aad_tenant_id = None
        self._connected = None
        self._event_grid_provider_registered = None
        self._name = None
        self._resource_group = None
        self._streaming_endpoint_started = None
        self._subscription_id = None
        self.discriminator = None
        if aad_application_id is not None:
            self.aad_application_id = aad_application_id
        if aad_tenant_id is not None:
            self.aad_tenant_id = aad_tenant_id
        if connected is not None:
            self.connected = connected
        if event_grid_provider_registered is not None:
            self.event_grid_provider_registered = event_grid_provider_registered
        if name is not None:
            self.name = name
        if resource_group is not None:
            self.resource_group = resource_group
        if streaming_endpoint_started is not None:
            self.streaming_endpoint_started = streaming_endpoint_started
        if subscription_id is not None:
            self.subscription_id = subscription_id

    @property
    def aad_application_id(self):
        """Gets the aad_application_id of this AccountAmsInfo.  # noqa: E501


        :return: The aad_application_id of this AccountAmsInfo.  # noqa: E501
        :rtype: str
        """
        return self._aad_application_id

    @aad_application_id.setter
    def aad_application_id(self, aad_application_id):
        """Sets the aad_application_id of this AccountAmsInfo.


        :param aad_application_id: The aad_application_id of this AccountAmsInfo.  # noqa: E501
        :type: str
        """

        self._aad_application_id = aad_application_id

    @property
    def aad_tenant_id(self):
        """Gets the aad_tenant_id of this AccountAmsInfo.  # noqa: E501


        :return: The aad_tenant_id of this AccountAmsInfo.  # noqa: E501
        :rtype: str
        """
        return self._aad_tenant_id

    @aad_tenant_id.setter
    def aad_tenant_id(self, aad_tenant_id):
        """Sets the aad_tenant_id of this AccountAmsInfo.


        :param aad_tenant_id: The aad_tenant_id of this AccountAmsInfo.  # noqa: E501
        :type: str
        """

        self._aad_tenant_id = aad_tenant_id

    @property
    def connected(self):
        """Gets the connected of this AccountAmsInfo.  # noqa: E501


        :return: The connected of this AccountAmsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this AccountAmsInfo.


        :param connected: The connected of this AccountAmsInfo.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def event_grid_provider_registered(self):
        """Gets the event_grid_provider_registered of this AccountAmsInfo.  # noqa: E501


        :return: The event_grid_provider_registered of this AccountAmsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._event_grid_provider_registered

    @event_grid_provider_registered.setter
    def event_grid_provider_registered(self, event_grid_provider_registered):
        """Sets the event_grid_provider_registered of this AccountAmsInfo.


        :param event_grid_provider_registered: The event_grid_provider_registered of this AccountAmsInfo.  # noqa: E501
        :type: bool
        """

        self._event_grid_provider_registered = event_grid_provider_registered

    @property
    def name(self):
        """Gets the name of this AccountAmsInfo.  # noqa: E501


        :return: The name of this AccountAmsInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountAmsInfo.


        :param name: The name of this AccountAmsInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource_group(self):
        """Gets the resource_group of this AccountAmsInfo.  # noqa: E501


        :return: The resource_group of this AccountAmsInfo.  # noqa: E501
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """Sets the resource_group of this AccountAmsInfo.


        :param resource_group: The resource_group of this AccountAmsInfo.  # noqa: E501
        :type: str
        """

        self._resource_group = resource_group

    @property
    def streaming_endpoint_started(self):
        """Gets the streaming_endpoint_started of this AccountAmsInfo.  # noqa: E501


        :return: The streaming_endpoint_started of this AccountAmsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._streaming_endpoint_started

    @streaming_endpoint_started.setter
    def streaming_endpoint_started(self, streaming_endpoint_started):
        """Sets the streaming_endpoint_started of this AccountAmsInfo.


        :param streaming_endpoint_started: The streaming_endpoint_started of this AccountAmsInfo.  # noqa: E501
        :type: bool
        """

        self._streaming_endpoint_started = streaming_endpoint_started

    @property
    def subscription_id(self):
        """Gets the subscription_id of this AccountAmsInfo.  # noqa: E501


        :return: The subscription_id of this AccountAmsInfo.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this AccountAmsInfo.


        :param subscription_id: The subscription_id of this AccountAmsInfo.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

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
        if issubclass(AccountAmsInfo, dict):
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
        if not isinstance(other, AccountAmsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other