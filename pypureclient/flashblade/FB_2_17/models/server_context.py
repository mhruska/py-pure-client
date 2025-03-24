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

class ServerContext(object):
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
        'directory_services': 'list[Reference]',
        'dns': 'list[Reference]',
        'created': 'int',
        'context': 'Reference'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'directory_services': 'directory_services',
        'dns': 'dns',
        'created': 'created',
        'context': 'context'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        directory_services=None,  # type: List[models.Reference]
        dns=None,  # type: List[models.Reference]
        created=None,  # type: int
        context=None,  # type: models.Reference
    ):
        """
        Keyword args:
            name (str): A name chosen by the user. Can be changed. Must be locally unique. 
            id (str): A non-modifiable, globally unique ID chosen by the system. 
            directory_services (list[Reference]): The directory service config to be used by this server. 
            dns (list[Reference]): The DNS config to be used by this server. 
            created (int): Creation timestamp of the server.
            context (Reference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request.  Other parameters provided with the request, such as names of volumes or snapshots,  are resolved relative to the provided `context`. 
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if directory_services is not None:
            self.directory_services = directory_services
        if dns is not None:
            self.dns = dns
        if created is not None:
            self.created = created
        if context is not None:
            self.context = context

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ServerContext`".format(key))
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
        if issubclass(ServerContext, dict):
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
        if not isinstance(other, ServerContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
