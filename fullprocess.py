import training
import scoring
import deployment
import diagnostics
import reporting

################## Check and read new data
# Keep deployed ingestedfiles.txt as model-training provenance, not processing state.
# Implement output_folder_path/processedfiles.json as unique project-relative CSV paths.
# Initialize it only after the successful practice run and first reports, before
# changing input_folder_path. See README: Track successfully processed inputs.
# Missing/malformed state during automation: stop with a setup/error message.

# Compare input_folder_path CSV paths with processedfiles.json. Include the folder
# in each identity; this exercise detects new paths, not edits at existing paths.
# For this stage, use sourcedata as input_folder_path and models as output_model_path.



################## Deciding whether to proceed, part 1
# If no new paths are found, stop before ingestion, drift checking or reporting.
# Otherwise, run ingestion to update the dataset and local ingestedfiles.txt.


################## Checking for model drift
# Read the baseline latestscore.txt and model from prod_deployment_path.
# Score that SAME deployed model on the newly ingested data, before any training.
# Pass the model and data explicitly to score_model; preserve the deployed baseline.


################## Deciding whether to proceed, part 2
# Retrain and redeploy only if the new F1 score is LOWER than the baseline.
# If it is equal or higher, keep the deployed model and baseline unchanged,
# skip re-deployment, and continue to diagnostics and reporting.



################## Re-deployment
# Train a replacement model on the newly ingested data only after detecting drift.
# Score the replacement on test_data_path/testdata.csv, saving latestscore.txt
# under output_model_path. Deploy the replacement model, its new score, and the
# updated ingestedfiles.txt together by running deployment.py.

################## Diagnostics and reporting
# After processing new data, report in both drift and no-drift cases.
# Complete any re-deployment first, then use the current deployed model.
# Run reporting.py on the configured test data and save confusionmatrix2.png.
# With the API running, run apicalls.py to make real HTTP requests to all four
# endpoints and save their combined responses as apireturns2.txt.
# Preserve confusionmatrix.png and apireturns.txt from the first run.
# Unchanged model/test data may produce the same predictions, score, and matrix;
# timing and dependency results may vary. Do not force retraining for new reports.







################## Acknowledge successful processing
# After ALL required stages and both second reports succeed, atomically save the
# union of prior processed paths and the paths actually ingested in this run.
# Do this with or without drift; never overwrite deployed provenance without deployment.
# On failure, preserve the previous processing record and return failure. Repair and
# retry using the current matching deployment (a completed deployment is not rolled back).
# Do not infer success from partial outputs or acknowledge files arriving mid-run.
# Keep runs serialized; verify an unchanged-input rerun stops and a failed run can retry.
