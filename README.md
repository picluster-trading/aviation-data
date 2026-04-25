# Aviation Data Mirror

This repository provides an automated weekly mirror of the NTSB aviation accident and incident dataset for ingestion into the `picluster-trading` system.

## Overview
A GitHub Action fetches the latest NTSB CSV export, normalizes it, and writes it to: data/ntsb_accidents.csv

This file is served via GitHub Raw and consumed by the ingestion module at: https://raw.githubusercontent.com/picluster-trading/aviation-data/main/data/ntsb_accidents.csv

## Update Schedule
- Weekly (Monday 03:00 UTC)
- Manual trigger available via GitHub Actions

## Purpose
Provides a stable, deterministic, CI‑safe, ingestion‑safe aviation accident dataset for the trading cluster.
