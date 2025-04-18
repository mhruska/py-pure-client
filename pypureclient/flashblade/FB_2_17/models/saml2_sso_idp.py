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

class Saml2SsoIdp(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'verification_certificate': 'ReferenceWritable',
        'sign_request_enabled': 'bool',
        'metadata_url': 'str',
        'encrypt_assertion_enabled': 'bool',
        'metadata_url_ca_certificate': 'ReferenceWritable',
        'metadata_url_ca_certificate_group': 'ReferenceWritable',
        'entity_id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'verification_certificate': 'verification_certificate',
        'sign_request_enabled': 'sign_request_enabled',
        'metadata_url': 'metadata_url',
        'encrypt_assertion_enabled': 'encrypt_assertion_enabled',
        'metadata_url_ca_certificate': 'metadata_url_ca_certificate',
        'metadata_url_ca_certificate_group': 'metadata_url_ca_certificate_group',
        'entity_id': 'entity_id',
        'url': 'url'
    }

    required_args = {
    }

    def __init__(
        self,
        verification_certificate=None,  # type: models.ReferenceWritable
        sign_request_enabled=None,  # type: bool
        metadata_url=None,  # type: str
        encrypt_assertion_enabled=None,  # type: bool
        metadata_url_ca_certificate=None,  # type: models.ReferenceWritable
        metadata_url_ca_certificate_group=None,  # type: models.ReferenceWritable
        entity_id=None,  # type: str
        url=None,  # type: str
    ):
        """
        Keyword args:
            verification_certificate (ReferenceWritable): The certificate used by the service provider to verify the SAML response signature from the identity provider. The credential is managed by the `certificates` endpoint and `purecert` CLI commands. 
            sign_request_enabled (bool): If set to `true`, SAML requests will be signed by the service provider.
            metadata_url (str): The URL of the identity provider metadata.
            encrypt_assertion_enabled (bool): If set to `true`, SAML assertions will be encrypted by the identity provider.
            metadata_url_ca_certificate (ReferenceWritable): CA certificate used to validate the authenticity of the configured Identity Provider server. 
            metadata_url_ca_certificate_group (ReferenceWritable): A certificate group containing CA certificates that can be used to validate the authenticity of the configured Identity Provider server. 
            entity_id (str): A globally unique name for the identity provider.
            url (str): The URL of the identity provider.
        """
        if verification_certificate is not None:
            self.verification_certificate = verification_certificate
        if sign_request_enabled is not None:
            self.sign_request_enabled = sign_request_enabled
        if metadata_url is not None:
            self.metadata_url = metadata_url
        if encrypt_assertion_enabled is not None:
            self.encrypt_assertion_enabled = encrypt_assertion_enabled
        if metadata_url_ca_certificate is not None:
            self.metadata_url_ca_certificate = metadata_url_ca_certificate
        if metadata_url_ca_certificate_group is not None:
            self.metadata_url_ca_certificate_group = metadata_url_ca_certificate_group
        if entity_id is not None:
            self.entity_id = entity_id
        if url is not None:
            self.url = url

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Saml2SsoIdp`".format(key))
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
        if issubclass(Saml2SsoIdp, dict):
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
        if not isinstance(other, Saml2SsoIdp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
