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
    public sealed class CheckAlertSettingsReminder
    {
        /// <summary>
        /// How many reminders to send out after the initial alert notification. Possible values are `0`, `1`, `2`, `3`, `4`, `5`, and `100000`
        /// </summary>
        public readonly int? Amount;
        /// <summary>
        /// . Possible values are `5`, `10`, `15`, and `30`. Defaults to `5`.
        /// </summary>
        public readonly int? Interval;

        [OutputConstructor]
        private CheckAlertSettingsReminder(
            int? amount,

            int? interval)
        {
            Amount = amount;
            Interval = interval;
        }
    }
}
