# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_19 import models

class ConnectionPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'lun': 'int',
        'protocol_endpoint': 'Reference'
    }

    attribute_map = {
        'lun': 'lun',
        'protocol_endpoint': 'protocol_endpoint'
    }

    required_args = {
    }

    def __init__(
        self,
        lun=None,  # type: int
        protocol_endpoint=None,  # type: models.Reference
    ):
        """
        Keyword args:
            lun (int): The logical unit number (LUN) by which the specified hosts are to address the specified volume. If the LUN is not specified, the system automatically assigns a LUN to the connection. To automatically assign a LUN to a private connection, the system starts at LUN `1` and counts up to the maximum LUN `4095`, assigning the first available LUN to the connection. For shared connections, the system starts at LUN `254` and counts down to the minimum LUN `1`, assigning the first available LUN to the connection. If all LUNs in the `[1...254]` range are taken, the system starts at LUN `255` and counts up to the maximum LUN `4095`, assigning the first available LUN to the connection.
            protocol_endpoint (Reference): A protocol endpoint (also known as a conglomerate volume) which acts as a proxy through which virtual volumes are created and then connected to VMware ESXi hosts or host groups. The protocol endpoint itself does not serve I/Os; instead, its job is to form connections between FlashArray volumes and ESXi hosts and host groups.
        """
        if lun is not None:
            self.lun = lun
        if protocol_endpoint is not None:
            self.protocol_endpoint = protocol_endpoint

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ConnectionPost`".format(key))
        if key == "lun" and value is not None:
            if value > 4095:
                raise ValueError("Invalid value for `lun`, value must be less than or equal to `4095`")
            if value < 1:
                raise ValueError("Invalid value for `lun`, must be a value greater than or equal to `1`")
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
        if issubclass(ConnectionPost, dict):
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
        if not isinstance(other, ConnectionPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other