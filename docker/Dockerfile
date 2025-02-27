FROM alpine/latest

# Set working directory
WORKDIR /app

# Install Python and pip using apk
RUN apk add --no-cache python3 py3-pip

# Install uv - Rust-based package installer, faster than pip
RUN pip install --no-cache-dir uv

# Create a virtual environment using uv
RUN python3 -m venv /app/.venv

# Activate the virtual environment for subsequent commands
ENV PATH="/app/.venv/bin:$PATH"

# Install streamlit using uv pip within the virtual environment
RUN uv pip install streamlit

# Expose Streamlit port (default 8501) if you intend to run a Streamlit app
EXPOSE 8501

# You can add instructions to copy your Streamlit app files here if needed
COPY ./streamlit_app.py .

# Example command to run a Streamlit app (replace streamlit_app.py with your app file)
CMD ["streamlit", "run", "streamlit_app.py"]

# Alternatively, for a basic environment, you can just leave the CMD for interactive shell
# CMD ["/bin/sh"]