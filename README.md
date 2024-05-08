# Secret manager project

## (0-step) Configuration environment

Create a virtual environment 

~~~
python -m venv venv
~~~


Activate vitural environment

```
# BASH
source venv/Scripts/activate

# CMD
.\venv\Scripts\activate
```

Install python dependencies

~~~
pip install -r requirements.txt
~~~

## Execute program

~~~
flask --app secret_manager.app run --debug
~~~