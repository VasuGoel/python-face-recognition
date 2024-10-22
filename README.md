# Python Face Recognition

Face recognition application built using world's simplest facial recognition API for Python and the Command Line. 

## Getting Started

Start by either downloading the zip file or clone with HTTPS.

### Prerequisites

* Anaconda Distribution (https://www.anaconda.com/distribution/)
* Python 3.7.3 (https://www.python.org/downloads/)

## Running

### Steps to play with application via terminal (on Mac or Linux)

#### 1. Clone the repository

```
git clone https://github.com/VasuGoel/python-face-recognition.git
```

#### 2. Unzip and change directory

* After cloning, double-click to unzip the project. After unzipping, type

```
cd ~/Downloads/python-face-recognition-master/
```

#### 3. Create and activate a virtual environment

* Create a virtual environment to pip install face_recognition package and several dependencies inside that virtual environment

```
pip install virtualenv
virtualenv virtual_env
```

* Activate the virtual environment 'virtual_env', which can be located inside the python-face-recognition-master folder root

```
source virtual_env/bin/activate
```

* Install face_recognition and its dependencies

```
pip install face_recognition
```

#### 4. Run a face recognition match on people in img/known/ and img/unknown/

* Put labelled images of known people in 'img/known/'
* To run a match of face_recognition on unknown people, put them inside 'img/unknown'

```
face_recognition ./img/known ./img/unknown
```

#### 5. Adjust tolerance

* If you don't get the expected results and get a match on known and unknown that is not correct, then first check out the distance or basically how much of a match it is.

```
face_recognition --show-distance true ./img/known ./img/unknown
```

* Check out the distance against that unknown picture and adjust the tolerance to get 'unknown person' on that falsely matched picture.

```
face_recognition --tolerance some_value ./img/known ./img/unknown
```

#### 6. Get only the names

* To only get the names of the poeple inside the unknown folder type,

```
face_recognition ./img/known ./img/unknown | cut -d ',' -f2
```

## Built With

* [Python] (https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.
* [face_recognition] (https://github.com/ageitgey/face_recognition) - The world's simplest facial recognition api for Python and the command line

## Authors

* **Vasu Goel** (https://github.com/VasuGoel)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/VasuGoel/python-face-recognition/blob/master/LICENSE) file for details
