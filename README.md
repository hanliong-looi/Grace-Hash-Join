# Grace-Hash-Join

## Cloning the repository
Go to the desired folder and clone the repository
```
git clone https://github.com/hanliong-looi/Grace-Hash-Join.git
cd Grace-Hash-Join
```

## Downloading the database data
Due to limited file sizes in the repository, download the zipped data files for the database from this link instead: 
https://drive.google.com/file/d/1NfXb829W4vL4Ltzz1k-i_9N_wEM4U271/view?usp=sharing

Extract the data files from the zipped folder and navigate to scripts/populate_tables.txt
Change the file path in {{your data filepath}} to the file path that your extracted data files are located at

## Setting up PostgreSQL database
### Installing PostgreSQL
If you have not done so, you can install PostgreSQL from https://www.postgresql.org/download/
* Note: The host address and port that this project is using is 127.0.0.1 and 5432

### Creating the database
Once PSQL has been set up, create a database named "TPC-H" with the user "postgres". The password will be the password that you used during the setup process
```
createdb -U postgres TPC-H
```

Connect to the database
``` 
psql -U postgres -d TPC-H
```

### Creating the tables
From the repository, navigate to scripts/create_tables.txt.
Copy the entire code from the text file and run it on your PSQL terminal

You can check if the tables have been created by running the following command in the terminal
```
/d
```

### Populating the tables
Populate each of the table by copying the code from scripts/populate_tables.txt. Ensure that the file path has already been changed in the previous step

You can check if the tables have been successfully populated by running a sample SQL query, for example
```
SELECT *
FROM nation
LIMIT 5;
```

## Installing python libraries
In a separate terminal, navigate to the source code's directory
```
pip install -r requirements.txt
```

## Running the application
To start the application, run the following line
```
python interface.py
```
