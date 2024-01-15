# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.12, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_12 import models

class UserQuota(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'file_system': 'FixedReference',
        'file_system_default_quota': 'int',
        'quota': 'int',
        'usage': 'int',
        'user': 'User'
    }

    attribute_map = {
        'name': 'name',
        'file_system': 'file_system',
        'file_system_default_quota': 'file_system_default_quota',
        'quota': 'quota',
        'usage': 'usage',
        'user': 'user'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        file_system=None,  # type: models.FixedReference
        file_system_default_quota=None,  # type: int
        quota=None,  # type: int
        usage=None,  # type: int
        user=None,  # type: models.User
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            file_system (FixedReference)
            file_system_default_quota (int): File system's default user quota (in bytes). If it is `0`, it means there is no default quota. This will be the effective user quota if the user doesn't have an individual quota. This default quota is set through the `file-systems` endpoint.
            quota (int): The limit of the quota (in bytes) for the specified user, cannot be `0`. If specified, this value will override the file system's default user quota.
            usage (int): The usage of the file system (in bytes) by the specified user.
            user (User): The user on which this quota is enforced.
        """
        if name is not None:
            self.name = name
        if file_system is not None:
            self.file_system = file_system
        if file_system_default_quota is not None:
            self.file_system_default_quota = file_system_default_quota
        if quota is not None:
            self.quota = quota
        if usage is not None:
            self.usage = usage
        if user is not None:
            self.user = user

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `UserQuota`".format(key))
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
        if issubclass(UserQuota, dict):
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
        if not isinstance(other, UserQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
