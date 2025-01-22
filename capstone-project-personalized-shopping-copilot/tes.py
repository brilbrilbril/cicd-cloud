from google.cloud import secretmanager

# Create the Secret Manager client
client = secretmanager.SecretManagerServiceClient()

# Access the secret
openai_api = "projects/capstone-deploy-447802/secrets/OPENAI_API_KEY/versions/1"
response = client.access_secret_version(request={"name": openai_api})

# Get the secret payload
secret_payload = response.payload.data.decode("UTF-8")
print(f"Secret: {secret_payload}")