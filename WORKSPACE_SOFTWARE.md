# Workspace software build specification

Maintainer specification for CD16204; learners do not install software.
The target is Debian 12 Linux x86_64 with Python 3.13.15 in
`/opt/conda/envs/ml`. Use the complete pinned `requirements.txt` at image build
time. It includes Flask/WSGI, numerical/ML libraries, headless plotting and local
HTTP dependencies. Preserve these versions when assembling the image; do not
upgrade unrelated base-image packages. The observed older Workspace package set
is not the build specification.

## Image build and verification

Install requirements into `ml` during maintainer image construction, then run:

```sh
/opt/conda/envs/ml/bin/python -m pip check
/opt/conda/envs/ml/bin/python scripts/software_smoke.py
```

Run the probe with network egress disabled but loopback enabled. It imports the
required libraries, creates a temporary headless PNG, and calls a temporary Flask
health endpoint over real loopback HTTP. It neither imports unfinished learner
modules nor trains a model. Temporary files and the server are cleaned up.
The probe is a software check, not evidence that the learner project is complete.

Required OS capabilities: bash, writable `/workspace`, `crontab`, a working
Supercronic-compatible scheduler, `/usr/bin/flock`, and loopback TCP. The image
must start its scheduler and reload installed jobs correctly without learner
sudo/service installation. Persist the schedule under `/workspace/.crontab`.
Do not install a second cron daemon alongside Supercronic. Verify registration,
reload, a real ten-minute invocation and restart behavior in #31/#40.
The current crontab wrapper calls `/etc/init.d/cron` despite running Supercronic;
that platform gap remains to be fixed/verified before declaring the image ready.

Set `/workspace/.conda_env` to `ml` and VS Code's
`python.defaultInterpreterPath` to `/opt/conda/envs/ml/bin/python`.
Bundle the correct unfinished starter and data separately in #32.

## Learner and optional environments

Learners use the preinstalled `ml` environment from
`/workspace/cd16204-starter-code`; no pip/Conda install or virtual environment
is required. No registry query is needed at runtime. #33 supplies the dated
offline dependency reference, separately from this build lock.

PDF/SQL extensions are optional and excluded from core requirements. This build
does not promise reportlab, a MySQL connector or a database server. #36 must omit
unsupported PDF/MySQL installation exercises; retain them only if #31 explicitly
adds and validates their complete software/service stack at image build time.
They cannot be conditions for passing the core project.

The devcontainer is an **optional maintainer/reviewer** environment, not the
Udacity Workspace image or the learner setup. It installs requirements at
container creation. Local reviewers may instead create a Python 3.13 virtual
environment and install requirements there. Those instructions do not authorize
requiring installation inside the learner Workspace.

## Verification coverage

Clean installations and the software probe passed on macOS ARM64 and on the
actual CD16204 v1.3 Workspace: Debian 12, Linux x86_64/glibc 2.36,
Python 3.13.15. The Linux check installed all 32 pins into an isolated temporary
virtual environment using the Workspace's `ml` interpreter, then passed pip's
dependency check, imports, headless PNG generation and real loopback HTTP.
The existing `ml` environment and project files were not modified.
Linux binary-only dependency resolution also passed separately.

This establishes package runtime compatibility with the observed Workspace base,
not completed image provisioning. The optional devcontainer build, scheduler
registration/reload/restart, fresh reset and egress-disabled execution remain
unverified and belong to #31/#39/#40. Temporary maintainer installation is a
verification technique, not a learner setup instruction.
