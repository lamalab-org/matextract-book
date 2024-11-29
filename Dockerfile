# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.5.5 /uv /uvx /bin/

ENV UV_SYSTEM_PYTHON=1

# Install PyTorch with CUDA support
RUN uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN uv pip install -r package/requirements.txt

# Install the local package
RUN uv pip install -e .

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Create a non-root user and switch to it
RUN useradd -m jupyter
USER jupyter

# Run Jupyter when the container launches
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
