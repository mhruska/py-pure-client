# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.38
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_38 import models

class Admin(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'api_token': 'ApiToken',
        'is_local': 'bool',
        'locked': 'bool',
        'lockout_remaining': 'int',
        'password': 'str',
        'public_key': 'str',
        'role': 'AdminRole',
        'management_access_policies': 'list[ReferenceWithType]'
    }

    attribute_map = {
        'name': 'name',
        'api_token': 'api_token',
        'is_local': 'is_local',
        'locked': 'locked',
        'lockout_remaining': 'lockout_remaining',
        'password': 'password',
        'public_key': 'public_key',
        'role': 'role',
        'management_access_policies': 'management_access_policies'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        api_token=None,  # type: models.ApiToken
        is_local=None,  # type: bool
        locked=None,  # type: bool
        lockout_remaining=None,  # type: int
        password=None,  # type: str
        public_key=None,  # type: str
        role=None,  # type: models.AdminRole
        management_access_policies=None,  # type: List[models.ReferenceWithType]
    ):
        """
        Keyword args:
            name (str): A user-specified name. The name must be locally unique and cannot be changed.
            api_token (ApiToken)
            is_local (bool): Returns a value of `true` if the user is local to the machine.
            locked (bool): Returns a value of `true` if the user is currently locked out. otherwise `false`. Change to `false` to unlock a user. This field is only visible to `array_admin` roles. For all other users, the value is always `null`.
            lockout_remaining (int): The remaining lockout period if the user is locked out, in milliseconds. This field is only visible to `array_admin` roles. For all other users, the value is always `null`.
            password (str): Password associated with the account.
            public_key (str): Public key for SSH access. Multiple public keys can be specified, separated by newlines.
            role (AdminRole)
            management_access_policies (list[ReferenceWithType]): List of management access policies associated with the administrator.
        """
        if name is not None:
            self.name = name
        if api_token is not None:
            self.api_token = api_token
        if is_local is not None:
            self.is_local = is_local
        if locked is not None:
            self.locked = locked
        if lockout_remaining is not None:
            self.lockout_remaining = lockout_remaining
        if password is not None:
            self.password = password
        if public_key is not None:
            self.public_key = public_key
        if role is not None:
            self.role = role
        if management_access_policies is not None:
            self.management_access_policies = management_access_policies

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Admin`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Admin`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Admin`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Admin`".format(key))
        object.__delattr__(self, key)

    def keys(self):
        return self.attribute_map.keys()

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
        if issubclass(Admin, dict):
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
        if not isinstance(other, Admin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
