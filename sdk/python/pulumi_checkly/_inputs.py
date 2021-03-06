# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'CheckAlertChannelSubscriptionArgs',
    'CheckAlertSettingsArgs',
    'CheckAlertSettingsReminderArgs',
    'CheckAlertSettingsRunBasedEscalationArgs',
    'CheckAlertSettingsSslCertificateArgs',
    'CheckAlertSettingsTimeBasedEscalationArgs',
    'CheckRequestArgs',
    'CheckRequestAssertionArgs',
    'CheckRequestBasicAuthArgs',
]

@pulumi.input_type
class CheckAlertChannelSubscriptionArgs:
    def __init__(__self__, *,
                 activated: pulumi.Input[bool],
                 channel_id: pulumi.Input[int]):
        """
        :param pulumi.Input[bool] activated: Determines if the check is running or not. Possible values `true`, and `false`.
        """
        pulumi.set(__self__, "activated", activated)
        pulumi.set(__self__, "channel_id", channel_id)

    @property
    @pulumi.getter
    def activated(self) -> pulumi.Input[bool]:
        """
        Determines if the check is running or not. Possible values `true`, and `false`.
        """
        return pulumi.get(self, "activated")

    @activated.setter
    def activated(self, value: pulumi.Input[bool]):
        pulumi.set(self, "activated", value)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "channel_id")

    @channel_id.setter
    def channel_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "channel_id", value)


@pulumi.input_type
class CheckAlertSettingsArgs:
    def __init__(__self__, *,
                 escalation_type: Optional[pulumi.Input[str]] = None,
                 reminders: Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsReminderArgs']]]] = None,
                 run_based_escalations: Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsRunBasedEscalationArgs']]]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsSslCertificateArgs']]]] = None,
                 time_based_escalations: Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsTimeBasedEscalationArgs']]]] = None):
        """
        :param pulumi.Input[str] escalation_type: Determines what type of escalation to use. Possible values are `RUN_BASED` or `TIME_BASED`.
        :param pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsReminderArgs']]] reminders: . Possible arguments:
        :param pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsRunBasedEscalationArgs']]] run_based_escalations: . Possible arguments:
        :param pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsSslCertificateArgs']]] ssl_certificates: At what interval the reminders should be send.  Possible arguments:
        :param pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsTimeBasedEscalationArgs']]] time_based_escalations: . Possible arguments:
        """
        if escalation_type is not None:
            pulumi.set(__self__, "escalation_type", escalation_type)
        if reminders is not None:
            pulumi.set(__self__, "reminders", reminders)
        if run_based_escalations is not None:
            pulumi.set(__self__, "run_based_escalations", run_based_escalations)
        if ssl_certificates is not None:
            pulumi.set(__self__, "ssl_certificates", ssl_certificates)
        if time_based_escalations is not None:
            pulumi.set(__self__, "time_based_escalations", time_based_escalations)

    @property
    @pulumi.getter(name="escalationType")
    def escalation_type(self) -> Optional[pulumi.Input[str]]:
        """
        Determines what type of escalation to use. Possible values are `RUN_BASED` or `TIME_BASED`.
        """
        return pulumi.get(self, "escalation_type")

    @escalation_type.setter
    def escalation_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "escalation_type", value)

    @property
    @pulumi.getter
    def reminders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsReminderArgs']]]]:
        """
        . Possible arguments:
        """
        return pulumi.get(self, "reminders")

    @reminders.setter
    def reminders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsReminderArgs']]]]):
        pulumi.set(self, "reminders", value)

    @property
    @pulumi.getter(name="runBasedEscalations")
    def run_based_escalations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsRunBasedEscalationArgs']]]]:
        """
        . Possible arguments:
        """
        return pulumi.get(self, "run_based_escalations")

    @run_based_escalations.setter
    def run_based_escalations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsRunBasedEscalationArgs']]]]):
        pulumi.set(self, "run_based_escalations", value)

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsSslCertificateArgs']]]]:
        """
        At what interval the reminders should be send.  Possible arguments:
        """
        return pulumi.get(self, "ssl_certificates")

    @ssl_certificates.setter
    def ssl_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsSslCertificateArgs']]]]):
        pulumi.set(self, "ssl_certificates", value)

    @property
    @pulumi.getter(name="timeBasedEscalations")
    def time_based_escalations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsTimeBasedEscalationArgs']]]]:
        """
        . Possible arguments:
        """
        return pulumi.get(self, "time_based_escalations")

    @time_based_escalations.setter
    def time_based_escalations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CheckAlertSettingsTimeBasedEscalationArgs']]]]):
        pulumi.set(self, "time_based_escalations", value)


@pulumi.input_type
class CheckAlertSettingsReminderArgs:
    def __init__(__self__, *,
                 amount: Optional[pulumi.Input[int]] = None,
                 interval: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] amount: How many reminders to send out after the initial alert notification. Possible values are `0`, `1`, `2`, `3`, `4`, `5`, and `100000`
        :param pulumi.Input[int] interval: . Possible values are `5`, `10`, `15`, and `30`. Defaults to `5`.
        """
        if amount is not None:
            pulumi.set(__self__, "amount", amount)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)

    @property
    @pulumi.getter
    def amount(self) -> Optional[pulumi.Input[int]]:
        """
        How many reminders to send out after the initial alert notification. Possible values are `0`, `1`, `2`, `3`, `4`, `5`, and `100000`
        """
        return pulumi.get(self, "amount")

    @amount.setter
    def amount(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "amount", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        . Possible values are `5`, `10`, `15`, and `30`. Defaults to `5`.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)


@pulumi.input_type
class CheckAlertSettingsRunBasedEscalationArgs:
    def __init__(__self__, *,
                 failed_run_threshold: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] failed_run_threshold: After how many failed consecutive check runs an alert notification should be send. Possible values are between 1 and 5. Defaults to `1`.
        """
        if failed_run_threshold is not None:
            pulumi.set(__self__, "failed_run_threshold", failed_run_threshold)

    @property
    @pulumi.getter(name="failedRunThreshold")
    def failed_run_threshold(self) -> Optional[pulumi.Input[int]]:
        """
        After how many failed consecutive check runs an alert notification should be send. Possible values are between 1 and 5. Defaults to `1`.
        """
        return pulumi.get(self, "failed_run_threshold")

    @failed_run_threshold.setter
    def failed_run_threshold(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "failed_run_threshold", value)


@pulumi.input_type
class CheckAlertSettingsSslCertificateArgs:
    def __init__(__self__, *,
                 alert_threshold: Optional[pulumi.Input[int]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[int] alert_threshold: At what moment in time to start alerting on SSL certificates. Possible values `3`, `7`, `14`, `30`. Defaults to `3`.
        :param pulumi.Input[bool] enabled: Determines if alert notifications should be send for expiring SSL certificates. Possible values `true`, and `false`. Defaults to `true`.
        """
        if alert_threshold is not None:
            pulumi.set(__self__, "alert_threshold", alert_threshold)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter(name="alertThreshold")
    def alert_threshold(self) -> Optional[pulumi.Input[int]]:
        """
        At what moment in time to start alerting on SSL certificates. Possible values `3`, `7`, `14`, `30`. Defaults to `3`.
        """
        return pulumi.get(self, "alert_threshold")

    @alert_threshold.setter
    def alert_threshold(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "alert_threshold", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if alert notifications should be send for expiring SSL certificates. Possible values `true`, and `false`. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class CheckAlertSettingsTimeBasedEscalationArgs:
    def __init__(__self__, *,
                 minutes_failing_threshold: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] minutes_failing_threshold: After how many minutes after a check starts failing an alert should be send. Possible values are `5`, `10`, `15`, and `30`. Defaults to `5`.
        """
        if minutes_failing_threshold is not None:
            pulumi.set(__self__, "minutes_failing_threshold", minutes_failing_threshold)

    @property
    @pulumi.getter(name="minutesFailingThreshold")
    def minutes_failing_threshold(self) -> Optional[pulumi.Input[int]]:
        """
        After how many minutes after a check starts failing an alert should be send. Possible values are `5`, `10`, `15`, and `30`. Defaults to `5`.
        """
        return pulumi.get(self, "minutes_failing_threshold")

    @minutes_failing_threshold.setter
    def minutes_failing_threshold(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minutes_failing_threshold", value)


@pulumi.input_type
class CheckRequestArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str],
                 assertions: Optional[pulumi.Input[Sequence[pulumi.Input['CheckRequestAssertionArgs']]]] = None,
                 basic_auth: Optional[pulumi.Input['CheckRequestBasicAuthArgs']] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 body_type: Optional[pulumi.Input[str]] = None,
                 follow_redirects: Optional[pulumi.Input[bool]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 method: Optional[pulumi.Input[str]] = None,
                 query_parameters: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 skip_ssl: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] url: .
        :param pulumi.Input[Sequence[pulumi.Input['CheckRequestAssertionArgs']]] assertions: A request can have multiple assetions. Assertion has the following arguments:
        :param pulumi.Input['CheckRequestBasicAuthArgs'] basic_auth: A request might have one basic_auth config. basic_auth has two arguments:
        :param pulumi.Input[str] body_type: Possible values `NONE`, `JSON`, `FORM`, `RAW`, and `GRAPHQL`.
        :param pulumi.Input[bool] follow_redirects: .
        :param pulumi.Input[Mapping[str, Any]] headers: .
        :param pulumi.Input[str] method: The HTTP method to use for this API check. Possible values are `GET`, `POST`, `PUT`, `HEAD`, `DELETE`, `PATCH`. Defaults to `GET`.
        :param pulumi.Input[Mapping[str, Any]] query_parameters: .
        :param pulumi.Input[bool] skip_ssl: .
        """
        pulumi.set(__self__, "url", url)
        if assertions is not None:
            pulumi.set(__self__, "assertions", assertions)
        if basic_auth is not None:
            pulumi.set(__self__, "basic_auth", basic_auth)
        if body is not None:
            pulumi.set(__self__, "body", body)
        if body_type is not None:
            pulumi.set(__self__, "body_type", body_type)
        if follow_redirects is not None:
            pulumi.set(__self__, "follow_redirects", follow_redirects)
        if headers is not None:
            pulumi.set(__self__, "headers", headers)
        if method is not None:
            pulumi.set(__self__, "method", method)
        if query_parameters is not None:
            pulumi.set(__self__, "query_parameters", query_parameters)
        if skip_ssl is not None:
            pulumi.set(__self__, "skip_ssl", skip_ssl)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        .
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def assertions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CheckRequestAssertionArgs']]]]:
        """
        A request can have multiple assetions. Assertion has the following arguments:
        """
        return pulumi.get(self, "assertions")

    @assertions.setter
    def assertions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CheckRequestAssertionArgs']]]]):
        pulumi.set(self, "assertions", value)

    @property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> Optional[pulumi.Input['CheckRequestBasicAuthArgs']]:
        """
        A request might have one basic_auth config. basic_auth has two arguments:
        """
        return pulumi.get(self, "basic_auth")

    @basic_auth.setter
    def basic_auth(self, value: Optional[pulumi.Input['CheckRequestBasicAuthArgs']]):
        pulumi.set(self, "basic_auth", value)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="bodyType")
    def body_type(self) -> Optional[pulumi.Input[str]]:
        """
        Possible values `NONE`, `JSON`, `FORM`, `RAW`, and `GRAPHQL`.
        """
        return pulumi.get(self, "body_type")

    @body_type.setter
    def body_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body_type", value)

    @property
    @pulumi.getter(name="followRedirects")
    def follow_redirects(self) -> Optional[pulumi.Input[bool]]:
        """
        .
        """
        return pulumi.get(self, "follow_redirects")

    @follow_redirects.setter
    def follow_redirects(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "follow_redirects", value)

    @property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        .
        """
        return pulumi.get(self, "headers")

    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "headers", value)

    @property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP method to use for this API check. Possible values are `GET`, `POST`, `PUT`, `HEAD`, `DELETE`, `PATCH`. Defaults to `GET`.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        .
        """
        return pulumi.get(self, "query_parameters")

    @query_parameters.setter
    def query_parameters(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "query_parameters", value)

    @property
    @pulumi.getter(name="skipSsl")
    def skip_ssl(self) -> Optional[pulumi.Input[bool]]:
        """
        .
        """
        return pulumi.get(self, "skip_ssl")

    @skip_ssl.setter
    def skip_ssl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_ssl", value)


@pulumi.input_type
class CheckRequestAssertionArgs:
    def __init__(__self__, *,
                 comparison: pulumi.Input[str],
                 source: pulumi.Input[str],
                 property: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] comparison: Possible values `EQUALS`, `NOT_EQUALS`, `HAS_KEY`, `NOT_HAS_KEY`, `HAS_VALUE`, `NOT_HAS_VALUE`, `IS_EMPTY`, `NOT_EMPTY`, `GREATER_THAN`, `LESS_THAN`, `CONTAINS`, `NOT_CONTAINS`, `IS_NULL`, and `NOT_NULL`.
        :param pulumi.Input[str] source: Possible values `STATUS_CODE`, `JSON_BODY`, `HEADERS`, `TEXT_BODY`, and `RESPONSE_TIME`.
        :param pulumi.Input[str] property: .
        :param pulumi.Input[str] target: .
        """
        pulumi.set(__self__, "comparison", comparison)
        pulumi.set(__self__, "source", source)
        if property is not None:
            pulumi.set(__self__, "property", property)
        if target is not None:
            pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[str]:
        """
        Possible values `EQUALS`, `NOT_EQUALS`, `HAS_KEY`, `NOT_HAS_KEY`, `HAS_VALUE`, `NOT_HAS_VALUE`, `IS_EMPTY`, `NOT_EMPTY`, `GREATER_THAN`, `LESS_THAN`, `CONTAINS`, `NOT_CONTAINS`, `IS_NULL`, and `NOT_NULL`.
        """
        return pulumi.get(self, "comparison")

    @comparison.setter
    def comparison(self, value: pulumi.Input[str]):
        pulumi.set(self, "comparison", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        """
        Possible values `STATUS_CODE`, `JSON_BODY`, `HEADERS`, `TEXT_BODY`, and `RESPONSE_TIME`.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        .
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def property(self) -> Optional[pulumi.Input[str]]:
        """
        .
        """
        return pulumi.get(self, "property")

    @property.setter
    def property(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property", value)


@pulumi.input_type
class CheckRequestBasicAuthArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


