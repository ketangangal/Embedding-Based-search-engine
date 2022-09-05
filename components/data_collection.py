# Create a simple API-based webpage to upload images to the s3 bucket.
# Single upload and Bulk upload.
# Ngnix authentication user to upload images.
# Single upload API will be used while inferencing to collect data at runtime.
from typing import Dict, Any
import boto3.session
import boto3


# Create aws cred secure config - github actions

class DataCollection:
    def __init__(self, ):
        self.s3 = boto3.resource("s3")
        self.bucket = self.s3.Bucket("image-database-system")
        self.header = "https://image-database-system.s3.ap-south-1.amazonaws.com"

    def __create_folder(self) -> Dict[str:Any]:
        """
        This Function is responsible for creating label name folder in the bucket.
        :return: Json Response of state message (success or failure)
        """

    def single_upload(self, label: str, image_path: str) -> Dict[str:Any]:
        """
        This Function is responsible for uploading single image in the predefined
        location in the s3 bucket.
        :param label: label Name
        :param image_path: Path to the image to upload
        :return: json Response of state message (success or failure)
        """
        pass

    def bulk_upload(self, label: str, folder_path: str) -> Dict[str:Any]:
        """
        This Function is responsible for uploading bulk images in the predefined
        location in the s3 bucket.
        :param label: label Name
        :param folder_path: Path to the folder to upload
        :return: json Response of state message (success or failure)
        """
        pass

    def new_single_upload(self, label: str, image_path: str) -> Dict[str:Any]:
        """
        This Function is responsible for uploading single image in the predefined
        location in the s3 bucket.
        :param label: label Name
        :param image_path: Path to the image to upload
        :return: json Response of state message (success or failure)
        """
        pass

    def new_bulk_upload(self, label: str, image_path: str) -> Dict[str:Any]:
        """
        This Function is responsible for uploading bulk images in the predefined
        location in the s3 bucket.
        :param label: label Name
        :param image_path: Path to the image to upload
        :return: json Response of state message (success or failure)
        """
        pass