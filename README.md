# by-the-sea

Youtube Video URL: https://youtu.be/R6bQ5pLVFfU<br>
PortBOT URL: <br>
https://port-bot.streamlit.app/ <br>
https://portbot-int.streamlit.app/

## Tech Stack
- Vue.js
- StreamLit
- FastAPI
- LangChain
- ChromaDB
- OpenAI API

### Create `.env` file at the root directory:
```
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=bts_db_mysql
MYSQL_USER=bts_user
MYSQL_PASSWORD=bts_password
PHPADMIN_HOST=bts_db_mysql
PHPADMIN_USER=bts_user
PHPADMIN_PASSWORD=bts_password
OPENAI_API_KEY= ***OpenAI API key***
```
## Setup
### 1. Go to the server directory:
```
python3 -m venv venv
source venv/bin/activate #For windows: venv\Scripts\activate.bat
pip install -r requirements.txt
```

### 2. Exit virtual environment by using a new terminal

### 3. Go to Root directory
### 4. Run Docker:
First build the image:
```
docker-compose build
```
When ready, run it:
```
docker-compose up
```
Close docker
```
docker-compose down -v
```

### 5. To run frontend locally, at the client directory:
```
npm install
```
```
npm run dev
```
