// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Checkly.Outputs
{

    [OutputType]
    public sealed class CheckAlertSettings
    {
        /// <summary>
        /// Determines what type of escalation to use. Possible values are `RUN_BASED` or `TIME_BASED`.
        /// </summary>
        public readonly string? EscalationType;
        /// <summary>
        /// . Possible arguments:
        /// </summary>
        public readonly ImmutableArray<Outputs.CheckAlertSettingsReminder> Reminders;
        /// <summary>
        /// . Possible arguments:
        /// </summary>
        public readonly ImmutableArray<Outputs.CheckAlertSettingsRunBasedEscalation> RunBasedEscalations;
        /// <summary>
        /// At what interval the reminders should be send.  Possible arguments:
        /// </summary>
        public readonly ImmutableArray<Outputs.CheckAlertSettingsSslCertificate> SslCertificates;
        /// <summary>
        /// . Possible arguments:
        /// </summary>
        public readonly ImmutableArray<Outputs.CheckAlertSettingsTimeBasedEscalation> TimeBasedEscalations;

        [OutputConstructor]
        private CheckAlertSettings(
            string? escalationType,

            ImmutableArray<Outputs.CheckAlertSettingsReminder> reminders,

            ImmutableArray<Outputs.CheckAlertSettingsRunBasedEscalation> runBasedEscalations,

            ImmutableArray<Outputs.CheckAlertSettingsSslCertificate> sslCertificates,

            ImmutableArray<Outputs.CheckAlertSettingsTimeBasedEscalation> timeBasedEscalations)
        {
            EscalationType = escalationType;
            Reminders = reminders;
            RunBasedEscalations = runBasedEscalations;
            SslCertificates = sslCertificates;
            TimeBasedEscalations = timeBasedEscalations;
        }
    }
}
