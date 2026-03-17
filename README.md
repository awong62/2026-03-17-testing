# 2026-03-17-testing

Today we'll talk about testing. Use the following instructions to setup your environment. 

## Environment Setup

This repository includes a Docker Compose setup with two services:

- `rstudio` builds from `rocker/rstudio`, installs the R package `testthat`, and mounts this repository at `/home/rstudio/project`.
- `vscode` builds a VS Code Server image with Python `3.12`, installs `pandas`, `matplotlib`, and `pytest`, and mounts this repository at `/project`.

Build the images:

```bash
docker compose build
```

Start the RStudio environment:

```bash
docker compose up rstudio
```

Then open `http://localhost:8787` and sign in with:

- Username: `rstudio`
- Password: `rstudio`

Start the VS Code Server environment:

```bash
docker compose up vscode
```

Then open `http://localhost:8080`.

In VS Code Server, open the `/project` folder.

To stop the services, press `Ctrl+C` in the running terminal, or use:

```bash
docker compose down
```