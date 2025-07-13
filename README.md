  <h1>🏢 Company & Employee Management API</h1>
  <p>A RESTful API built using <strong>Django</strong> and <strong>Django REST Framework</strong> to manage companies and their employees. This project supports full CRUD operations and includes a custom endpoint to retrieve employees of a specific company.</p>

  <hr>

  <h2>📌 Features</h2>
  <ul>
    <li>✅ CRUD operations for Companies and Employees</li>
    <li>✅ Custom endpoint to fetch employees of a specific company</li>
    <li>✅ Modular Django app structure</li>
    <li>✅ Browsable API interface via Django REST Framework</li>
    <li>✅ Hyperlinked serializers for clean, navigable responses</li>
  </ul>

  <h2>🛠 Tech Stack</h2>
  <ul>
    <li><strong>Backend:</strong> Python, Django</li>
    <li><strong>API Framework:</strong> Django REST Framework</li>
    <li><strong>Database:</strong> SQLite (can be upgraded to PostgreSQL/MySQL)</li>
    <li><strong>Tools:</strong> pip, venv, Postman</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <pre>
project_root/
├── API/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── project_root/
│   └── urls.py
├── manage.py
├── requirements.txt
  </pre>

  <h2>🚀 Installation</h2>
  <p><strong>Prerequisites:</strong> Python 3.8+, pip</p>
  <pre>
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Start the server
python manage.py runserver
  </pre>

  <h2>🔗 API Endpoints</h2>  <br>

  <img width="1897" height="1005" alt="Screenshot 2025-07-13 185202" src="https://github.com/user-attachments/assets/6260011c-ebc9-4254-8f0c-d206a43e99a8" />  <br><br>


  <h3>📁 Company</h3>
  <table border="1" cellpadding="8" cellspacing="0">
    <tr><th>Method</th><th>Endpoint</th><th>Description</th></tr>
    <tr><td>GET</td><td>/api/v1/companies/</td><td>List all companies</td></tr>
    <tr><td>POST</td><td>/api/v1/companies/</td><td>Create a new company</td></tr>
    <tr><td>GET</td><td>/api/v1/companies/{id}/</td><td>Retrieve a specific company</td></tr>
    <tr><td>PUT</td><td>/api/v1/companies/{id}/</td><td>Update a specific company</td></tr>
    <tr><td>DELETE</td><td>/api/v1/companies/{id}/</td><td>Delete a specific company</td></tr>
    <tr><td>GET</td><td>/api/v1/companies/{id}/employees/</td><td>List employees in a company 🔥</td></tr>
  </table>

  <h3>👨‍💼 Employee</h3>
  <table border="1" cellpadding="8" cellspacing="0">
    <tr><th>Method</th><th>Endpoint</th><th>Description</th></tr>
    <tr><td>GET</td><td>/api/v1/employee/</td><td>List all employees</td></tr>
    <tr><td>POST</td><td>/api/v1/employee/</td><td>Create a new employee</td></tr>
    <tr><td>GET</td><td>/api/v1/employee/{id}/</td><td>Retrieve a specific employee</td></tr>
    <tr><td>PUT</td><td>/api/v1/employee/{id}/</td><td>Update a specific employee</td></tr>
    <tr><td>DELETE</td><td>/api/v1/employee/{id}/</td><td>Delete a specific employee</td></tr>
  </table>

  <h2>🧬 Models Overview</h2>

  <h3>🏢 Company</h3>
  <ul>
    <li>company_id: Auto-generated primary key</li>
    <li>name, location, about</li>
    <li>types: IT, Non IT, Mobile Phones</li>
    <li>active: Boolean</li>
    <li>added_time: Timestamp (auto-updated)</li>
  </ul>

  <h3>👨‍💼 Employee</h3>
  <ul>
    <li>name, email, address, phone, about</li>
    <li>position: Manager, Software Developer, Project Leader</li>
    <li>company: ForeignKey to Company</li>
  </ul>

  <h2>🔍 Custom Endpoint</h2>
  
<img width="1919" height="550" alt="Screenshot 2025-07-13 185228" src="https://github.com/user-attachments/assets/2e4c0626-c3eb-4294-aaf6-3e8006307e71" />  <br> <br>

  <pre>
GET /api/v1/companies/{company_id}/employees/
  </pre>
  <p>This returns all employees belonging to the specified company.</p>

  <h2>🧪 Testing the API</h2>
  <ul>
    <li>Run the server: http://127.0.0.1:8000/</li>
    <li>Admin Panel: http://127.0.0.1:8000/admin/</li>
    <li>Use Postman or Insomnia for API testing</li>
    <li>Or test via DRF's browsable interface</li>
  </ul>

  <h2>🚧 Future Improvements</h2>
  <ul>
    <li>[ ] Add JWT or token-based authentication</li>
    <li>[ ] Add pagination and filters</li>
    <li>[ ] Add Swagger / ReDoc documentation</li>
    <li>[ ] Add unit and integration tests</li>
    <li>[ ] Dockerize the project</li>
  </ul>

