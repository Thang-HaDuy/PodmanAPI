# Podman Manager API

A simple FastAPI-based API to manage Podman containers and pods.

## Prerequisites
- Python 3.11+
- Podman installed and running
- Podman socket enabled (`systemctl --user enable --now podman.socket`)

## Setup
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd podman_manager