Simple backend application that provides an API for a dashboard which
allows a planner to get insights into client and planning information.

The corresponding data that needs to be imported into the database is in 
`planning.json`, which contains around 10k records.


## Setup
1. Before installing the dependencies it is recommended to set up virtual environment 

    ```
   virtualenv .venv
   source .venv/bin/activate
   ```
2. Install the dependencies

    ```
    pip install -r requirements.txt
    ```

3. Initialize DB
   ```
   python init_db.py
   ```

4. Run service
   
   ```
   python main.py
   ```
