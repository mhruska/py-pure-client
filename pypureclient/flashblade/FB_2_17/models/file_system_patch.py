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

class FileSystemPatch(object):
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
        'promotion_status': 'str',
        'storage_class': 'StorageClassInfo',
        'created': 'int',
        'qos_policy': 'Reference',
        'smb': 'Smb',
        'source': 'FixedLocationReference',
        'multi_protocol': 'MultiProtocol',
        'fast_remove_directory_enabled': 'bool',
        'writable': 'bool',
        'time_remaining': 'int',
        'destroyed': 'bool',
        'hard_limit_enabled': 'bool',
        'provisioned': 'int',
        'requested_promotion_state': 'str',
        'default_user_quota': 'int',
        'group_ownership': 'str',
        'http': 'Http',
        'nfs': 'NfsPatch',
        'default_group_quota': 'int',
        'snapshot_directory_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'promotion_status': 'promotion_status',
        'storage_class': 'storage_class',
        'created': 'created',
        'qos_policy': 'qos_policy',
        'smb': 'smb',
        'source': 'source',
        'multi_protocol': 'multi_protocol',
        'fast_remove_directory_enabled': 'fast_remove_directory_enabled',
        'writable': 'writable',
        'time_remaining': 'time_remaining',
        'destroyed': 'destroyed',
        'hard_limit_enabled': 'hard_limit_enabled',
        'provisioned': 'provisioned',
        'requested_promotion_state': 'requested_promotion_state',
        'default_user_quota': 'default_user_quota',
        'group_ownership': 'group_ownership',
        'http': 'http',
        'nfs': 'nfs',
        'default_group_quota': 'default_group_quota',
        'snapshot_directory_enabled': 'snapshot_directory_enabled'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        promotion_status=None,  # type: str
        storage_class=None,  # type: models.StorageClassInfo
        created=None,  # type: int
        qos_policy=None,  # type: models.Reference
        smb=None,  # type: models.Smb
        source=None,  # type: models.FixedLocationReference
        multi_protocol=None,  # type: models.MultiProtocol
        fast_remove_directory_enabled=None,  # type: bool
        writable=None,  # type: bool
        time_remaining=None,  # type: int
        destroyed=None,  # type: bool
        hard_limit_enabled=None,  # type: bool
        provisioned=None,  # type: int
        requested_promotion_state=None,  # type: str
        default_user_quota=None,  # type: int
        group_ownership=None,  # type: str
        http=None,  # type: models.Http
        nfs=None,  # type: models.NfsPatch
        default_group_quota=None,  # type: int
        snapshot_directory_enabled=None,  # type: bool
    ):
        """
        Keyword args:
            name (str): A name chosen by the user. Can be changed. Must be locally unique. 
            id (str): A non-modifiable, globally unique ID chosen by the system. 
            promotion_status (str): Possible values are `promoted` and `demoted`. The current status of the file system with respect to replication. Changes via `requested_promotion_state`. The default for new file systems is `promoted`. 
            storage_class (StorageClassInfo)
            created (int): Creation timestamp of the file system.
            qos_policy (Reference): The QoS policy for the File System defines the performance controls that can be applied to the aggregate performance of all the clients accessing the file system.  If no policy is configured for a file system, then no performance controls are applied to it. Use \"\" to clear an attached policy. 
            smb (Smb): SMB configuration.
            source (FixedLocationReference): A reference to the source file system.
            multi_protocol (MultiProtocol): Multi-protocol configuration.
            fast_remove_directory_enabled (bool): If set to `true`, the file system, when mounted, will contain a directory that can be used for fast removal of other directories. Directories can be moved into the fast remove directory in order to have them deleted, and their space freed, more quickly than a normal removal operation. 
            writable (bool): Whether the file system is writable or not. If `false`, this overrides any protocol or file permission settings and prevents changes. If `true`, then the protocol and file permission settings are evaluated. If not specified, defaults to `true`. Modifiable. 
            time_remaining (int): Time in milliseconds before the file system is eradicated. `null` if not destroyed. 
            destroyed (bool): Returns a value of `true` if the file system has been destroyed and is pending eradication. The file system cannot be modified while it is in the destroyed state.  The `time_remaining` value displays the amount of time left until the destroyed file system is permanently eradicated. Once eradication has begun, the file system can no  longer be recovered. Before the `time_remaining` period has elapsed, the destroyed file system can be recovered through the PATCH method by setting `destroyed=false`. 
            hard_limit_enabled (bool): If set to `true`, the file system's size, as defined by `provisioned`, is used as a hard limit quota. 
            provisioned (int): The provisioned size of the file system, displayed in bytes. If set to an empty string (`\"\"`), the file system is unlimited in size. 
            requested_promotion_state (str): Possible values are `promoted` and `demoted`. The `demoted` state is used for replication targets and is only allowed to be set if the file system is in a replica-link relationship. The additional query param `discard-non-snapshotted-data` must be set to `true` when demoting a file system. The default for new file systems is `promoted`. 
            default_user_quota (int): The default space quota for a user writing to this file system.
            group_ownership (str): The group ownership for new files and directories in a file system. Possible values are `creator` and `parent-directory`. If `creator` is selected, the owning group of new files and directories is the primary group of the user who creates them. If `parent-directory` is selected, the owning group is the parent directory group.  Note: Existing files and directories are unaffected by this change. 
            http (Http): HTTP configuration.
            nfs (NfsPatch): NFS configuration.
            default_group_quota (int): The default space quota for a group writing to this file system.
            snapshot_directory_enabled (bool): If set to `true`, a hidden .snapshot directory will be present in each directory of the file system when it is mounted. The .snapshot directory allows clients read access to the contents of the snapshots that have been taken of a directory. If set to `false`, the .snapshot directory will not be present in any directories within a mounted file system. 
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if promotion_status is not None:
            self.promotion_status = promotion_status
        if storage_class is not None:
            self.storage_class = storage_class
        if created is not None:
            self.created = created
        if qos_policy is not None:
            self.qos_policy = qos_policy
        if smb is not None:
            self.smb = smb
        if source is not None:
            self.source = source
        if multi_protocol is not None:
            self.multi_protocol = multi_protocol
        if fast_remove_directory_enabled is not None:
            self.fast_remove_directory_enabled = fast_remove_directory_enabled
        if writable is not None:
            self.writable = writable
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if destroyed is not None:
            self.destroyed = destroyed
        if hard_limit_enabled is not None:
            self.hard_limit_enabled = hard_limit_enabled
        if provisioned is not None:
            self.provisioned = provisioned
        if requested_promotion_state is not None:
            self.requested_promotion_state = requested_promotion_state
        if default_user_quota is not None:
            self.default_user_quota = default_user_quota
        if group_ownership is not None:
            self.group_ownership = group_ownership
        if http is not None:
            self.http = http
        if nfs is not None:
            self.nfs = nfs
        if default_group_quota is not None:
            self.default_group_quota = default_group_quota
        if snapshot_directory_enabled is not None:
            self.snapshot_directory_enabled = snapshot_directory_enabled

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FileSystemPatch`".format(key))
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
        if issubclass(FileSystemPatch, dict):
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
        if not isinstance(other, FileSystemPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
