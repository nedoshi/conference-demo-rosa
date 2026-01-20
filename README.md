# Conference Demo ROSA - E-commerce Application

This repository contains the Helm chart and Kubernetes manifests for deploying the e-commerce application on Red Hat OpenShift Service on AWS (ROSA).

## Repository Structure

```
conference-demo-rosa/
├── 02-application/              # Helm chart directory
│   ├── Chart.yaml               # Helm chart metadata
│   ├── values.yaml              # Default values
│   ├── values-dev.yaml          # Development environment values
│   ├── values-staging.yaml     # Staging environment values
│   ├── values-prod.yaml         # Production environment values
│   └── templates/               # Helm templates directory
│       ├── _helpers.tpl         # Template helpers
│       ├── deployment.yaml      # Deployment template
│       ├── service.yaml         # Service template
│       └── route.yaml           # OpenShift Route template
└── README.md
```

## Prerequisites

- Red Hat OpenShift Service on AWS (ROSA) cluster
- ArgoCD installed and configured
- Helm 3.x (for local testing)

## ArgoCD Configuration

This repository is configured to work with ArgoCD applications:

- **Development**: Points to `02-application` path with `values-dev.yaml`
- **Staging**: Points to `02-application` path with `values-staging.yaml`
- **Production**: Points to `02-application` path with `values-prod.yaml`

### Example ArgoCD Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: ecommerce-dev
  namespace: openshift-gitops
spec:
  source:
    repoURL: https://github.com/nedoshi/conference-demo-rosa.git
    targetRevision: main
    path: 02-application
    helm:
      valueFiles:
        - values-dev.yaml
  destination:
    server: https://kubernetes.default.svc
    namespace: ecommerce-dev
```

## Local Testing

To test the Helm chart locally:

```bash
# Install the chart
helm install ecommerce-dev ./02-application -f ./02-application/values-dev.yaml

# Upgrade the chart
helm upgrade ecommerce-dev ./02-application -f ./02-application/values-dev.yaml

# Uninstall the chart
helm uninstall ecommerce-dev
```

## Customization

### Environment Variables

Add custom environment variables in your values file:

```yaml
env:
  - name: CUSTOM_VAR
    value: "custom-value"
```

### Image Pull Secrets

If your images are in a private registry:

```yaml
imagePullSecrets:
  - name: my-registry-secret
```

### Resource Limits

Adjust resource limits per environment in the respective values files:

```yaml
resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 200m
    memory: 256Mi
```

## Deployment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nedoshi/conference-demo-rosa.git
   cd conference-demo-rosa
   ```

2. **Update values files** with your specific configuration

3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Initial commit: Add Helm chart for ecommerce app"
   git push origin main
   ```

4. **ArgoCD will automatically sync** the changes (if auto-sync is enabled)

## License

This is a demo repository for conference presentations.
