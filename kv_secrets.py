# https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python
from azure.keyvault.secrets import SecretClient
from azure.identity import AzureCliCredential


def main():
    keyVaultName = "PaikendKeyVault"
    KVUri = f"https://{keyVaultName}.vault.azure.net"

    credential = AzureCliCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    secretName = input("Input a name for your secret > ")
    secretValue = input("Input a value for your secret > ")

    print(
        f"Creating a secret in {keyVaultName} called '{secretName}' with the value '{secretValue}' ..."
    )

    client.set_secret(secretName, secretValue)

    print(" done.")

    print(f"Retrieving your secret from {keyVaultName}.")

    retrieved_secret = client.get_secret(secretName)

    print(f"Your secret is '{retrieved_secret.value}'.")
    print(f"Deleting your secret from {keyVaultName} ...")

    poller = client.begin_delete_secret(secretName)
    deleted_secret = poller.result()

    print(f"{deleted_secret} done.")


if __name__ == "__main__":
    main()
