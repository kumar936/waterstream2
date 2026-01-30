# 🚀 GitHub Deployment Guide - Streamlit Dashboard

Complete step-by-step instructions to deploy your Streamlit water forecasting dashboard to GitHub and Render.

---

## 📋 Prerequisites

Before starting, ensure you have:

- [ ] Git installed (`git --version`)
- [ ] GitHub account (free)
- [ ] Render account (free)
- [ ] Project tested locally (`streamlit run app_streamlit.py` works)

---

## PART 1: GitHub Setup (15 minutes)

### Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click **New Repository** (green button)
3. Name: `water-forecasting-streamlit`
4. Description: "Multi-Municipality Water Consumption Forecasting Dashboard"
5. Public or Private (your choice)
6. **Don't** add README yet (we have one)
7. Click **Create Repository**

### Step 2: Get Repository URL

After creation, copy the repository URL:
```
https://github.com/YOUR-USERNAME/water-forecasting-streamlit.git
```

---

## PART 2: Push Code to GitHub (10 minutes)

### Step 1: Open Terminal in Project Directory

```bash
cd c:\Users\naras\OneDrive\Desktop\dailyw\Daily-water-consumption-forecasting-and-demand-analytics
```

### Step 2: Initialize Git (if not already initialized)

```bash
git init
```

### Step 3: Add All Files

```bash
git add .
```

**Check what will be uploaded**:
```bash
git status
```

Expected output shows:
- ✅ `app_streamlit.py`
- ✅ `requirements.txt`
- ✅ `Procfile`
- ✅ `render.yaml`
- ✅ `.gitignore`
- ✅ `README.md`
- ✅ Model files (`.pkl`)
- ✅ Data file (`.csv`)
- ❌ `__pycache__/` (ignored)
- ❌ `venv/` (ignored)

### Step 4: Commit Changes

```bash
git commit -m "Initial commit: Streamlit water forecasting dashboard with ML models"
```

### Step 5: Set Remote Repository

Replace `YOUR-USERNAME` and `REPO-NAME`:

```bash
git remote add origin https://github.com/YOUR-USERNAME/water-forecasting-streamlit.git
```

### Step 6: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

**You'll be asked to:**
- Enter GitHub username
- Create a Personal Access Token (or use password)

### Step 7: Verify on GitHub

1. Go to your GitHub repository URL
2. Refresh page
3. Should see all files uploaded ✅

---

## PART 3: Render Deployment (15 minutes)

### Step 1: Create Render Account

1. Go to [Render.com](https://render.com)
2. Click **Sign up** (or Sign in if you have account)
3. Use GitHub to sign in (recommended)
4. Authorize Render to access GitHub

### Step 2: Connect GitHub Repository

1. In Render dashboard, click **Dashboard**
2. Click **New +** → **Web Service**
3. Connect to GitHub:
   - Click **Connect account** (if not already connected)
   - Click **Install**
   - Authorize Render
4. Select repository: `water-forecasting-streamlit`
5. Click **Connect**

### Step 3: Configure Service

Fill in the configuration:

**Name**:
```
water-forecasting-streamlit
```

**Region** (choose nearest):
```
Oregon (US West)  or  Frankfurt (Europe)  or  Singapore (Asia)
```

**Branch**:
```
main
```

**Runtime**:
```
Python 3
```

**Build Command**:
```
pip install -r requirements.txt
```

**Start Command**:
```
streamlit run app_streamlit.py --server.port=$PORT --server.address=0.0.0.0
```

**Environment Variables** (Optional - can add later):
```
Key: STREAMLIT_SERVER_ADDRESS
Value: 0.0.0.0

Key: STREAMLIT_SERVER_PORT
Value: 10000
```

### Step 4: Select Plan

Choose:
- **Free**: (Spins down after 15 min inactivity, good for testing)
- **Paid**: (Always on, better for production)

### Step 5: Deploy

1. Click **Create Web Service**
2. Wait for deployment (3-5 minutes)
3. You'll see logs scrolling:
   ```
   Starting build...
   Installing dependencies...
   Launching app...
   ```

### Step 6: Get Your URL

After deployment completes:
- You'll see: `https://water-forecasting-streamlit.onrender.com` (example)
- Copy this URL
- Share with your team!

---

## PART 4: Verify Deployment

### Test the Live Dashboard

1. Click the deployed URL
2. Dashboard should load (may take 30-50 sec first time)
3. Try these:
   - [ ] Select municipality from dropdown
   - [ ] Adjust temperature slider
   - [ ] Click "Get Live Prediction" button
   - [ ] See charts load
   - [ ] Check all features work

### If It Doesn't Work

**Check Logs** (Render Dashboard):
1. Go to your service in Render
2. Click **Logs** tab
3. Look for red error messages
4. Common issues:
   - Missing dependencies → Add to `requirements.txt`
   - Missing data files → Make sure `.pkl` and `.csv` are in repo
   - Wrong start command → Fix in Procfile

---

## PART 5: Updates & Maintenance

### Making Changes Locally

1. Edit files locally
2. Test: `streamlit run app_streamlit.py`
3. Commit: `git add . && git commit -m "Your message"`
4. Push: `git push origin main`
5. Render **auto-deploys** within 1-2 minutes!

### Deploy New Version

```bash
# Make changes
nano app_streamlit.py

# Test locally
streamlit run app_streamlit.py

# Push to GitHub
git add .
git commit -m "Update: New feature"
git push origin main

# Render auto-deploys!
```

### Monitor Deployment

In Render dashboard:
- **Deployment** tab: Shows status
- **Logs** tab: Shows what's happening
- **Environment** tab: View variables

---

## 📂 Project Files Checklist

Ensure these files are in GitHub:

```
✅ app_streamlit.py                         (Main app)
✅ requirements.txt                         (Dependencies)
✅ Procfile                                 (Start command)
✅ render.yaml                              (Config)
✅ .gitignore                               (Ignore rules)
✅ README.md                                (Documentation)
✅ water_consumption_model.pkl              (ML model)
✅ municipality_encoder.pkl                 (Encoder)
✅ feature_columns.pkl                      (Features)
✅ water_consumption_100000_rows_improved.csv  (Data)

❌ __pycache__/ (ignored by gitignore)
❌ venv/ (ignored by gitignore)
❌ .env (never commit secrets!)
```

---

## 🔧 File Configuration Reference

### requirements.txt
```txt
# Core Data Science
pandas==2.1.0
numpy==2.2.4
scikit-learn==1.3.0

# Web Framework - Streamlit Only
streamlit==1.32.0

# Visualization
plotly==5.17.0
matplotlib==3.7.2
seaborn==0.12.2

# Utilities
python-dateutil==2.8.2
pytz==2024.1
```

### Procfile
```
web: streamlit run app_streamlit.py --server.port=$PORT --server.address=0.0.0.0 --client.toolbarPosition=bottom
```

### .gitignore (Essential Lines)
```
__pycache__/
*.py[cod]
venv/
.venv
.env
.streamlit/secrets.toml
*.log
```

---

## 🎯 Quick Reference

### GitHub Commands

```bash
# First time setup
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR-USERNAME/REPO.git
git branch -M main
git push -u origin main

# Subsequent updates
git add .
git commit -m "Update: description"
git push origin main

# Check status
git status
git log --oneline
```

### Streamlit Commands

```bash
# Run locally
streamlit run app_streamlit.py

# Run on different port
streamlit run app_streamlit.py --server.port=8502

# Run with minimal UI
streamlit run app_streamlit.py --logger.level=error
```

---

## 📊 Deployment Status

After following all steps, you should have:

| Task | Status |
|------|--------|
| Code pushed to GitHub | ✅ |
| Service created on Render | ✅ |
| Dashboard deployed and live | ✅ |
| All features working | ✅ |
| URL shared | ✅ |

---

## 🐛 Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| "Git not found" | Install Git from git-scm.com |
| "Remote already exists" | Use `git remote set-url origin [url]` |
| "Permission denied" | Generate GitHub Personal Access Token |
| Build fails on Render | Check requirements.txt for missing packages |
| Model not loading | Ensure .pkl files are in GitHub repo |
| Data not loading | Ensure .csv file is in GitHub repo |
| Service spins down | Free tier is inactive after 15 min (upgrade for 24/7) |
| Slow first load | Normal for free tier - 30-50 sec first time |

---

## 🚀 Next Steps

1. ✅ Create GitHub repository
2. ✅ Push code to GitHub
3. ✅ Create Render account
4. ✅ Deploy service
5. ✅ Test dashboard
6. ✅ Share URL with team
7. ✅ Monitor and update as needed

---

## 📞 Support Resources

- **Git Help**: https://git-scm.com/doc
- **GitHub Guide**: https://docs.github.com
- **Render Docs**: https://render.com/docs
- **Streamlit Docs**: https://docs.streamlit.io

---

## ✅ Deployment Checklist

Before going live:

- [ ] All code committed to GitHub
- [ ] Procfile has correct Streamlit command
- [ ] requirements.txt has all dependencies
- [ ] Model and data files in GitHub
- [ ] README.md updated with actual URL
- [ ] .gitignore prevents accidentally committing secrets
- [ ] Tested locally works perfectly
- [ ] Render deployment shows "Live"
- [ ] Dashboard accessible from public URL
- [ ] All features tested on live version

---

**Your Streamlit dashboard is now deployed and live! 🎉**

Share your Render URL with colleagues and let them use the water forecasting dashboard!

---

Last Updated: January 30, 2026
