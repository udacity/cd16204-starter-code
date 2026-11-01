# Workspace software build specification

Maintainer runtime specification for CD16204; learners do not install software.
The verified baseline is Debian 12 Linux x86_64 with Python 3.13.15 in
`/opt/conda/envs/ml`. The shared environment's existing versions are retained.
The project dependency snapshot covers Flask/WSGI, numerical/ML libraries,
headless plotting and local HTTP without changing the shared image.

## Preserve the existing shared image

The user selected the existing shared `ml` versions because CD16201 and CD16209
also use this environment. `requirements.txt` records the 32 project-related
distributions observed on 2026-11-01, not every package in the shared image.
Do not upgrade or downgrade shared packages to the superseded #30/#42 pins.
No image modification or additional core package installation is needed for the
observed environment: its dependency check and import/plot/HTTP probe passed.
Only a missing required package or a reproduced defect should trigger a minimal
change request to the separate image maintainer.

Run these read-only software checks in the existing environment:

```sh
/opt/conda/envs/ml/bin/python -m pip check
/opt/conda/envs/ml/bin/python scripts/software_smoke.py
```

The probe imports required libraries, creates a temporary headless PNG, and
calls a temporary Flask health endpoint over real loopback HTTP. It neither
imports unfinished learner modules nor trains a model. Temporary files and the
server are cleaned up. It is a software check, not project-completion evidence.
No learner package installation, venv creation or external account is needed.

Required OS capabilities: bash, writable `/workspace`, `crontab`, a working
Supercronic-compatible scheduler, `/usr/bin/flock`, and loopback TCP. The image
must start its scheduler and reload installed jobs correctly without learner
sudo/service installation. Persist the schedule under `/workspace/.crontab`.
Do not install a second cron daemon alongside Supercronic. Verify registration,
reload, a real ten-minute invocation and restart behavior in #31/#40.
The Workspace provides `/etc/init.d/cron` as a per-user Supercronic
compatibility script. The crontab wrapper calls that script to reload jobs; this
is not evidence of a missing Debian cron daemon. A temporary every-minute
maintainer date job was registered through `crontab`, executed successfully and
removed by restoring the original crontab bytes. This checks registration, reload
and execution; it does not prove ten-minute project execution or restart behavior.

The existing `/workspace/.conda_env` selects `ml`, and VS Code's
`python.defaultInterpreterPath` is `/opt/conda/envs/ml/bin/python`. A new
terminal and the editor's Run Python File both executed with that interpreter
without selecting a different environment or changing settings.
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

The unchanged preinstalled `ml` environment passed `python -m pip check` and the
exact software probe on Debian 12 Linux x86_64/glibc 2.36, Python 3.13.15.
Required imports, headless PNG generation and real loopback HTTP passed.
`sys.executable`, `sys.prefix` and `sys.base_prefix` all identify the existing
`/opt/conda/envs/ml` environment, not the temporary #30 venv. The 32 selected
distribution versions were identical before and after the checks. No packages
were installed or changed. Localhost port 8000 bind also passed.

Earlier #30 checks used different pins in isolated macOS/Linux environments.
They remain historical evidence for that superseded package set, not verification
of the revised requirements on macOS. The optional reviewer devcontainer build,
fresh-runtime checks after reset, sleep/restart and egress-disabled execution
remain unverified. #32 separately verified restored starter assets after a
maintainer-confirmed save/reset; that is not a complete runtime journey.
The actual ten-minute completed-project journey belongs to #39/#40.

## Observed Mocha configuration (#31/#32)

The construction branch's Project Workspace atom selects
`cd16204-dynamic-risk-assessment` (renamed from `cd16204-local-fastapi`
in #32; config ID `e88f1a29e48441358ac00ff76affa9f2` is unchanged).
It uses container `vscode`, port 3000 and
`us-central1-docker.pkg.dev/workspaces-162222/staging-images/conda-ml:latest`.
A second config, `cd0583-vscode` (`45a67ca9e4694cb69cc2aa8e87798de9`),
references the same image. The project atom overrides its path with
`/?folder=%2Fworkspace%2Fcd16204-starter-code` and has no command override.
These are observed configuration references, not an immutable image digest or
build provenance. The image build repository/CI is not exposed in this Mocha UI.
Installing into a running Workspace or changing its student disk does not prove
fresh-image provisioning. No image change is needed for the observed runtime
under the existing-version policy; an immutable digest/build source is not
established. Recheck the baseline if the shared image changes. Starter assets
were verified separately in #32 and must be resynchronized after publishing
these updated requirements and the offline reference manifest.
