# Helm Chart Usage

## Basic (sane defaults for STARLAKE connected)

`helm upgrade akhq .\akhq-minimal --install --atomic -n starlake-kafka --create-namespace`

## Environment Specific

```shell
helm upgrade akhq ./akhq-minimal/ --create-namespace --install --atomic \
--set releaseManager=${releaseMgr} \
--namespace starlake-kafka${instance} \
--set image=${url}/starlake/tchiotludo/akhq:0.23.0 \
--set source='http://connectsource-okd-<env>-connect.apps.sp1.starforge.mil:80' \
--set sink='http://svc-<app-name>-headless.starlake-connect:8083' \
--set username='' \
--set passwordSha256='' \
--set route.tls.enabled=true ${dryrun}"
```

## Tips

- For powershell, replace \ with `.
- To generate password in SHA256, in linux cli, run `echo -n 'plschangeme' | sha256sum`
