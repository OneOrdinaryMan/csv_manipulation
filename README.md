# CSV manipulation
This will convert the raw csv files to ordered csv by year.
# Virtual Enviroinment
Make sure to use venv while running the file to avoid any conflicts and errors.
In Unix Enviroinments,
```
python3 -m venv venv
source ./venv/bin/activate
```
In Windows enviroinments,
```
python -m venv venv
.\venv\Scripts\activate
```
# Installing the dependencies
This package uses following dependencies,
- chardet [For auto detecting encoding and avoiding read errors ].
- pandas [For numericals]

To install the dependencies use,
```
python3 -m pip install -r requirements.txt # for unix
python -m pip install -r requirements.txt # for windows
```
# Running the app
Make sure the directory you're running the app is the working directory of the code.

```
python3 -m app #for unix
python -m app #for windows
```
# License
This project is under MIT License.
