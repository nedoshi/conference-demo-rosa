# Quick Start: Push to GitHub

## Option 1: Use the Automated Script (Recommended)

```bash
cd /Users/flyers/.cursor/worktrees/conference-demo-rosa/mes/conference-demo-rosa
./push-to-github.sh
```

The script will guide you through:
- ✅ Checking files
- ✅ Initializing git (if needed)
- ✅ Setting up remote
- ✅ Staging files
- ✅ Committing
- ✅ Pushing to GitHub

## Option 2: Manual Commands

### 1. Create GitHub Repository
- Go to: https://github.com/new
- Name: `conference-demo-rosa`
- **Don't** initialize with README/gitignore
- Click "Create repository"

### 2. Run These Commands

```bash
# Navigate to directory
cd /Users/flyers/.cursor/worktrees/conference-demo-rosa/mes/conference-demo-rosa

# Initialize git (if needed)
git init

# Add remote
git remote add origin https://github.com/nedoshi/conference-demo-rosa.git
# OR if remote exists:
git remote set-url origin https://github.com/nedoshi/conference-demo-rosa.git

# Stage files
git add .

# Commit
git commit -m "Initial commit: Add Helm chart for ecommerce application"

# Push
git branch -M main
git push -u origin main
```

### 3. Authentication
When prompted:
- **Username**: `nedoshi`
- **Password**: Use a **Personal Access Token**
  - Create at: https://github.com/settings/tokens
  - Scope: `repo`

## Verify

After pushing, visit: https://github.com/nedoshi/conference-demo-rosa

You should see:
- ✅ `02-application/` directory with Helm chart
- ✅ `README.md`
- ✅ `.gitignore`

## Files Included

```
02-application/
├── Chart.yaml
├── values.yaml
├── values-dev.yaml
├── values-staging.yaml
├── values-prod.yaml
└── templates/
    ├── _helpers.tpl
    ├── deployment.yaml
    ├── service.yaml
    └── route.yaml
```

## Need More Help?

See `GITHUB_SETUP.md` for detailed step-by-step instructions with troubleshooting.
