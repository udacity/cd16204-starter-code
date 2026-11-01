# A Dynamic Risk Assessment System

Starter files for the **A Dynamic Risk Assessment System** project in Udacity's **Chevron ML Model Scoring and Monitoring** course (`cd16204`), adapted from the CD0583 project. Build a workflow that trains, deploys, evaluates, and monitors a model for corporate-client attrition risk.

This repository contains **unfinished templates**, not a completed solution. Several files intentionally contain blank assignments or incomplete function bodies and will raise syntax errors until you implement them. The preinstalled software does not make the unfinished pipeline runnable.

Follow the [CD16204 project classroom](https://learn.udacity.com/cd16204?version=1.3&lessonKey=b6f49ff6-7544-486d-a913-73028a0472e9&conceptKey=16fce2d4-a2d9-4d1b-93c6-eb568f4e2559) and its rubric for the full requirements and submission instructions. Classroom access requires enrollment. The starter repository is [udacity/cd16204-starter-code](https://github.com/udacity/cd16204-starter-code); the supplied Workspace already contains the project files, so cloning or a GitHub account is not required.

## Set up your environment

### Udacity Workspace (recommended)

Use the supplied Workspace and its preinstalled Python 3.13 `ml` environment.
New terminals and the editor should use `/opt/conda/envs/ml/bin/python`.
From a Workspace terminal, check the project root and interpreter:

```bash
cd /workspace/cd16204-starter-code
pwd
python -c "import sys; print(sys.executable)"
```

The interpreter should be `/opt/conda/envs/ml/bin/python`. If a terminal is using
another existing environment, run `conda activate ml` and check again. Keep the
shared environment's installed versions. Do not install packages, create a venv,
or download missing project files. If required files or software are missing,
report the Workspace setup problem. Run every project command from this root;
the templates read `config.json` and resolve its paths relative to the current
working directory. Use the same root and `ml` environment in additional terminals.

### Optional maintainer/reviewer setup

Outside the learner Workspace, obtain the CD16204 starter and run from its root.
Use Python 3.13 and an isolated environment:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip check
python scripts/software_smoke.py
```

Alternatively, use the optional VS Code devcontainer, which installs requirements
at creation. See [Workspace software specification](WORKSPACE_SOFTWARE.md) for
image requirements, optional extension policy and verification limits. Neither
optional setup is a learner installation requirement.

## Repository layout

| File or directory | Purpose |
| --- | --- |
| `ingestion.py` | Implement data ingestion and ingestion records. |
| `training.py` | Implement model training and model persistence. |
| `scoring.py` | Implement model scoring. |
| `deployment.py` | Implement deployment of the model and associated records. |
| `diagnostics.py` | Implement predictions, dataset statistics, missing-data checks, timing, and dependency diagnostics. |
| `reporting.py` | Implement model-performance reports. |
| `app.py` | Implement the Flask API endpoints. |
| `apicalls.py` | Implement API calls and save their combined responses. |
| `fullprocess.py` | Implement the new-data and model-drift automation workflow. |
| `wsgi.py` | Expose the Flask application to a WSGI server. |
| `config.json` | Configure input, output, test-data, and deployment paths. |
| `requirements.txt` | Pin the project's Python dependencies. |
| `dependency_reference.json` | Dated shared `ml` version snapshot for the offline diagnostics exercise. |
| `practicedata/` | Supplied practice inputs: `dataset1.csv` and `dataset2.csv`. |
| `sourcedata/` | Supplied source inputs: `dataset3.csv` and `dataset4.csv`. |
| `testdata/` | Supplied evaluation input: `testdata.csv`. |
| `ingesteddata/` | Destination for your ingestion outputs. |
| `practicemodels/` | Destination for your practice model and score. |
| `models/` | Destination for your later-stage model and score. |
| `production_deployment/` | Destination for your deployed model and associated records. |

The five supplied CSV files contain fabricated corporate data. The four output directories initially contain only `.gitkeep` files; these preserve the directory structure and are not input data.

## Configuration

The starter begins with practice paths:

| Setting | Initial value |
| --- | --- |
| `input_folder_path` | `practicedata` |
| `output_folder_path` | `ingesteddata` |
| `test_data_path` | `testdata` |
| `output_model_path` | `practicemodels` |
| `prod_deployment_path` | `production_deployment` |

For the process-automation stage, follow the classroom instructions to switch `input_folder_path` to `sourcedata` and `output_model_path` to `models`. Keep the directory structure consistent when using a local environment or the Udacity Workspace.

All five values are relative to the project root. Use `testdata/testdata.csv`
for test-data scoring and reporting. Keep ingestion outputs (`finaldata.csv`,
`ingestedfiles.txt`) under `ingesteddata/`; model and score under the configured
model-output folder; and the deployed model, matching score and ingestion record
under `production_deployment/`. Save `confusionmatrix.png`, `apireturns.txt`,
their second-run counterparts and `cronjob.txt` at the project root.

## Complete the project

1. **Data ingestion:** combine the input CSV data and record which files were ingested.
2. **Training, scoring, and deployment:** train and evaluate a model, then deploy it with its score and ingestion records.
3. **Diagnostics:** implement prediction, data-quality, timing, and dependency checks.
4. **Reporting and API:** generate a confusion-matrix report, implement the endpoints below, and save their combined responses.
5. **Process automation:** stop if there is no new data. Otherwise, ingest and check for drift, retrain and redeploy only when needed, then generate reports using the current deployed model in either case. Configure the required cron job according to the classroom instructions.

These are implementation tasks, not features already provided by the templates. Generated models, scores, reports, API responses, and a completed cron job are intentionally absent from the starter.

After implementing each stage, make its script runnable from the project root.
In particular, `training.py`, `scoring.py` and `deployment.py` currently define
unfinished functions without script entry points; connecting those functions
to their inputs is part of your work. The intended first-run sequence is:

```bash
python ingestion.py
python training.py
python scoring.py
python deployment.py
python diagnostics.py
```

These commands are for your completed scripts. Do not expect the starter to pass
them before implementing the exercises. Start the API and produce the first
reports as described below. After completing the automation stage and switching
the configuration to `sourcedata`/`models`, run `python fullprocess.py` with the
local API running. Retain the required ten-minute scheduling exercise from the
classroom; manual execution alone does not replace it.

Calculate the mean, median, and standard deviation for each numeric column in the ingested dataset and return the results as a Python list. Calculate missing-value percentages for every column. Time ingestion and training, as specified by Step 3 and the rubric, without replacing the deployed model.

Pass a model and a DataFrame explicitly to `score_model(model, dataframe, score_path=None)`. Use the following model, data, and score-saving behavior in each context:

| Context | Model | Evaluation data | Save a score? |
| --- | --- | --- | --- |
| Step 2 and replacement training | `output_model_path` | `test_data_path/testdata.csv` | `output_model_path/latestscore.txt` |
| `/scoring` API | `prod_deployment_path` | `test_data_path/testdata.csv` | No |
| Drift check | Same deployed model | Newly ingested data | No |

Retrain only when the drift-check F1 score is lower than the deployed baseline. Score the replacement before deploying it so that its `latestscore.txt` belongs to that model. The prediction helper accepts a DataFrame; the API must load the dataset location supplied by its caller before invoking it.

After processing new data, run reporting and API calls whether or not drift occurred, completing any redeployment first. Use the current deployed model and configured test data for the confusion matrix and API score. Save `confusionmatrix2.png` and `apireturns2.txt` while preserving the first-run files. Without drift, keep the deployed model and baseline score unchanged; identical predictions, scores, and confusion matrices are valid when the model and test data are unchanged. Timing and dependency results may vary. Do not force retraining or alter the baseline to produce different reports.

### Track successfully processed inputs

Keep three different records:

| Record | Meaning |
| --- | --- |
| `output_folder_path/ingestedfiles.txt` | CSV filenames used to build the current ingested dataset. Ingestion alone does not prove the pipeline succeeded. |
| `prod_deployment_path/ingestedfiles.txt` | Training-input provenance of the deployed model. Update it only when deploying a replacement, together with its matching model and score. |
| `output_folder_path/processedfiles.json` | Successfully processed input identities across runs; independent of model provenance. |

Implement the processing record yourself as a JSON list of unique project-relative
CSV paths using `/`, including the input folder (for example,
`practicedata/dataset1.csv`). Files with the same basename in different folders
are distinct. This exercise detects new paths, not changed contents at an existing
path; content hashing is not required.

After completing the initial practice ingestion, training, scoring, deployment
and first reports, initialize the processing record from the practice ingestion
record and its input folder, **before** switching to `sourcedata`/`models`.
Do not initialize it from the newly selected source files. If the record is
missing later, stop with a setup/recovery message; if malformed, stop with an
error. Do not infer success from existing reports or silently acknowledge inputs.

In Step 5, compare discovered CSV paths with the processing record, not the
deployed training provenance. If any path is new, ingest all CSVs in the configured
input folder as before, then perform drift evaluation and both second reports.
Only after every required stage succeeds, atomically save the union of the previous
record and the paths actually ingested in that run. Do this in both drift and
no-drift cases. Do not rediscover and acknowledge files that arrived during the run.
With no new paths, stop before ingestion, drift checks, training or reports.

On any failure, leave the previous processing record unchanged and return a
failure status. Repair the cause and retry the same inputs; partial outputs are
not proof of success. If deployment already succeeded before reporting failed,
retain the matching deployed model/score/provenance and retry using that current
deployment; preserve the first reports and acknowledge inputs only after success.
Do not promise automatic rollback of a completed deployment. Keep scheduled runs
serialized with the existing overlap lock.

For each independent validation scenario, initialize from that copy's successful
practice run. After each new-data scenario, rerun unchanged inputs and check that
no further stages run and deployment/reports stay unchanged. Also check a failed
report request (for example with the API stopped): the processing record must
stay unchanged, and a successful retry after recovery must acknowledge the inputs.
Include the processing record with submission artifacts; do not ship a prefilled
record in the unfinished starter.

### Offline dependency diagnostics

Implement `outdated_packages_list()` in `diagnostics.py` using the root-level
[`dependency_reference.json`](dependency_reference.json). Its `packages` mapping
contains distribution names and reference versions; `captured_on_utc` and
`provenance` identify the observation date, source and environment. The reference
records the existing shared `ml` versions verified in issue #31. It is a dated
snapshot, **not live latest package-index data or an upgrade recommendation**.

For every listed distribution, read the installed version locally with Python's
standard-library `importlib.metadata`. Report three columns: package name,
installed version, and reference version (dated snapshot). Display missing
distributions as `not installed` and continue with the remaining packages.
Include the snapshot date and provenance with the report. A difference alone
does not establish that a package is older, unsafe or needs upgrading. Return
the dependency table through the diagnostics API alongside the other required
diagnostics. The existing function name is retained for compatibility.

Do not query PyPI or another registry, run `pip list --outdated`, or install,
upgrade or downgrade packages. Preserve the shared `ml` environment. The manifest
is support data; the comparison function and its report remain learner work.
Maintainers update the manifest only after verifying a new shared baseline and
recording its provenance; students do not refresh it from the network. Include
the reference file with the project source in the Workspace or optional archive.

### API development

After implementing the required functions and creating the necessary data and model artifacts, start the development API from the repository root:

```bash
python app.py
```

The development server binds to `127.0.0.1` on port **8000**. Keep it running.
In a second terminal at the same project root using `ml`, run the completed
first-run reporting scripts:

```bash
python apicalls.py
python reporting.py
```

Use `http://127.0.0.1:8000` for API requests. POST `/prediction` accepts JSON
with `dataset_path`, such as `{"dataset_path": "testdata/testdata.csv"}`; load
that local CSV before invoking the prediction helper. A hosted server, public
URL and WSGI deployment are not required. `wsgi.py` is optional server context.

| Method | Endpoint | Intended response |
| --- | --- | --- |
| POST | `/prediction` | Predictions for the supplied dataset location. |
| GET | `/scoring` | The deployed model's score. |
| GET | `/summarystats` | Dataset summary statistics. |
| GET | `/diagnostics` | Timing, missing-data, and dependency diagnostics. |

The initial endpoint bodies do not return usable responses. Keep the model and data used by each endpoint consistent with the classroom requirements. The included Flask debug server is for development.

## Validate the automation branches

`validation_data/no_drift/no_drift.csv` and `validation_data/drift/drift.csv` are synthetic fixtures for checking control flow, not realistic performance benchmarks. Each contains eight unique rows and both target classes. They share feature values but deliberately use opposite labels. Keep them separate from `practicedata`, `sourcedata`, and `testdata`; do not ingest the entire `validation_data` tree.

Before each scenario, use an independent project copy and complete Steps 1–4 with the original practice configuration. Train on all 26 deduplicated practice rows, use the three specified features and the Logistic Regression settings in `training.py`, and score on the unchanged `testdata/testdata.csv`. Deploy that model, its score, and the practice ingestion record. Initialize `processedfiles.json` only after the practice run and first reports succeed, as described above. Preserve these initial artifacts; do not carry a scenario's replacement model or ingestion record into another scenario.

Then set `input_folder_path` as shown below, set `output_model_path` to `models`, and run your completed `fullprocess.py` with the API running from the same project root.

| Scenario / `input_folder_path` | Initial model F1 on scenario data | Expected behavior |
| --- | --- | --- |
| No new data / `practicedata` | Not evaluated | Stop; no retraining, deployment, or second reports. |
| No drift / `validation_data/no_drift` | 1.0 | Keep the deployed model and baseline; generate both second reports. |
| Drift / `validation_data/drift` | 0.0 | Retrain, score the replacement on test data, deploy, then generate both second reports. |

The initial test-data baseline is approximately **0.5714**. These values were checked with Python 3.13.15 and scikit-learn 1.8.0 on macOS ARM64; they assume the initial model described above. A different model or preprocessing may change the comparison. Do not edit the baseline score to force a branch. In the drift scenario, 0.0 is the initial deployed model's score on the fixture, not the replacement model's test score.

Check that each new-data scenario creates `confusionmatrix2.png` and `apireturns2.txt` and preserves the first-run reports. In the no-drift scenario, also confirm that the deployed model and baseline score remain unchanged. Restore the classroom configuration (`sourcedata` and `models`) for the final project run.

## Submission

### Choose a submission method

**Workspace submission is recommended.** Keep the completed project under
`/workspace/cd16204-starter-code` and submit through the course Workspace.
This route requires no external account, repository URL, Git history or manual
ZIP upload. Save all files and check the rubric before submitting. Download a
backup before any Workspace data Reset; a running API or installed cron entry
does not replace saved source and evidence files.

**ZIP upload and GitHub repository selection are optional alternatives.** Use
the same files and directory layout for every method. For GitHub, select your
completed repository through the available submission option and confirm the
required generated files are included even if ignored by Git. A bare/private
Azure Repos URL, pipeline link, screenshot or starter-only repository is not a
substitute for the required source and artifacts. No hosted deployment is needed.

### Required-file checklist

All paths below are relative to the project root. Preserve directories; do not
flatten files with the same name into one folder.

| Include | Files and purpose |
| --- | --- |
| Completed source | `ingestion.py`, `training.py`, `scoring.py`, `deployment.py`, `diagnostics.py`, `reporting.py`, `app.py`, `apicalls.py`, `fullprocess.py`. Keep supplied `wsgi.py` as context; WSGI hosting is not required. |
| Configuration and reproduction notes | `config.json`, `requirements.txt`, `dependency_reference.json`, and `README.md` with your run order, configuration changes, observed drift/no-drift outcome and scheduling evidence location. Requirements/reference files record the supplied environment; do not install or upgrade packages. |
| Supplied inputs | `practicedata/dataset1.csv`, `practicedata/dataset2.csv`, `sourcedata/dataset3.csv`, `sourcedata/dataset4.csv`, `testdata/testdata.csv`, and the supplied `validation_data/` fixtures for separate branch checks. Do not mix validation fixtures into the final source-data run. |
| Ingestion outputs | `ingesteddata/finaldata.csv` and `ingesteddata/ingestedfiles.txt` from the final configured ingestion, plus `ingesteddata/processedfiles.json` recording successfully processed inputs. |
| Practice artifacts | `practicemodels/trainedmodel.pkl` and its matching `practicemodels/latestscore.txt`; preserve these initial-stage outputs. |
| Final candidate artifacts, when retraining occurred | `models/trainedmodel.pkl` and its matching `models/latestscore.txt`. If no drift occurred, this directory may remain empty; do not train or fabricate artifacts just to fill it. |
| Current deployment | `production_deployment/trainedmodel.pkl`, its matching `production_deployment/latestscore.txt`, and `production_deployment/ingestedfiles.txt`. With no drift, preserve the deployed model and baseline score. |
| Both report pairs | Root-level `confusionmatrix.png`, `apireturns.txt`, `confusionmatrix2.png` and `apireturns2.txt`. Generate the second pair after processing new data even without drift; identical predictions, scores or matrices can be valid. |
| Scheduling evidence | Root-level `cronjob.txt` containing the single ten-minute project entry, plus `fullprocess.log` showing a timestamped actual scheduled invocation and its result. Preserve unrelated installed jobs; do not submit them. Manual execution or a crontab listing alone does not prove scheduling ran. |

Optional PDF, time-trend or SQLite work supplements these required files. It does
not replace them or introduce required software installation.

### Check reproducibility

Keep the submitted `config.json` set to `sourcedata` and `models`, with the other
paths unchanged. Include the actual data and matching deployed artifacts, not
only filenames, empty placeholders or screenshots. Use the preinstalled `ml`
environment; required results must not depend on an external service or account.

In a separate disposable copy, follow Steps 1–4 using the initial practice
configuration and your completed script entry points. Start `python app.py` in
one terminal; use the same root/environment in another for `python apicalls.py`
and `python reporting.py`. Then switch to the final configuration and run
`python fullprocess.py` as in Step 5, keeping the API available. Do not rerun
training or ingestion over your only saved submission artifacts. Repeating the
process with no new data should stop before drift checks or new reports.

Record how to reproduce the three automation branches using the README's
separate validation scenarios. Keep the first report pair, preserve the
deployed baseline during drift checks, and never change labels or baseline
scores to force drift. Cron registration is Workspace state, not a portable
file: document the supported installation/recovery steps and retain the actual
invocation log. Scheduling runs only while the Workspace is running.

### Optional ZIP preparation

Use the Workspace file interface to download an archive if available, or create
one with the existing Python standard library. From the completed project root:

```bash
python -m zipfile -c ../cd16204-submission.zip README.md ingestion.py training.py scoring.py deployment.py diagnostics.py reporting.py app.py wsgi.py apicalls.py fullprocess.py config.json requirements.txt dependency_reference.json practicedata sourcedata testdata validation_data ingesteddata practicemodels models production_deployment confusionmatrix.png apireturns.txt confusionmatrix2.png apireturns2.txt cronjob.txt fullprocess.log
python -m zipfile -l ../cd16204-submission.zip
```

Add optional work only if attempted. Extract the ZIP into an empty disposable
folder and compare it with the checklist before uploading. Confirm that data,
models and reports are present and readable, paths remain relative to the
extracted root, and your completed scripts can reproduce the results there in
the supplied environment. Creating an archive alone is not a runtime check.

### Protect sensitive information

For every submission method, exclude credentials, tokens, private keys,
secret-bearing `.env` files, confidential employer data and unmasked pipeline
logs. Rotate any exposed credential under your provider/organization procedure.
Do not include `.git`, virtual/Conda environments, caches or unrelated files.
Keep only the project-specific scheduling log and remove sensitive content.
Never invite unknown reviewers to a private organization or weaken permissions;
use the Workspace or optional ZIP route if repository access is unsuitable.

The starter templates alone are not a completed submission. Review every
specification in the course project rubric before submitting.

## License

See [LICENSE](LICENSE) for the repository's license terms.
