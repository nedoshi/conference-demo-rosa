# Step-by-Step Guide: Create GitHub Repository and Push Files

This guide will walk you through creating a new GitHub repository and pushing the Helm chart files.

## Prerequisites

- GitHub account (username: `nedoshi`)
- Git installed on your local machine
- Terminal/Command line access

## Step 1: Create GitHub Repository via Web UI

1. **Go to GitHub**: Open your browser and navigate to https://github.com/new

2. **Repository Settings**:
   - **Repository name**: `conference-demo-rosa`
   - **Description**: `E-commerce application Helm chart for ROSA conference demo` (optional)
   - **Visibility**: Choose **Public** or **Private** (your choice)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these files)

3. **Click "Create repository"**

4. **Copy the repository URL**: You'll see something like:
   ```
   https://github.com/nedoshi/conference-demo-rosa.git
   ```

## Step 2: Navigate to Your Local Directory

Open your terminal and navigate to the directory containing the files:

```bash
cd /Users/flyers/.cursor/worktrees/conference-demo-rosa/mes/conference-demo-rosa
```

## Step 3: Initialize Git Repository (if not already initialized)

Check if git is already initialized:

```bash
git status
```

If you see "not a git repository", initialize it:

```bash
git init
```

## Step 4: Add Remote Repository

Add the GitHub repository as the remote origin:

```bash
git remote add origin https://github.com/nedoshi/conference-demo-rosa.git
```

If the remote already exists with a different URL, update it:

```bash
git remote set-url origin https://github.com/nedoshi/conference-demo-rosa.git
```

Verify the remote:

```bash
git remote -v
```

You should see:
```
origin  https://github.com/nedoshi/conference-demo-rosa.git (fetch)
origin  https://github.com/nedoshi/conference-demo-rosa.git (push)
```

## Step 5: Stage All Files

Add all files to git staging:

```bash
git add .
```

Or add specific files:

```bash
git add 02-application/
git add README.md
git add .gitignore
```

Verify what will be committed:

```bash
git status
```

You should see files like:
- `02-application/Chart.yaml`
- `02-application/values.yaml`
- `02-application/values-dev.yaml`
- `02-application/values-staging.yaml`
- `02-application/values-prod.yaml`
- `02-application/templates/_helpers.tpl`
- `02-application/templates/deployment.yaml`
- `02-application/templates/service.yaml`
- `02-application/templates/route.yaml`
- `README.md`
- `.gitignore`

## Step 6: Commit Files

Create your first commit:

```bash
git commit -m "Initial commit: Add Helm chart for ecommerce application"
```

## Step 7: Create Main Branch and Push

Create and switch to the main branch:

```bash
git branch -M main
```

Push to GitHub:

```bash
git push -u origin main
```

**Note**: If this is your first time pushing to GitHub from this machine, you may be prompted for credentials:
- **Username**: `nedoshi`
- **Password**: Use a **Personal Access Token** (not your GitHub password)
  - Create one at: https://github.com/settings/tokens
  - Select scopes: `repo` (full control of private repositories)

## Step 8: Verify on GitHub

1. Go to: https://github.com/nedoshi/conference-demo-rosa
2. You should see all your files:
   - `02-application/` directory with Chart.yaml and templates
   - `README.md`
   - `.gitignore`

## Troubleshooting

### Issue: Authentication Failed

**Solution**: Use a Personal Access Token instead of password:
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Name it: `conference-demo-rosa`
4. Select scope: `repo`
5. Click "Generate token"
6. Copy the token and use it as your password when pushing

### Issue: Remote Already Exists

**Solution**: Remove and re-add the remote:
```bash
git remote remove origin
git remote add origin https://github.com/nedoshi/conference-demo-rosa.git
```

### Issue: Branch Already Exists

**Solution**: If you're in a detached HEAD state:
```bash
git checkout -b main
git push -u origin main
```

### Issue: Permission Denied

**Solution**: Check your git configuration:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Quick Command Summary

Here's the complete sequence of commands:

```bash
# Navigate to directory
cd /Users/flyers/.cursor/worktrees/conference-demo-rosa/mes/conference-demo-rosa

# Initialize git (if needed)
git init

# Add remote
git remote add origin https://github.com/nedoshi/conference-demo-rosa.git
# OR update existing remote:
git remote set-url origin https://github.com/nedoshi/conference-demo-rosa.git

# Stage files
git add .

# Commit
git commit -m "Initial commit: Add Helm chart for ecommerce application"

# Create main branch and push
git branch -M main
git push -u origin main
```

## Next Steps After Pushing

1. **Update ArgoCD**: Update your ArgoCD application YAML files to use:
   ```yaml
   repoURL: https://github.com/nedoshi/conference-demo-rosa.git
   ```

2. **Test ArgoCD Sync**: ArgoCD should automatically sync from the `02-application` path

3. **Verify Helm Chart**: Test locally:
   ```bash
   helm template ./02-application -f ./02-application/values-dev.yaml
   ```

## File Structure Summary

Your repository should have this structure:

```
conference-demo-rosa/
├── 02-application/
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── values-dev.yaml
│   ├── values-staging.yaml
│   ├── values-prod.yaml
│   └── templates/
│       ├── _helpers.tpl
│       ├── deployment.yaml
│       ├── service.yaml
│       └── route.yaml
├── README.md
└── .gitignore
```

---

**Need Help?** If you encounter any issues, check the error message and refer to the troubleshooting section above.
