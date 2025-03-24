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

class LogsAsync(object):
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
        'available_files': 'list[FileInfo]',
        'start_time': 'int',
        'end_time': 'int',
        'processing': 'bool',
        'progress': 'float',
        'hardware_components': 'list[FixedReference]',
        'last_request_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'available_files': 'available_files',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'processing': 'processing',
        'progress': 'progress',
        'hardware_components': 'hardware_components',
        'last_request_time': 'last_request_time'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        available_files=None,  # type: List[models.FileInfo]
        start_time=None,  # type: int
        end_time=None,  # type: int
        processing=None,  # type: bool
        progress=None,  # type: float
        hardware_components=None,  # type: List[models.FixedReference]
        last_request_time=None,  # type: int
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system. 
            available_files (list[FileInfo]): All of the available files ready for download. 
            start_time (int): When the time window starts (in milliseconds since epoch). start_time and end_time determine the number of hours for which the logs are prepared for. At most 6 hours of logs can be prepared in one request. start_time and end_time are truncated to hour boundaries. 
            end_time (int): When the time window ends (in milliseconds since epoch). start_time and end_time determine the number of hours for which the logs are prepared for. At most 6 hours of logs can be prepared in one request. start_time and end_time are truncated to hour boundaries. 
            processing (bool): Returns a value of `true` if the logs are being prepared. 
            progress (float): A representation of log preparation progress. Ranges from 0 to 1.0. 
            hardware_components (list[FixedReference]): All of the hardware components for which logs are being processed. 
            last_request_time (int): The last time log preparation was requested (in milliseconds since epoch). 
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if available_files is not None:
            self.available_files = available_files
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if processing is not None:
            self.processing = processing
        if progress is not None:
            self.progress = progress
        if hardware_components is not None:
            self.hardware_components = hardware_components
        if last_request_time is not None:
            self.last_request_time = last_request_time

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LogsAsync`".format(key))
        if key == "start_time" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `start_time`, must be a value greater than or equal to `0`")
        if key == "end_time" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `end_time`, must be a value greater than or equal to `0`")
        if key == "last_request_time" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `last_request_time`, must be a value greater than or equal to `0`")
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
        if issubclass(LogsAsync, dict):
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
        if not isinstance(other, LogsAsync):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
