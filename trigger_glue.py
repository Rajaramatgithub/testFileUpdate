import boto3

glue = boto3.client("glue")

response = glue.start_job_run(JobName="my_glue_job")

job_run_id = response["JobRunId"]

print("Job triggered: " + str(job_run_id))
