# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_26 import models

class VolumeGroupPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'qos': 'Qos',
        'priority_adjustment': 'PriorityAdjustment',
        'space': 'Space',
        'time_remaining': 'int',
        'volume_count': 'int',
        'destroyed': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'qos': 'qos',
        'priority_adjustment': 'priority_adjustment',
        'space': 'space',
        'time_remaining': 'time_remaining',
        'volume_count': 'volume_count',
        'destroyed': 'destroyed'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        qos=None,  # type: models.Qos
        priority_adjustment=None,  # type: models.PriorityAdjustment
        space=None,  # type: models.Space
        time_remaining=None,  # type: int
        volume_count=None,  # type: int
        destroyed=None,  # type: bool
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A user-specified name. The name must be locally unique and can be changed.
            qos (Qos)
            priority_adjustment (PriorityAdjustment)
            space (Space)
            time_remaining (int): The amount of time left until the destroyed volume group is permanently eradicated, measured in milliseconds.
            volume_count (int): The number of volumes in the volume group.
            destroyed (bool): If set to `true`, destroys a volume group. If set to `false`, recovers a destroyed volume group. If not specified, defaults to `false`.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if qos is not None:
            self.qos = qos
        if priority_adjustment is not None:
            self.priority_adjustment = priority_adjustment
        if space is not None:
            self.space = space
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if volume_count is not None:
            self.volume_count = volume_count
        if destroyed is not None:
            self.destroyed = destroyed

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeGroupPost`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeGroupPost`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeGroupPost`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeGroupPost`".format(key))
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
        if issubclass(VolumeGroupPost, dict):
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
        if not isinstance(other, VolumeGroupPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
