# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.14, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_14 import models

class MemberLink(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'local_file_system': 'FixedReference',
        'remote': 'FixedReferenceNoResourceType',
        'remote_file_system': 'FixedReferenceNoResourceType'
    }

    attribute_map = {
        'local_file_system': 'local_file_system',
        'remote': 'remote',
        'remote_file_system': 'remote_file_system'
    }

    required_args = {
    }

    def __init__(
        self,
        local_file_system=None,  # type: models.FixedReference
        remote=None,  # type: models.FixedReferenceNoResourceType
        remote_file_system=None,  # type: models.FixedReferenceNoResourceType
    ):
        """
        Keyword args:
            local_file_system (FixedReference): Reference to a local file system.
            remote (FixedReferenceNoResourceType): Reference to a remote array.
            remote_file_system (FixedReferenceNoResourceType): Reference to a remote file system.
        """
        if local_file_system is not None:
            self.local_file_system = local_file_system
        if remote is not None:
            self.remote = remote
        if remote_file_system is not None:
            self.remote_file_system = remote_file_system

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `MemberLink`".format(key))
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
        if issubclass(MemberLink, dict):
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
        if not isinstance(other, MemberLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
