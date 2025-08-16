# --- Buckets ---
resource "google_storage_bucket" "audio_bucket" {
  name                        = "${var.GCP_PROJECT}-meditation-audio"
  location                    = var.GCP_REGION
  force_destroy               = true
  uniform_bucket_level_access = true
}

resource "google_storage_bucket" "function_bucket" {
  name                        = "${var.GCP_PROJECT}-meditation-function"
  location                    = var.GCP_REGION
  force_destroy               = true
  uniform_bucket_level_access = true
}

# --- Service Account ---
resource "google_service_account" "function_sa" {
  account_id   = "meditation-function-sa"
  display_name = "Meditation Function Service Account"
}

# --- IAM Roles for Cloud Function ---
resource "google_project_iam_member" "function_sa_roles" {
  for_each = toset([
    "roles/cloudfunctions.invoker",
    "roles/storage.objectAdmin",
    "roles/secretmanager.secretAccessor",
    "roles/sheets.admin"
  ])
  project = var.GCP_PROJECT
  role    = each.value
  member  = "serviceAccount:${google_service_account.function_sa.email}"
}

# --- Cloud Function ---
resource "google_cloudfunctions_function" "meditation_transcriber" {
  name        = "meditation-transcriber"
  runtime     = "python310"
  region      = var.GCP_REGION
  entry_point = "gcs_trigger"

  source_archive_bucket = google_storage_bucket.function_bucket.name
  source_archive_object = "meditation-function.zip"

  trigger_bucket = google_storage_bucket.audio_bucket.name

  service_account_email = google_service_account.function_sa.email

  environment_variables = {
    GCP_PROJECT = var.GCP_PROJECT
    SHEET_NAME  = var.SHEET_NAME
    ADK_MODEL   = var.ADK_MODEL
  }
}

