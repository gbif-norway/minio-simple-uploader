# Simple MinIO Upload Tool

This repository contains a Python script for uploading files to a MinIO server, along with a GitHub Actions workflow for building a Windows executable using PyInstaller.

## Features

- **Easy File Uploads**: Simplify the process of uploading files to a MinIO bucket.
- **Automated Executable Builds**: Automatically build a Windows executable upon each push to the main branch.
- **Secure Handling**: Designed to handle credentials and sensitive information securely.

## Getting Started

### Prerequisites

- Python 3.11.2 or later.
- MinIO server access (endpoint, access key, and secret key).

### Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/minio-upload-tool.git
cd minio-simple-uploader
```

### Usage
#### Run the script with the necessary parameters:

```bash
python minio-upload.py <path_to_file> <bucket_name> <endpoint> <access_key> <secret_key>
```
#### Using the Windows Executable

For Windows users, an executable file is available in the Releases section of this repository.
Download the minio-upload.exe from the latest release.
Open Command Prompt and navigate to the directory where minio-upload.exe is located.
Run the executable with the necessary parameters:
```cmd
minio-upload.exe <path_to_file> <bucket_name> <endpoint> <access_key> <secret_key>
```
No Python installation is required for using the executable.

### Building the Executable

The executable is automatically built and released via GitHub Actions upon each push to the main branch. You can also build it manually using PyInstaller:
```bash
pyinstaller --onefile --noconsole minio-upload.py
```
### GitHub Actions Workflow

The .github/workflows/build_exe.yml file defines the workflow for building the Windows executable. This process includes:

    Setting up a Python environment.
    Installing PyInstaller.
    Building the executable.
    Creating a GitHub release.
    Uploading the executable to the release.

### Contributing

Contributions to this project are welcome! Please feel free to submit issues and pull requests.
License

This project is licensed under the [MIT License](./LICENSE).
