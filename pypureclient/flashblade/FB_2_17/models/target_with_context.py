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

class TargetWithContext(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'address': 'str',
        'ca_certificate_group': 'FixedReference',
        'status_details': 'str',
        'status': 'str',
        'context': 'Reference'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'address': 'address',
        'ca_certificate_group': 'ca_certificate_group',
        'status_details': 'status_details',
        'status': 'status',
        'context': 'context'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        address=None,  # type: str
        ca_certificate_group=None,  # type: models.FixedReference
        status_details=None,  # type: str
        status=None,  # type: str
        context=None,  # type: models.Reference
    ):
        """
        Keyword args:
            name (str): A name chosen by the user. Can be changed. Must be locally unique. 
            id (str): A non-modifiable, globally unique ID chosen by the system. 
            address (str): IP address or FQDN of the target system.
            ca_certificate_group (FixedReference): The group of CA certificates that can be used, in addition to well-known Certificate Authority certificates, in order to establish a secure connection to the target system. Defaults to a reference to the `_default_replication_certs` group. 
            status_details (str): Additional information describing any issues encountered when connecting, or `null` if the `status` is `connected`. 
            status (str): Status of the connection. Valid values are `connected` and `connecting`. `connected` - The connection is OK. `connecting` - No connection exists and the array is trying to reconnect to the target. 
            context (Reference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request.  Other parameters provided with the request, such as names of volumes or snapshots,  are resolved relative to the provided `context`. 
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if ca_certificate_group is not None:
            self.ca_certificate_group = ca_certificate_group
        if status_details is not None:
            self.status_details = status_details
        if status is not None:
            self.status = status
        if context is not None:
            self.context = context

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `TargetWithContext`".format(key))
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
        if issubclass(TargetWithContext, dict):
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
        if not isinstance(other, TargetWithContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
