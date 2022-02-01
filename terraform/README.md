# Concepts

[Terraform_overview](../1_terraform_overview.md)
  [Audio](https://drive.google.com/file/d/1IqMRDwJV-m0v9_le_i2HA_UbM_sIWgWx/view?usp=sharing)

## Execution

```shell
# Refresh service-account's auth-token for this session
gcloud auth application-default login

# Initialize state file (.tfstate); (Initialize and install)
terraform init

# Check changes to new infra plan; (Match changes against the previous state)
terraform plan -var="project=<your-gcp-project-id>"
```

```shell
# Create new infra; (apply changes to cloud)
terraform apply -var="project=<your-gcp-project-id>"
```

```shell
# Delete infra after your work, to avoid costs on any running services; (remove your stack from cloud)
terraform destroy
```
