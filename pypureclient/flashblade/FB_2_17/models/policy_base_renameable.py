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

class PolicyBaseRenameable(object):
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
        'policy_type': 'str',
        'location': 'FixedReference',
        'is_local': 'bool',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'policy_type': 'policy_type',
        'location': 'location',
        'is_local': 'is_local',
        'enabled': 'enabled'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        policy_type=None,  # type: str
        location=None,  # type: models.FixedReference
        is_local=None,  # type: bool
        enabled=None,  # type: bool
    ):
        """
        Keyword args:
            name (str): A name chosen by the user. Can be changed. Must be locally unique. 
            id (str): A non-modifiable, globally unique ID chosen by the system. 
            policy_type (str): Type of the policy. Valid values include `alert`, `audit`, `bucket-access`, `cross-origin-resource-sharing`, `network-access`, `nfs`, `object-access`, `smb-client`, `smb-share`, `snapshot`, `ssh-certificate-authority`, and `worm-data`. 
            location (FixedReference): Reference to the array where the policy is defined.
            is_local (bool): Whether the policy is defined on the local array.
            enabled (bool): If `true`, the policy is enabled. If not specified, defaults to `true`. 
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if policy_type is not None:
            self.policy_type = policy_type
        if location is not None:
            self.location = location
        if is_local is not None:
            self.is_local = is_local
        if enabled is not None:
            self.enabled = enabled

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyBaseRenameable`".format(key))
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
        if issubclass(PolicyBaseRenameable, dict):
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
        if not isinstance(other, PolicyBaseRenameable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
