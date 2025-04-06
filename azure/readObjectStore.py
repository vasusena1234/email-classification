from azure.storage.blob import ContainerClient

# NOTE: This SAS URL should be for the *container*, NOT a specific blob
# Format: https://<account>.blob.core.windows.net/<container>?<SAS-token>
container_sas_url = "https://sapcpp3o4bpathcqkmbzsikk.z15.blob.storage.azure.net/sapcp-osaas-23402bc5-000a-48ec-ae36-84737955fb53-zrs?sv=2023-11-03&spr=https&si=43762825-76c2-45d6-bf38-d40364ae9a1a&sr=c&sig=esXY1CArSocRBev6%2F6sfzKUDy3KpJAT4UJPDZVrS0k4%3D"

# Create a ContainerClient from the SAS URL
container_client = ContainerClient.from_container_url(container_sas_url)

# List all blobs in the container
print("📄 Files in container:")
for blob in container_client.list_blobs():
    print(f"➡️ {blob.name}")
