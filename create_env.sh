sh -c "az login --use-device-code"
sh -c "az group create --name KeyVault-PythonQS-rg --location koreacentral"
sh -c "az keyvault create --name PaikendKeyVault --resource-group KeyVault-PythonQS-rg"
