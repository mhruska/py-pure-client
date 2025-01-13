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

class DirectoryPerformance(object):
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
        'bytes_per_op': 'int',
        'bytes_per_read': 'int',
        'bytes_per_write': 'int',
        'others_per_sec': 'int',
        'read_bytes_per_sec': 'int',
        'reads_per_sec': 'int',
        'time': 'int',
        'usec_per_other_op': 'int',
        'usec_per_read_op': 'int',
        'usec_per_write_op': 'int',
        'write_bytes_per_sec': 'int',
        'writes_per_sec': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'bytes_per_op': 'bytes_per_op',
        'bytes_per_read': 'bytes_per_read',
        'bytes_per_write': 'bytes_per_write',
        'others_per_sec': 'others_per_sec',
        'read_bytes_per_sec': 'read_bytes_per_sec',
        'reads_per_sec': 'reads_per_sec',
        'time': 'time',
        'usec_per_other_op': 'usec_per_other_op',
        'usec_per_read_op': 'usec_per_read_op',
        'usec_per_write_op': 'usec_per_write_op',
        'write_bytes_per_sec': 'write_bytes_per_sec',
        'writes_per_sec': 'writes_per_sec'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        bytes_per_op=None,  # type: int
        bytes_per_read=None,  # type: int
        bytes_per_write=None,  # type: int
        others_per_sec=None,  # type: int
        read_bytes_per_sec=None,  # type: int
        reads_per_sec=None,  # type: int
        time=None,  # type: int
        usec_per_other_op=None,  # type: int
        usec_per_read_op=None,  # type: int
        usec_per_write_op=None,  # type: int
        write_bytes_per_sec=None,  # type: int
        writes_per_sec=None,  # type: int
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A user-specified name. The name must be locally unique and can be changed.
            bytes_per_op (int): The average I/O size for both read and write (all) operations.
            bytes_per_read (int): The average I/O size per read, measured in bytes.
            bytes_per_write (int): The average I/O size per write, measured in bytes.
            others_per_sec (int): The number of other requests processed per second.
            read_bytes_per_sec (int): The number of bytes read per second.
            reads_per_sec (int): The number of read requests processed per second.
            time (int): The time when the sample performance data was taken. Measured in milliseconds since the UNIX epoch.
            usec_per_other_op (int): The average time it takes the array to process an I/O other request, measured in microseconds.
            usec_per_read_op (int): The average time it takes the array to process an I/O read request, measured in microseconds.
            usec_per_write_op (int): The average time it takes the array to process an I/O write request, measured in microseconds.
            write_bytes_per_sec (int): The number of bytes written per second.
            writes_per_sec (int): The number of write requests processed per second.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if bytes_per_op is not None:
            self.bytes_per_op = bytes_per_op
        if bytes_per_read is not None:
            self.bytes_per_read = bytes_per_read
        if bytes_per_write is not None:
            self.bytes_per_write = bytes_per_write
        if others_per_sec is not None:
            self.others_per_sec = others_per_sec
        if read_bytes_per_sec is not None:
            self.read_bytes_per_sec = read_bytes_per_sec
        if reads_per_sec is not None:
            self.reads_per_sec = reads_per_sec
        if time is not None:
            self.time = time
        if usec_per_other_op is not None:
            self.usec_per_other_op = usec_per_other_op
        if usec_per_read_op is not None:
            self.usec_per_read_op = usec_per_read_op
        if usec_per_write_op is not None:
            self.usec_per_write_op = usec_per_write_op
        if write_bytes_per_sec is not None:
            self.write_bytes_per_sec = write_bytes_per_sec
        if writes_per_sec is not None:
            self.writes_per_sec = writes_per_sec

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryPerformance`".format(key))
        if key == "bytes_per_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `bytes_per_op`, must be a value greater than or equal to `0`")
        if key == "bytes_per_read" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `bytes_per_read`, must be a value greater than or equal to `0`")
        if key == "bytes_per_write" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `bytes_per_write`, must be a value greater than or equal to `0`")
        if key == "others_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `others_per_sec`, must be a value greater than or equal to `0`")
        if key == "read_bytes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `read_bytes_per_sec`, must be a value greater than or equal to `0`")
        if key == "reads_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `reads_per_sec`, must be a value greater than or equal to `0`")
        if key == "usec_per_other_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `usec_per_other_op`, must be a value greater than or equal to `0`")
        if key == "usec_per_read_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `usec_per_read_op`, must be a value greater than or equal to `0`")
        if key == "usec_per_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `usec_per_write_op`, must be a value greater than or equal to `0`")
        if key == "write_bytes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `write_bytes_per_sec`, must be a value greater than or equal to `0`")
        if key == "writes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `writes_per_sec`, must be a value greater than or equal to `0`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryPerformance`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryPerformance`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryPerformance`".format(key))
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
        if issubclass(DirectoryPerformance, dict):
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
        if not isinstance(other, DirectoryPerformance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
