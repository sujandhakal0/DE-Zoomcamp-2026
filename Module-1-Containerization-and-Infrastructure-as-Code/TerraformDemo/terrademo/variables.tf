variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-creds.json"
}

variable "project" {
  description = "My Project name"
  default     = "pure-feat-477115-s5"
}

variable "region" {
  description = "My Project region"
  default     = "us-central1"
}

variable "location" {
  description = "My Project location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Stroage Bucket Name"
  default     = "pure-feat-477115-s5-terra-bucket"
}


variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}