# 🧳 Travelsblog

**Travelsblog** is a full-featured travel blogging platform built with **Django** and **MongoDB**. It allows users to share their travel stories, upload beautiful images, and discover experiences from around the world through an intuitive and responsive interface.

---

## 🚀 Features

- ✍️ Create, edit, and delete travel blogs  
- 📸 Upload images to enrich your posts  
- 👥 User registration and login system  
- 🧭 Explore stories from all users  
- 🧑‍💻 Admin panel for content moderation  
- 📱 Fully responsive design using Bootstrap or TailwindCSS  

---

## 🛠️ Tech Stack

| Layer       | Technology                     |
|-------------|---------------------------------|
| Backend     | Django (Python 3.x)             |
| Frontend    | HTML, CSS, JavaScript           |
| Templating  | Django Template Language (DTL) |
| Database    | MongoDB (via Djongo/MongoEngine) |
| ORM Bridge  | `djongo` or `mongoengine`       |
| Media       | Cloudinary (for images)         |
| Tools       | Git, GitHub, Django Admin       |

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sunthesuraj/Travelsblog.git
cd Travelsblog/Blog/myproject

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
SECRET_KEY=your_django_secret_key
DEBUG=True
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/your-db-name
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

 MongoDB Setup in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your-db-name',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': os.environ.get('MONGO_URI'),
        }
    }
}

