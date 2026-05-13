# BARTR 🛒

BARTR is a Django-based bartering marketplace that allows users to solicit, exchange, and discover services, products, and information on a centralized platform.

Instead of traditional buying and selling, BARTR focuses on value exchange—users can post listings for what they need or what they can offer, whether that’s a service, physical item, or knowledge-based exchange.

## 🚀 Core Concept

BARTR is built around the idea of modern bartering:
- Users can create listings offering services, products, or information
- Users can browse and respond to community listings
- The platform enables value-for-value exchanges instead of cash transactions
- All activity is centralized in a clean, searchable marketplace interface

## 🧱 Features

- User authentication (login/logout required for interactions)
- Create bartering listings with title, description, and image
- Browse a centralized marketplace of community offers and requests
- Ownership-based permissions for editing and deleting listings
- Responsive grid-based UI for clean browsing experience
- Empty-state UI encouraging user participation when no listings exist

## 🧠 Key Design Philosophy

BARTR is designed to simulate a decentralized value economy inside a centralized platform:
- Emphasis on peer-to-peer exchange instead of traditional e-commerce
- Lightweight, fast UI focused on discovery and posting
- Ownership-driven content control (users manage their own listings)
- Built for scalability into services, goods, and knowledge exchange ecosystems

## 🧱 Tech Stack

- Python
- Django 6
- SQLite (development)
- Tailwind CSS (via CDN)
- Heroku-ready deployment configuration

## 📁 Project Structure

- `listings/` → Core marketplace logic (models, views, templates)
- `templates/` → Base and shared UI structure
- `main/` → Project settings and configuration

## ⚙️ Setup (Local Development)

```bash
git clone <repo-url>
cd bartr
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver