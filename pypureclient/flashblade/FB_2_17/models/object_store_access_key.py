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

class ObjectStoreAccessKey(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'context': 'Reference',
        'created': 'int',
        'secret_access_key': 'str',
        'user': 'FixedReference',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'context': 'context',
        'created': 'created',
        'secret_access_key': 'secret_access_key',
        'user': 'user',
        'enabled': 'enabled'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        context=None,  # type: models.Reference
        created=None,  # type: int
        secret_access_key=None,  # type: str
        user=None,  # type: models.FixedReference
        enabled=None,  # type: bool
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            context (Reference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request.  Other parameters provided with the request, such as names of volumes or snapshots,  are resolved relative to the provided `context`. 
            created (int): Creation timestamp of the object.
            secret_access_key (str): The secret access key, only populated on creation if it is not imported from another FlashBlade. 
            user (FixedReference): Reference of the associated user.
            enabled (bool): Is the access key enabled? If not specified, defaults to `false`. 
        """
        if name is not None:
            self.name = name
        if context is not None:
            self.context = context
        if created is not None:
            self.created = created
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if user is not None:
            self.user = user
        if enabled is not None:
            self.enabled = enabled

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ObjectStoreAccessKey`".format(key))
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
        if issubclass(ObjectStoreAccessKey, dict):
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
        if not isinstance(other, ObjectStoreAccessKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
