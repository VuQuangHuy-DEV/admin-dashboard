from storages.backends.s3boto3 import S3Boto3Storage


class CustomS3Boto3Storage(S3Boto3Storage):
    def get_object_parameters(self, name):
        s3_object_params = {
            'CacheControl': 'max-age=1000',
            'ACL': 'private'
        }
        return {**s3_object_params}
