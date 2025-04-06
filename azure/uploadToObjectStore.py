from azure.storage.blob import BlobClient

# Your SAS URL — points to the container, not a specific blob
sas_url = "https://sapcpp3o4bpathcqkmbzsikk.z15.blob.storage.azure.net/sapcp-osaas-23402bc5-000a-48ec-ae36-84737955fb53-zrs/emailClassificationTrainingData/spam.csv?sv=2023-11-03&spr=https&si=43762825-76c2-45d6-bf38-d40364ae9a1a&sr=c&sig=esXY1CArSocRBev6%2F6sfzKUDy3KpJAT4UJPDZVrS0k4%3D"

# Create the blob client with full path
blob_client = BlobClient.from_blob_url(sas_url)

# Upload the local CSV file to that blob path
with open("./training/spam.csv", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("✅ spam.csv uploaded successfully to emailClassificationTrainingData/")
