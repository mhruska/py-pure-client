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

class VirtualMachineVolumeSnapshot(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created': 'int',
        'destroyed': 'bool',
        'id': 'str',
        'name': 'str',
        'recover_context': 'FixedReference',
        'time_remaining': 'int',
        'vm_id': 'str',
        'vm_type': 'str',
        'vvol_name': 'str',
        'vvol_type': 'str'
    }

    attribute_map = {
        'created': 'created',
        'destroyed': 'destroyed',
        'id': 'id',
        'name': 'name',
        'recover_context': 'recover_context',
        'time_remaining': 'time_remaining',
        'vm_id': 'vm_id',
        'vm_type': 'vm_type',
        'vvol_name': 'vvol_name',
        'vvol_type': 'vvol_type'
    }

    required_args = {
    }

    def __init__(
        self,
        created=None,  # type: int
        destroyed=None,  # type: bool
        id=None,  # type: str
        name=None,  # type: str
        recover_context=None,  # type: models.FixedReference
        time_remaining=None,  # type: int
        vm_id=None,  # type: str
        vm_type=None,  # type: str
        vvol_name=None,  # type: str
        vvol_type=None,  # type: str
    ):
        """
        Keyword args:
            created (int): The virtual machine volume snapshot creation time measured in milliseconds since the UNIX epoch.
            destroyed (bool): Returns a value of `true` if the virtual machine volume snapshot has been destroyed and is pending eradication.
            id (str): A globally unique, system-generated ID. The ID cannot be modified.
            name (str): The name of the virtual machine volume snapshot.
            recover_context (FixedReference): A reference to any additional entities needed to recover this virtual machine.
            time_remaining (int): Specifies the amount of time left until the destroyed volume snapshot is permanently eradicated, measured in milliseconds. Once the `time_remaining` period has elapsed, the volume snapshot is permanently eradicated and can no longer be recovered.
            vm_id (str): The ID of the virtual machine, as assigned by the external system.
            vm_type (str): The type of virtual machine. The only valid value is `vvol`.
            vvol_name (str): The name of the virtual machine volume.
            vvol_type (str): The type of virtual machine volume. Values include `config` and `data`.
        """
        if created is not None:
            self.created = created
        if destroyed is not None:
            self.destroyed = destroyed
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if recover_context is not None:
            self.recover_context = recover_context
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if vm_id is not None:
            self.vm_id = vm_id
        if vm_type is not None:
            self.vm_type = vm_type
        if vvol_name is not None:
            self.vvol_name = vvol_name
        if vvol_type is not None:
            self.vvol_type = vvol_type

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VirtualMachineVolumeSnapshot`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VirtualMachineVolumeSnapshot`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VirtualMachineVolumeSnapshot`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VirtualMachineVolumeSnapshot`".format(key))
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
        if issubclass(VirtualMachineVolumeSnapshot, dict):
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
        if not isinstance(other, VirtualMachineVolumeSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
