# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.17, developed by Pure Storage, Inc. (http://www.purestorage.com/). 

    OpenAPI spec version: 2.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_17 import models

class SnmpManager(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'notification': 'str',
        'v2c': 'SnmpV2c',
        'host': 'str',
        'v3': 'SnmpV3',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'notification': 'notification',
        'v2c': 'v2c',
        'host': 'host',
        'v3': 'v3',
        'version': 'version'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        notification=None,  # type: str
        v2c=None,  # type: models.SnmpV2c
        host=None,  # type: str
        v3=None,  # type: models.SnmpV3
        version=None,  # type: str
    ):
        """
        Keyword args:
            name (str): A name chosen by the user. Can be changed. Must be locally unique. 
            id (str): A non-modifiable, globally unique ID chosen by the system. 
            notification (str): The type of notification the agent will send. Valid values are `inform` and `trap`. 
            v2c (SnmpV2c)
            host (str): DNS hostname or IP address of a computer that hosts an SNMP manager to which Purity is to send trap messages when it generates alerts. 
            v3 (SnmpV3)
            version (str): Version of the SNMP protocol to be used by Purity in communications with the specified manager. Valid values are `v2c` and `v3`. 
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if notification is not None:
            self.notification = notification
        if v2c is not None:
            self.v2c = v2c
        if host is not None:
            self.host = host
        if v3 is not None:
            self.v3 = v3
        if version is not None:
            self.version = version

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SnmpManager`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
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
        if issubclass(SnmpManager, dict):
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
        if not isinstance(other, SnmpManager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
