# PassManager

This project is a simple password manager written in Python for Terminal. It allows users to register, log in, and store/retrieve their credentials securely.
## Features

- Triple-Layer password storage encryption
- Undecryptable hashing protection
- Easy to use GUI


## Installation

### Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.6 or later installed on your machine.
Git installed on your machine.

### Clone the Repository
First, clone the repository to your local machine using Git.

```bash
git clone https://github.com/yourusername/PassManager.git
cd PassManager
```
### Set Up a Virtual Environment (Optional but Recommended)
It is recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install Dependencies
Install the necessary dependencies using `pip`.

```bash
pip install hashlib maskpass keyring
```
### Running the Script
Once the dependencies are installed, you can run the script.

```bash
python passmanager.py
```
## Usage/Examples

- Register: Create a new user account.
- Sign In: Log into your existing account.
- Enter: Store a new credential.
- Find: Retrieve stored credentials.
- Exit: Exit the application.
## Acknowledgements

 - [hashlib](https://docs.python.org/3/library/hashlib.html)
 - [maskpass](https://pypi.org/project/maskpass/)
 - [keyring](https://pypi.org/project/keyring/)


## Authors

- [@areyougoodbro](https://github.com/areyougoodbro)


## License

[MIT](https://github.com/areyougoodbro/PassManager/blob/master/LICENSE)

