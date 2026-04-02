# JupyterHub Custom Templates

Custom UI templates for Piksel Sandbox (JupyterHub) — spawn page, navbar, dark mode support, and modular CSS with design tokens.

## Local Development

```
make up      # start JupyterHub with templates mounted
make down    # stop
make logs    # follow logs
```

Templates are mounted via Docker volume — changes are reflected on reload.

## Build

```
make dist
```

Generates `dist/templates.yaml` — a Kubernetes ConfigMap with flattened CSS files for ConfigMap compatibility. The build rewrites `{% include 'css/...' %}` paths to flat references and bundles all templates into a single deployable YAML.

## GitOps Integration

`dist/templates.yaml` is consumed by [piksel-gitops](https://github.com/piksel-ina/piksel-gitops) as a ConfigMap mounted into the JupyterHub hub pod.
