// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func GetAccountId(ctx *pulumi.Context) string {
	return config.Get(ctx, "checkly:accountId")
}
func GetApiKey(ctx *pulumi.Context) string {
	return config.Get(ctx, "checkly:apiKey")
}
func GetApiUrl(ctx *pulumi.Context) string {
	return config.Get(ctx, "checkly:apiUrl")
}
