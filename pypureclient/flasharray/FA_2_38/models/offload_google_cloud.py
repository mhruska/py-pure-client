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

class OffloadGoogleCloud(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_key_id': 'str',
        'bucket': 'str',
        'secret_access_key': 'str',
        'profile': 'str'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'bucket': 'bucket',
        'secret_access_key': 'secret_access_key',
        'profile': 'profile'
    }

    required_args = {
    }

    def __init__(
        self,
        access_key_id=None,  # type: str
        bucket=None,  # type: str
        secret_access_key=None,  # type: str
        profile=None,  # type: str
    ):
        """
        Keyword args:
            access_key_id (str): The access key ID of the Google Cloud account used to create a connection between the array and a Google Cloud offload target. The access key ID is 24 characters in length and is only accepted when creating the connection between the array and the Google Cloud offload target. The `access_key_id`, `secret_access_key`, and `bucket` parameters must be set together.
            bucket (str): The name of the Google Cloud Storage bucket to which the data will be offloaded. Grant basic read and write access permissions to the bucket and verify that the bucket is empty of all objects. The `access_key_id`, `secret_access_key`, and `bucket` parameters must be set together.
            secret_access_key (str): The secret access key that goes with the access key ID of the Google Cloud account. The secret access key is 40 characters in length is only accepted when creating the connection between the array and the Google Cloud offload target. The `access_key_id`, `secret_access_key`, and `bucket` parameters must be set together.
            profile (str): The offload target profile that will be selected for this target. This option allows more granular configuration for the target on top of the `protocol` parameter. Values include `gcp`.
        """
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if bucket is not None:
            self.bucket = bucket
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if profile is not None:
            self.profile = profile

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OffloadGoogleCloud`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OffloadGoogleCloud`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OffloadGoogleCloud`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OffloadGoogleCloud`".format(key))
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
        if issubclass(OffloadGoogleCloud, dict):
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
        if not isinstance(other, OffloadGoogleCloud):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
