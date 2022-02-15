import * as pulumi from "@pulumi/pulumi";
import * as checkly from "@pulumi/checkly";

if (!pulumi.runtime.isDryRun()) {
    const x = new checkly.Check("test", {
        name: "testCheck",
        activated: true,
        frequency: 10,
        type: "API",
    });

    export const y = x.groupId

}
