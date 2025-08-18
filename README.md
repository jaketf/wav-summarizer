# WAV Summarizer

## Disclaimer: ~100% Vibe Coded
This project is an experiment of using LLMs to write basic but useful serverless agentic AI apps.
I write code for a living, teaching yoga and meditation is my passion.
I need automation to help me spend less time coding and ease my content creation flow. 
I wanted to see how far I could get vibe coding the basic agents I need to work through a backlog of meditation files I've recorded and see what's worth producing.

This is a very basic POC, in the future I'd like to make this part of a larger pipeline that can automate editing and mixing the meditation files over public domain meditation tracks, prompting a user to listen and approve them before publishing to youtube, insight timer, etc.  

## Overview
Automatically transcribes WAV files from a GCS bucket, summarizes themes and techniques, and suggests a title using Google ADK. Outputs are stored in a Google Sheet with separate columns.

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

