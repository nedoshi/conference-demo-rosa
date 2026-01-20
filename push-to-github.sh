#!/bin/bash

# Script to push conference-demo-rosa to GitHub
# Repository: https://github.com/nedoshi/conference-demo-rosa.git

set -e

REPO_URL="https://github.com/nedoshi/conference-demo-rosa.git"
BRANCH="main"

echo "=========================================="
echo "GitHub Repository Setup Script"
echo "=========================================="
echo ""
echo "Repository: $REPO_URL"
echo "Branch: $BRANCH"
echo ""

# Check if we're in the right directory
if [ ! -d "02-application" ]; then
    echo "❌ Error: 02-application directory not found!"
    echo "Please run this script from the conference-demo-rosa directory"
    exit 1
fi

echo "✅ Found 02-application directory"
echo ""

# Initialize git if needed
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Check remote
if git remote get-url origin &>/dev/null; then
    CURRENT_REMOTE=$(git remote get-url origin)
    if [ "$CURRENT_REMOTE" != "$REPO_URL" ]; then
        echo "🔄 Updating remote URL from $CURRENT_REMOTE to $REPO_URL"
        git remote set-url origin "$REPO_URL"
    else
        echo "✅ Remote already set to $REPO_URL"
    fi
else
    echo "➕ Adding remote origin..."
    git remote add origin "$REPO_URL"
fi

echo ""
echo "📋 Current git status:"
git status --short

echo ""
read -p "Do you want to proceed with adding and committing files? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

# Add all files
echo ""
echo "📝 Staging files..."
git add .

# Show what will be committed
echo ""
echo "Files to be committed:"
git status --short

echo ""
read -p "Do you want to commit these changes? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted. Files are staged but not committed."
    exit 0
fi

# Commit
echo ""
echo "💾 Committing files..."
git commit -m "Initial commit: Add Helm chart for ecommerce application" || {
    echo "⚠️  No changes to commit (files may already be committed)"
}

# Create main branch
echo ""
echo "🌿 Creating/updating main branch..."
git branch -M main

# Push
echo ""
echo "🚀 Pushing to GitHub..."
echo ""
echo "⚠️  Note: You may be prompted for GitHub credentials."
echo "   Username: nedoshi"
echo "   Password: Use a Personal Access Token (not your GitHub password)"
echo "   Create token at: https://github.com/settings/tokens"
echo ""

git push -u origin main

echo ""
echo "=========================================="
echo "✅ Success! Files pushed to GitHub"
echo "=========================================="
echo ""
echo "Repository URL: $REPO_URL"
echo "View your repository at: https://github.com/nedoshi/conference-demo-rosa"
echo ""
