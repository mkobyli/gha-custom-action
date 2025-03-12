import * as core from '@actions/core';
import github from '@actions/github';
import exec from '@actions/exec';

Object.assign(global, core);

function run() {
    core.notice('Hello from my custom js action');
}

run();
