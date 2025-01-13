# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_2 import models

class SubscriptionAsset(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'as_of': 'int',
        'id': 'str',
        'name': 'str',
        'activation_date': 'int',
        'array': 'SubscriptionAssetArray',
        'end_of_life_date': 'int',
        'install_address': 'BaseAddress',
        'license': 'FixedReference',
        'subscription': 'FixedReference'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'activation_date': 'activation_date',
        'array': 'array',
        'end_of_life_date': 'end_of_life_date',
        'install_address': 'install_address',
        'license': 'license',
        'subscription': 'subscription'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        id=None,  # type: str
        name=None,  # type: str
        activation_date=None,  # type: int
        array=None,  # type: models.SubscriptionAssetArray
        end_of_life_date=None,  # type: int
        install_address=None,  # type: models.BaseAddress
        license=None,  # type: models.FixedReference
        subscription=None,  # type: models.FixedReference
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            name (str): A non-modifiable, locally unique name chosen by the system.
            activation_date (int): The date when the appliance is activated under the license. Represented as a timestamp of 00:00 on that date in UTC, in milliseconds since UNIX epoch.
            array (SubscriptionAssetArray): The specific fields for assets that are arrays.
            end_of_life_date (int): The date when the appliance hardware reach end of life and Pure no longer provide support. Represented as a timestamp of 00:00 on that date in UTC, in milliseconds since UNIX epoch.
            install_address (BaseAddress): The address where the appliance is installed. This address is also where replacement parts will be shipped to.
            license (FixedReference): A reference to which license this appliance belongs.
            subscription (FixedReference): A reference to which subscription this appliance belongs.
        """
        if as_of is not None:
            self.as_of = as_of
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if activation_date is not None:
            self.activation_date = activation_date
        if array is not None:
            self.array = array
        if end_of_life_date is not None:
            self.end_of_life_date = end_of_life_date
        if install_address is not None:
            self.install_address = install_address
        if license is not None:
            self.license = license
        if subscription is not None:
            self.subscription = subscription

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SubscriptionAsset`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SubscriptionAsset`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SubscriptionAsset`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SubscriptionAsset`".format(key))
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
        if issubclass(SubscriptionAsset, dict):
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
        if not isinstance(other, SubscriptionAsset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
