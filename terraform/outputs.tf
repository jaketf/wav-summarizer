output "audio_bucket_name" {
  value = google_storage_bucket.audio_bucket.name
}

output "function_bucket_name" {
  value = google_storage_bucket.function_bucket.name
}

output "cloud_function_name" {
  value = google_cloudfunctions_function.meditation_transcriber.name
}

output "service_account_email" {
  value = google_service_account.function_sa.email
}

