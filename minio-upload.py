#!python3
import os
import sys
from minio import Minio
from minio.error import S3Error

def upload_file_to_minio(file_path, bucket_name, endpoint, access_key, secret_key, secure=True, object_name=None):
    """
    Uploads a file to a MinIO bucket.

    Args:
    file_path (str): The path to the file to upload.
    bucket_name (str): The name of the bucket to upload the file to.
    endpoint (str): The MinIO server URL.
    access_key (str): The access key for MinIO.
    secret_key (str): The secret key for MinIO.
    secure (bool): Set to False if not using https. Defaults to True.
    object_name (str, optional): The object name in the bucket.
                                Defaults to the file name if not specified.
    """

    minio_client = Minio(endpoint,
                         access_key=access_key,
                         secret_key=secret_key,
                         secure=secure)
    # Check if the specified bucket exists
    if not minio_client.bucket_exists(bucket_name):
        print(f"Bucket '{bucket_name}' does not exist.")
        return

    # Use the file name as the object name if not provided
    if object_name is None:
        object_name = os.path.basename(file_path)

    # Upload the file
    try:
        minio_client.fput_object(bucket_name, object_name, file_path)
        print(f"'{file_path}' has been successfully uploaded as '{object_name}' in the '{bucket_name}' bucket.")
    except S3Error as e:
        print(f"An error occurred during upload: {e}")

def main():
    if len(sys.argv) != 6:
        print("Usage: python script.py <path_to_file> <bucket_name> <endpoint> <access_key> <secret_key>")
        sys.exit(1)

    file_path, bucket_name, endpoint, access_key, secret_key = sys.argv[1:6]

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"The file '{file_path}' does not exist.")
        sys.exit(1)

    # Upload the file
    upload_file_to_minio(file_path, bucket_name, endpoint, access_key, secret_key)

if __name__ == "__main__":
    main()
