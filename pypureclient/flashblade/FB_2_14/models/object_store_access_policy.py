# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.14, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_14 import models

class ObjectStoreAccessPolicy(object):
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
        'enabled': 'bool',
        'is_local': 'bool',
        'location': 'FixedReference',
        'policy_type': 'str',
        'account': 'FixedReference',
        'arn': 'str',
        'created': 'int',
        'description': 'str',
        'rules': 'list[PolicyRuleObjectAccess]',
        'updated': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'enabled': 'enabled',
        'is_local': 'is_local',
        'location': 'location',
        'policy_type': 'policy_type',
        'account': 'account',
        'arn': 'arn',
        'created': 'created',
        'description': 'description',
        'rules': 'rules',
        'updated': 'updated'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        enabled=None,  # type: bool
        is_local=None,  # type: bool
        location=None,  # type: models.FixedReference
        policy_type=None,  # type: str
        account=None,  # type: models.FixedReference
        arn=None,  # type: str
        created=None,  # type: int
        description=None,  # type: str
        rules=None,  # type: List[models.PolicyRuleObjectAccess]
        updated=None,  # type: int
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            enabled (bool): If `true`, the policy is enabled. If not specified, defaults to `true`.
            is_local (bool): Whether the policy is defined on the local array.
            location (FixedReference): Reference to the array where the policy is defined.
            policy_type (str): Type of the policy. Valid values are `audit`, `bucket-access`, `cross-origin-resource-sharing`, `network-access`, `nfs`, `object-access`, `smb-client`, `smb-share`, and `snapshot`.
            account (FixedReference): Reference of the associated account. If the policy is not associated with an account, all fields in the reference possess `null` values.
            arn (str): Amazon Resource Name of the policy. Used when referencing the policy via S3 APIs.
            created (int): Creation timestamp of the object.
            description (str): A description of the policy, optionally specified when the policy is created. Cannot be modified for an existing policy.
            rules (list[PolicyRuleObjectAccess])
            updated (int): The last updated timestamp of the object.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if enabled is not None:
            self.enabled = enabled
        if is_local is not None:
            self.is_local = is_local
        if location is not None:
            self.location = location
        if policy_type is not None:
            self.policy_type = policy_type
        if account is not None:
            self.account = account
        if arn is not None:
            self.arn = arn
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if rules is not None:
            self.rules = rules
        if updated is not None:
            self.updated = updated

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ObjectStoreAccessPolicy`".format(key))
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
        if issubclass(ObjectStoreAccessPolicy, dict):
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
        if not isinstance(other, ObjectStoreAccessPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
