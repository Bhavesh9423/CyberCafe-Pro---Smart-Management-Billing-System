# CyberCafe Pro - Smart Management & Billing System

## Quick Start (Local)
```bash
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
# Login: admin / admin123
```

## Deploy to Render
1. Push code to GitHub
2. Create new Web Service on render.com
3. Connect your repo
4. Render auto-detects render.yaml

## Convert to EXE (Windows)
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "templates;templates" --add-data "static;static" app.py
# EXE will be in dist/ folder
```

## Features
- Admin login (admin/admin123)
- Customer management (add/edit/delete/search)
- Customer profile with document upload
- Billing with auto-invoice numbers
- Professional printable invoices
- Excel export
- Activity logging
