# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.39
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_39 import models

class ArrayErasure(object):
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
        'status': 'str',
        'image_source': 'str',
        'image_version': 'str',
        'image_download_progress': 'float',
        'details': 'str',
        'sanitization_certificate': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'image_source': 'image_source',
        'image_version': 'image_version',
        'image_download_progress': 'image_download_progress',
        'details': 'details',
        'sanitization_certificate': 'sanitization_certificate'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        status=None,  # type: str
        image_source=None,  # type: str
        image_version=None,  # type: str
        image_download_progress=None,  # type: float
        details=None,  # type: str
        sanitization_certificate=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A user-specified name. The name must be locally unique and can be changed.
            status (str): The status of the factory reset process. Valid values include `resetting`, `reset_failed`, `reimage_failed`, `waiting_for_finalize`, `downloading`, `downloaded`, and `download_failed`. A status of `resetting` indicates that the factory reset is running. A status of `reset_failed` indicates that the factory reset encountered a failure. A status of `reimage_failed` indicates that the factory reset failed to reimage the array. A status of `waiting_for_finalize` indicates that the factory reset has finished sanitizing drives, and is waiting to be finalized. A status of `downloading` indicates that the factory reset is downloading ISO image. A status of `downloaded` indicates that the factory reset completed ISO image download. A status of `download_failed` indicates that the factory reset failed to download ISO image.
            image_source (str): Source of the ISO image to download. Valid values include `auto` and URLs. `auto` means download the image from Pure1 cloud, and a URL means download the image from the specified URL.
            image_version (str): Version of the image to download and install.
            image_download_progress (float): The progress of the ISO image download, displayed in decimal format.
            details (str): The detailed reason of the `status`.
            sanitization_certificate (str): The sanitization certificate of the factory reset, which complies with the standard described in NIST SP800-88R1 section 4.8.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if image_source is not None:
            self.image_source = image_source
        if image_version is not None:
            self.image_version = image_version
        if image_download_progress is not None:
            self.image_download_progress = image_download_progress
        if details is not None:
            self.details = details
        if sanitization_certificate is not None:
            self.sanitization_certificate = sanitization_certificate

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayErasure`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayErasure`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayErasure`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayErasure`".format(key))
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
        if issubclass(ArrayErasure, dict):
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
        if not isinstance(other, ArrayErasure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
