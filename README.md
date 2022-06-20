# Awwwards Clone

> A clone of the popular web app Awwwards.

## :hammer: Built With

- HTML, CSS
- Python, Django, PostgreSQL

### :computer: Setup
To get a local copy up and running follow these simple example steps.

##### Cloning the repository:  
 ```bash 
git clone https://github.com/blancc-page/week9-awwwards-clone-app.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd week9-awwwards-clone-app 
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations awwwardsApp
 ``` 
 Now Migrate  
 ```bash 
python manage.py migrate 
```
##### Run the application  
 ```bash 
python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  


## :trollface: Authors

👤 **Moses Muta**

- GitHub: [@githubhandle](https://github.com/blancc-page)
- LinkedIn: [LinkedIn](<linkedIn link>)


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## :muscle: Show your support

    Please give a⭐️if you love this project.
    

## 📝 License

This project is [MIT](./MIT.md) licensed.
