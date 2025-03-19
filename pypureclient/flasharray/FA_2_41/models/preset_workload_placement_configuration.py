# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_41 import models

class PresetWorkloadPlacementConfiguration(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'storage_class': 'ReferenceWithType',
        'qos_configurations': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'storage_class': 'storage_class',
        'qos_configurations': 'qos_configurations'
    }

    required_args = {
        'name',
        'storage_class',
    }

    def __init__(
        self,
        name,  # type: str
        storage_class,  # type: models.ReferenceWithType
        qos_configurations=None,  # type: List[str]
    ):
        """
        Keyword args:
            name (str, required): The name of the placement configuration, by which other configuration objects in the preset can reference it. Name must be unique across all configuration objects in the preset.
            storage_class (ReferenceWithType, required): The storage class to which the placement and its associated storage resources may be deployed. Supports parameterization.
            qos_configurations (list[str]): The names of the QoS configurations to apply to the storage resources (such as volumes) in the placement. The limits defined in the QoS configurations will be shared across all storage resources in the placement.
        """
        self.name = name
        self.storage_class = storage_class
        if qos_configurations is not None:
            self.qos_configurations = qos_configurations

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadPlacementConfiguration`".format(key))
        if key == "name" and value is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if key == "storage_class" and value is None:
            raise ValueError("Invalid value for `storage_class`, must not be `None`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadPlacementConfiguration`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadPlacementConfiguration`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadPlacementConfiguration`".format(key))
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
        if issubclass(PresetWorkloadPlacementConfiguration, dict):
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
        if not isinstance(other, PresetWorkloadPlacementConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
