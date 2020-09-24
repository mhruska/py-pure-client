# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_1 import models

class Bucket(object):
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
        'arrays': 'list[FixedReference]',
        'account': 'FixedReference',
        'created': 'int',
        'destroyed': 'bool',
        'object_count': 'int',
        'versioning': 'str'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'arrays': 'arrays',
        'account': 'account',
        'created': 'created',
        'destroyed': 'destroyed',
        'object_count': 'object_count',
        'versioning': 'versioning'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        id=None,  # type: str
        name=None,  # type: str
        arrays=None,  # type: List[models.FixedReference]
        account=None,  # type: models.FixedReference
        created=None,  # type: int
        destroyed=None,  # type: bool
        object_count=None,  # type: int
        versioning=None,  # type: str
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            name (str): A modifiable, locally unique name chosen by the user.
            arrays (list[FixedReference]): The list of arrays where this resource exists. Many resources are on a single array, but some resources, such as pods, can be shared across multiple arrays.
            account (FixedReference)
            created (int): Creation time of the bucket, in milliseconds since Unix epoch.
            destroyed (bool): Returns a value of `true` if the bucket is destroyed, but not yet eradicated.
            object_count (int): The number of objects contained within the bucket.
            versioning (str): The versioning state for objects within the bucket. Valid values are `none`, `enabled`, and `suspended`.
        """
        if as_of is not None:
            self.as_of = as_of
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if arrays is not None:
            self.arrays = arrays
        if account is not None:
            self.account = account
        if created is not None:
            self.created = created
        if destroyed is not None:
            self.destroyed = destroyed
        if object_count is not None:
            self.object_count = object_count
        if versioning is not None:
            self.versioning = versioning

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Bucket`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
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
        if issubclass(Bucket, dict):
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
        if not isinstance(other, Bucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other