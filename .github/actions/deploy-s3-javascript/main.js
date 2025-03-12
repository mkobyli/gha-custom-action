const core = require('@actions/core');
const github = require('@actions/github');
const exec = require('@actions/exec');

function run() {
    core.notice('Hello from my custom js action');

    const bucket = core.getInput('bucket', {required: true})
    const bucketRegion = core.getInput('bucket-region', {required: true})
    const distFolder = core.getInput('dist-folder', {required: true})

    const ctxSha = github.context.sha
    exec.exec(`echo sha ${ctxSha}`)

    const s3Uri = `s3://${bucket}`
    exec.exec(`echo aws ${distFolder} ${s3Uri} --region ${bucketRegion}`)
}

run();
