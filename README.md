<p align="center">
  <img width="620" src="public/opportunity-logo.png" alt="Opportunity Logo">
</p>

# opPORTunity :ship:
[CHAMPION :trophy:] PSA Code Sprint Hackathon 2023 <br>

 <img width="400" src="public/cert.png" alt="Certificate">
https://www.psacodesprint.com/code-sprint-2023

## About :blue_book:
opPORTunity is a synergistic HR transformation portal that leverages the power of data, AI, and HR and has three key features: Talent, Experience, and Engagement. 

#### PortBOT :robot: [Talent]
<img width="400" src="public/portbot.gif" alt="PortBot GIF">
A dynamic virtual assistant that offers instantaneous support and conducts efficient resume reviews for potential candidates Within an organization, PortBot functions as a comprehensive internal knowledge hub for employees. <br>
[External Demo](https://port-bot.streamlit.app/) |
[Internal Demo](https://portbot-int.streamlit.app/) <br>
Note: Demos will be in sleep mode after a period of inactivity; notify me if you wish to try them out.

#### LightHouse :bulb: [Experience]
<img width="400" src="public/lighthouse.gif" alt="LightHouse GIF">
LightHouse utilizes AI-driven talent matching and dynamic skill profiling to personalize development roadmaps for each individual. Each team member receives tailored advice for their career growth.

#### PortConnections 🚢 [Engagement] 
<img width="400" src="public/portconnections.gif" alt="PortConnections GIF">
Fostering engagement through the use of an AI recommendation engine to match employees and have them participate in diverse, budget-friendly activities that encourage cross-departmental connectivity. These activities are generated by matching the preferences of the group of matched employees.

### Team Members :busts_in_silhouette:

- [Xavier Koo](https://github.com/xavierkoo)
- [Aaron Kwah](https://github.com/A2ron-k)
- [Ray Quek](https://github.com/rayquekCW)
- [Maurice Ho](https://github.com/HZKmaurice)

## Tech Stack
- Vue.js
- StreamLit
- FastAPI
- LangChain
- ChromaDB
- OpenAI API

## Setup
In this section, these are the steps required to setup opPORTunity locally to try it out. Note that PortBot demos can be accessed via the links mentioned above.

### Steps
1. Create `.env` file at the root directory:
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

2. Go to the server directory:
```
python3 -m venv venv
source venv/bin/activate #For windows: venv\Scripts\activate.bat
pip install -r requirements.txt
```

3. Exit virtual environment by using a new terminal

4. Go to Root directory
5. Run Docker: <br>
* First build the image:
```
docker-compose build
```
* When ready, run it:
```
docker-compose up
```
* Close docker
```
docker-compose down -v
```

6. To run frontend locally, at the client directory:
```
npm install
```
```
npm run dev
```
