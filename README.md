# 📦 Django Modular Product Management

A Django-based web application to manage installable modules and their associated products. Built using the AdminLTE theme for a modern, responsive UI.

---

## 🚀 Features

- Add, edit, install, upgrade, and uninstall modules  
- Associate multiple products with each module  
- Auto-slugging for URL paths  
- Role-based permissions (e.g., manager access for deletion)  
- AdminLTE integrated with Bootstrap 5 for styling  

---

## 🛠️ Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jejevj/django-hm-modular.git
cd yourproject
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Database Setup

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

---

## 🧪 Running the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

---

## 📁 Project Structure Overview
```
yourproject/
├── manage.py
├── requirements.txt
├── README.md
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── accounts/
│           ├── login.html
│           ├── register.html
│           └── profile.html
├── main_apps/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── utils/
│   │   ├── barcode.py
│   │   └── decorators.py
│   └── templates/
│       └── modules/
│           ├── module_list.html
│           ├── module_detail.html
│           ├── add_module.html
│           └── edit_module.html
├── djangotest/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── static/
│   └── adminlte/
├── templates/
│   ├── base.html
│   ├── base_auth.html
│   └── base_dash.html
```

---

## 🙌 Credits

- [Django](https://www.djangoproject.com/)
- [AdminLTE](https://adminlte.io/)
- [Bootstrap 5](https://getbootstrap.com/)
