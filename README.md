# WAV Summarizer

## Disclaimer: 100% Vibe Coded

## Overview
Automatically transcribes WAV meditation files from a GCS bucket, summarizes themes and techniques, and suggests a title using Google ADK. Outputs are stored in a Google Sheet with separate columns.

## Features
- Cloud Function triggered by WAV upload
- Google Speech-to-Text transcription
- ADK summarization for summary, techniques, and suggested title
- Google Sheet logging with separate columns
- Fully environment-configurable via Pydantic
- Secure handling of API keys via Secret Manager
- Terraform deployable infrastructure

## Quickstart
1. Set `.env` variables (see `.env.example`)
2. Deploy infrastructure with Terraform
3. Upload WAVs → results appear in Google Sheet

