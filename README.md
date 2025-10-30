# 🧩 Project Environment Setup Guide

This guide helps you set up a Python virtual environment for the project.

---

## ⚙️ Prerequisites

Before proceeding, make sure you have the following installed on your system:

- **Python 3.8+**
- **pip (Python package manager)**
- **Git** (optional, if cloning from a repository)
- **Linux/WSL/Ubuntu environment**

---

## 🏗️ Step 1: Update System Packages

```bash
sudo apt update
```

---

## 🧱 Step 2: Install Virtual Environment Module

```bash
sudo apt install python3-venv -y
```

---

## 🧬 Step 3: Create a Virtual Environment

Inside your project root directory, run:

```bash
python3 -m venv venv
```

This creates a folder named **`venv/`** which holds your isolated Python environment.

---

## 🚀 Step 4: Activate the Virtual Environment

Run the following command:

```bash
source venv/bin/activate
```

After activation, your terminal prompt should start with `(venv)` — indicating you’re inside the virtual environment.

---

## 📦 Step 5: Install Project Dependencies

Make sure you have a **`requirements.txt`** file inside the `backend/` folder.  
Then, install all dependencies using:

```bash
pip install -r backend/requirements.txt
```

---

## 🧹 Step 6: Deactivate Environment (Optional)

Once done, you can deactivate the environment using:

```bash
deactivate
```

---

## ✅ Notes

- Always **activate the virtual environment** before running the project.  
- To regenerate the requirements file (after adding new packages):

```bash
pip freeze > backend/requirements.txt
```

---

**Author:** *Subhiksha Kodibass*  
**Project:** *HireBOT – Automated Mail Communication System*