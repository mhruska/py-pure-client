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

class ObjectLockConfigRequestBody(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'bool',
        'freeze_locked_objects': 'bool',
        'default_retention_mode': 'str',
        'default_retention': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'freeze_locked_objects': 'freeze_locked_objects',
        'default_retention_mode': 'default_retention_mode',
        'default_retention': 'default_retention'
    }

    required_args = {
    }

    def __init__(
        self,
        enabled=None,  # type: bool
        freeze_locked_objects=None,  # type: bool
        default_retention_mode=None,  # type: str
        default_retention=None,  # type: str
    ):
        """
        Keyword args:
            enabled (bool): If set to `true`, then S3 APIs relating to object lock may be used. 
            freeze_locked_objects (bool): If set to `true`, a locked object will be read-only and no new versions of the object may be created due to modifications. If not specified, defaults to `false`. 
            default_retention_mode (str): The retention mode used to apply locks on new objects if none is specified by the S3 client. Valid values include `compliance` and `governance`. If there is no default, this value is `null`. Use \"\" to clear. 
            default_retention (str): The retention period, in milliseconds, used to apply locks on new objects if none is specified by the S3 client. Valid values are any multiple of `86400000` (1 day), up to `3153600000000` (36500 days). If there is no default, this value is `null`. Use \"\" to clear. 
        """
        if enabled is not None:
            self.enabled = enabled
        if freeze_locked_objects is not None:
            self.freeze_locked_objects = freeze_locked_objects
        if default_retention_mode is not None:
            self.default_retention_mode = default_retention_mode
        if default_retention is not None:
            self.default_retention = default_retention

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ObjectLockConfigRequestBody`".format(key))
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
        if issubclass(ObjectLockConfigRequestBody, dict):
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
        if not isinstance(other, ObjectLockConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
