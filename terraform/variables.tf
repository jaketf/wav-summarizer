variable "GCP_PROJECT" {
  type = string
}

variable "GCP_REGION" {
  type    = string
  default = "us-central1"
}

variable "SHEET_NAME" {
  type    = string
  default = "Meditation Transcripts"
}

variable "ADK_MODEL" {
  type    = string
  default = "models/text-bison-001"
}

