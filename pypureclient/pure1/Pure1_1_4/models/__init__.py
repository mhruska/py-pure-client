# coding: utf-8

from __future__ import absolute_import


class ReferenceType(object):
    """Class just for type annotations.

    It's used for reference arg on api function. This allows user to pass collections of Model objects
    to the method without transforming them to ids or names.

    Should be Protocol type when the typing module will get support of it.
    """
    def __init__(self):
        self.id = ''
        self.name = ''


def quoteString(s):
    r"""Quote string according to
    https://wiki.purestorage.com/display/UXReviewers/Filtering

    >>> quote("a")
    "'a'"
    >>> quote("a\\b")
    "'a\\\\b'"
    >>> quote("a\\b")
    "'a\\\\b'"
    >>> quote("a'b")
    "'a\\'b'"
    >>> quote(None)
    None
    """
    if s is None:
        return None
    quoted = str(s).replace("\\", "\\\\").replace("'", "\\'")
    return "'{}'".format(quoted)


def quoteStrings(s):
    if s is None:
        return None
    return [quoteString(x) for x in s]


# import models into model package
from .alerts_response import AlertsResponse
from .array_response import ArrayResponse
from .asset_org import AssetOrg
from .asset_space import AssetSpace
from .asset_upgrade_details import AssetUpgradeDetails
from .audits_response import AuditsResponse
from .base_address import BaseAddress
from .blade_response import BladeResponse
from .bucket_replica_link_response import BucketReplicaLinkResponse
from .bucket_response import BucketResponse
from .controller_response import ControllerResponse
from .current_metric import CurrentMetric
from .default_details import DefaultDetails
from .directory_response import DirectoryResponse
from .drive_response import DriveResponse
from .error import Error
from .error_errors import ErrorErrors
from .error_no_context import ErrorNoContext
from .evergreen_forever_and_foundation_details import EvergreenForeverAndFoundationDetails
from .file_system_replica_link_response import FileSystemReplicaLinkResponse
from .file_system_response import FileSystemResponse
from .file_system_snapshot_response import FileSystemSnapshotResponse
from .fixed_reference import FixedReference
from .geolocation import Geolocation
from .hardware_connector_response import HardwareConnectorResponse
from .hardware_response import HardwareResponse
from .http import Http
from .inline_response400 import InlineResponse400
from .inline_response401 import InlineResponse401
from .install_address import InstallAddress
from .invoice import Invoice
from .invoice_line import InvoiceLine
from .invoice_line_component import InvoiceLineComponent
from .invoice_response import InvoiceResponse
from .marketplace_partner import MarketplacePartner
from .metric_availability import MetricAvailability
from .metric_history_response import MetricHistoryResponse
from .metric_response import MetricResponse
from .network_interface_response import NetworkInterfaceResponse
from .nfs import Nfs
from .oauth_token_response import OauthTokenResponse
from .object_store_account_response import ObjectStoreAccountResponse
from .pod_replica_link_response import PodReplicaLinkResponse
from .pod_response import PodResponse
from .policy_members_response import PolicyMembersResponse
from .policy_response import PolicyResponse
from .policy_rule import PolicyRule
from .port_response import PortResponse
from .smb import Smb
from .subscription_asset_array import SubscriptionAssetArray
from .subscription_asset_array_advanced_space import SubscriptionAssetArrayAdvancedSpace
from .subscription_asset_response import SubscriptionAssetResponse
from .subscription_license_add_on_sla import SubscriptionLicenseAddOnSla
from .subscription_license_response import SubscriptionLicenseResponse
from .subscription_response import SubscriptionResponse
from .support_contract import SupportContract
from .support_contract_response import SupportContractResponse
from .sustainability_array_response import SustainabilityArrayResponse
from .sustainability_insight_array_response import SustainabilityInsightArrayResponse
from .tag import Tag
from .tag_batch_required import TagBatchRequired
from .tag_put import TagPut
from .tag_response import TagResponse
from .target_response import TargetResponse
from .tax import Tax
from .time_interval import TimeInterval
from .volume_response import VolumeResponse
from .volume_snapshot_response import VolumeSnapshotResponse
from .alerts_get_response import AlertsGetResponse
from .array_get_response import ArrayGetResponse
from .asset_address import AssetAddress
from .asset_space_total_used_ratio import AssetSpaceTotalUsedRatio
from .audits_get_response import AuditsGetResponse
from .blade_array_status import BladeArrayStatus
from .blade_get_response import BladeGetResponse
from .bucket_get_response import BucketGetResponse
from .bucket_replica_link_get_response import BucketReplicaLinkGetResponse
from .controller_get_response import ControllerGetResponse
from .directory_get_response import DirectoryGetResponse
from .drive_array_status import DriveArrayStatus
from .drive_get_response import DriveGetResponse
from .file_system_get_response import FileSystemGetResponse
from .file_system_replica_link_get_response import FileSystemReplicaLinkGetResponse
from .file_system_snapshot_get_response import FileSystemSnapshotGetResponse
from .fixed_reference_fqdn import FixedReferenceFqdn
from .hardware_connector_get_response import HardwareConnectorGetResponse
from .hardware_get_response import HardwareGetResponse
from .invoice_get_response import InvoiceGetResponse
from .metric_get_response import MetricGetResponse
from .metric_history_get_response import MetricHistoryGetResponse
from .network_interface_get_response import NetworkInterfaceGetResponse
from .object_store_account_get_response import ObjectStoreAccountGetResponse
from .pod_get_response import PodGetResponse
from .pod_replica_link_get_response import PodReplicaLinkGetResponse
from .policy_get_response import PolicyGetResponse
from .policy_member import PolicyMember
from .policy_members_get_response import PolicyMembersGetResponse
from .port_get_response import PortGetResponse
from .resource import Resource
from .resource_no_name import ResourceNoName
from .resource_with_location import ResourceWithLocation
from .resource_with_locations import ResourceWithLocations
from .subscription_asset_get_response import SubscriptionAssetGetResponse
from .subscription_get_response import SubscriptionGetResponse
from .subscription_license_get_response import SubscriptionLicenseGetResponse
from .subscription_license_pre_ratio import SubscriptionLicensePreRatio
from .support_contract_get_response import SupportContractGetResponse
from .sustainability_array_get_response import SustainabilityArrayGetResponse
from .sustainability_assessment import SustainabilityAssessment
from .sustainability_insight_array import SustainabilityInsightArray
from .sustainability_insight_array_get_response import SustainabilityInsightArrayGetResponse
from .tag_get_response import TagGetResponse
from .target_get_response import TargetGetResponse
from .volume_get_response import VolumeGetResponse
from .volume_snapshot_get_response import VolumeSnapshotGetResponse
from .array import Array
from .blade import Blade
from .drive import Drive
from .license_resource_reference import LicenseResourceReference
from .metric import Metric
from .metric_history import MetricHistory
from .replica_link import ReplicaLink
from .subscription import Subscription
from .subscription_asset import SubscriptionAsset
from .subscription_license import SubscriptionLicense
from .sustainability_array import SustainabilityArray
from .alert import Alert
from .audit import Audit
from .bucket import Bucket
from .bucket_replica_link import BucketReplicaLink
from .controller import Controller
from .directory import Directory
from .file_system import FileSystem
from .file_system_replica_link import FileSystemReplicaLink
from .file_system_snapshot import FileSystemSnapshot
from .hardware import Hardware
from .hardware_connector import HardwareConnector
from .network_interface import NetworkInterface
from .object_store_account import ObjectStoreAccount
from .pod import Pod
from .pod_replica_link import PodReplicaLink
from .policy import Policy
from .port import Port
from .target import Target
from .volume import Volume
from .volume_snapshot import VolumeSnapshot
