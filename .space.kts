container("openjdk:11") {
    kotlinScript { api ->
        api.space().projects.automation.deployments.start(
            project = api.projectIdentifier(),
            targetIdentifier = TargetIdentifier.Key("space-korea-ac"),
            version = "1.0.0",
            // automatically update deployment status based on a status of a job
            syncWithAutomationJob = true
        )
    }
}