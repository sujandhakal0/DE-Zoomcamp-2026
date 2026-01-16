
### 1. Prerequisites and Environment Setup

To follow this module effectively, you need **Docker**, **Python**, and a **GitHub account**.

- **Recommendation:** Use **GitHub Codespaces**. It is a remote environment that comes pre-configured with Docker and Python, saving you from the "it works on my machine" issues common with Windows or Mac.
- **Local Setup:** If you prefer working locally, Linux is the most straightforward OS for Docker. Windows and Mac users may face more complex configuration challenges.
- **Editor:** **Visual Studio Code (Desktop)** is recommended over the browser version for a more robust development experience.

### 2. Docker Fundamentals

Docker creates isolated environments called **containers** that are separate from your host machine.

- **Images vs. Containers:** A **Docker Image** is a static snapshot (like a blueprint) of an operating system and its files. A **Docker Container** is a running instance of that image.
- **Statelessness:** By default, containers are stateless. Any files created or changes made inside a container are lost once it is deleted unless you use volumes.
- **Essential Commands:**
    - `docker run hello-world`: Verifies your installation is correct.
    - `docker run -it [image]`: Starts a container with an interactive terminal.
    - `docker ps -a`: Lists all containers, including those that have exited.
    - `docker rm [ID]`: Removes a container to clean up your system.
    - `--rm` flag: Automatically removes the container when it exits.

### 3. Modern Python Tooling: UV

The workshop introduces **UV**, a dependency manager written in Rust, as a faster alternative to Conda or Mamba.

- **Why UV?** It is extremely fast and manages virtual environments efficiently, allowing you to isolate project dependencies.
- **Workflow:** Use `uv init` to start a project, `uv add [package]` to install dependencies (like Pandas or PyArrow), and `uv run python [script]` to execute code within the isolated environment.

### 4. Building and Dockerizing a Data Pipeline

A data pipeline takes an input (e.g., a CSV file), processes it, and produces an output (e.g., a database table).

- **Dockerfile:** This file contains instructions to build your custom image.
    - `FROM`: The base image (e.g., Python 3.13).
    - `WORKDIR`: Sets the working directory inside the container.
    - `COPY`: Transfers files from your host machine to the image.
    - `RUN`: Executes commands during the build (like installing libraries).
    - `ENTRYPOINT`: Defines the command that runs when the container starts.
- **Building the Image:** Run `docker build -t [name:tag] .` to create your image based on the Dockerfile.

### 5. Database Interaction (Postgres & Networking)

Data engineers frequently use Docker to run databases without installing them directly on their host machines.

- **Postgres Setup:** You can pass environment variables (`-e`) to configure the database user, password, and name.
- **Persistence:** Use **volumes** (`-v`) to ensure your database data persists even if the container is stopped or deleted.
- **Port Mapping:** Use `-p [host_port]:[container_port]` to make the database inside the container accessible to your local machine (e.g., `5432:5432`).
- **Docker Networks:** To allow two containers (like an ingestion script and a Postgres database) to communicate, you must put them on the same **Docker Network**. Once connected, they can find each other using their container names as hostnames.

### 6. Orchestration with Docker Compose

**Docker Compose** is a tool for defining and running multi-container applications using a `.yaml` file.

- **Efficiency:** Instead of running long, manual `docker run` commands for Postgres, PGAdmin, and your scripts, you define them in `docker-compose.yaml`.
- **Command:** `docker compose up` starts all defined services simultaneously and automatically sets up a shared network for them.

### 7. Pro-Tips for Learning

- **Interactive Coding:** Use **Jupyter Notebooks** for initial data exploration and then convert them into Python scripts for your final pipeline.
- **Command Line Interfaces (CLI):** Use the **Click** library to make your Python scripts configurable via command-line arguments (e.g., passing different dates or database credentials).
- **Ask for Help:** If you encounter errors, especially with Linux commands or Python logic, the sources suggest using AI tools like ChatGPT to explain specific code snippets or translate commands for different operating systems.