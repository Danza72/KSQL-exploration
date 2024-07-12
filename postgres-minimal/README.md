# Helm Chart Usage

Based on bitnami's Postgres image (non-root). See their full README <https://github.com/bitnami/containers/blob/main/bitnami/postgresql/README.md>

## Basic (sane defaults for connected Openshift Local)

```shell
helm upgrade ${release-name} .\postgres-minimal --install --atomic -n ${release-namespace} --create-namespace  --set storageClass=crc-csi-hostpath-provisioner`
```

For test purposes, default user/password is "postgres/plschangeme".

## Values

- For powershell, replace \ with `.

```shell
#Basic
helm upgrade ${release-name} ./postgres-minimal --create-namespace --install --atomic \
--namespace ${release-namespace} \
--set storageClass=crc-csi-hostpath-provisioner \

#Defaults applied
--set dbName=postgres-db \
--set userName=postgres-db \
--set userPassword=plschangeme \
--set superUserPassword=plschangemepls \

#K8s secrets
--set secrets.create=true \
--set secretNameDB=starlake-credentials-db \
--set secretKeyDB=dbPassword \
--set secretNameSuper=starlake-credentials-super \
--set secretKeySuper=superPassword \

#External secrets
--set externalSecrets.enabled=true \
--set secretStoreName=vault-backend \
--set secretStoreKind=ClusterSecretStore \
--set secretNameDB=starlake-credentials-db \
--set vaultDbKey=secret/starlake-db \
--set secretNameSuper=starlake-credentials-super \
--set vaultSuperKey=secret/starlake-super \

#Disconnected
--set storageClass=freenas-iscsi-csi
--set image=${repo-url}/commonapps/bitnami/postgres:16.1 \
--set busyboxImage=${repo-url}/commonapps/busybox:1.36 \

#Production
--set storage=500Gi \
--set pvcPolicyKeep=true \
```
