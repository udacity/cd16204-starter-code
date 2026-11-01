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

Before each scenario, use an independent project copy and complete Steps 1–4 with the original practice configuration. Train on all 26 deduplicated practice rows, use the three specified features and the Logistic Regression settings in `training.py`, and score on the unchanged `testdata/testdata.csv`. Deploy that model, its score, and the practice ingestion record. Preserve these initial artifacts; do not carry a scenario's replacement model or ingestion record into another scenario.

Then set `input_folder_path` as shown below, set `output_model_path` to `models`, and run your completed `fullprocess.py` with the API running from the same project root.

| Scenario / `input_folder_path` | Initial model F1 on scenario data | Expected behavior |
| --- | --- | --- |
| No new data / `practicedata` | Not evaluated | Stop; no retraining, deployment, or second reports. |
| No drift / `validation_data/no_drift` | 1.0 | Keep the deployed model and baseline; generate both second reports. |
| Drift / `validation_data/drift` | 0.0 | Retrain, score the replacement on test data, deploy, then generate both second reports. |

The initial test-data baseline is approximately **0.5714**. These values were checked with Python 3.13.15 and scikit-learn 1.8.0 on macOS ARM64; they assume the initial model described above. A different model or preprocessing may change the comparison. Do not edit the baseline score to force a branch. In the drift scenario, 0.0 is the initial deployed model's score on the fixture, not the replacement model's test score.

Check that each new-data scenario creates `confusionmatrix2.png` and `apireturns2.txt` and preserves the first-run reports. In the no-drift scenario, also confirm that the deployed model and baseline score remain unchanged. Restore the classroom configuration (`sourcedata` and `models`) for the final project run.

## Submission

Use the classroom rubric as the final checklist. Submit the required scripts and generated outputs in a ZIP, including both report pairs (`confusionmatrix.png` / `apireturns.txt` and `confusionmatrix2.png` / `apireturns2.txt`) and `cronjob.txt`. The second pair is required after new-data processing even without drift. The starter repository itself is not a completed submission.

## License

See [LICENSE](LICENSE) for the repository's license terms.
