#establishing connection with the database: We are using a POSTGRES database with the pgvector extension.
# Connects to a PostgreSQL database, retrieves and prints database version, tables, and contents of 'metadata' and 'chunks' tables.

import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="vector_db",    
            user="postgres",        
            password="root123",     
            host="localhost",       
            port="5432"             
        )
        cursor = connection.cursor()
    
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Connected to PostgreSQL database! Database version: {db_version[0]}")
        # cursor.close()
        # connection.close()
        
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables
            WHERE table_schema = 'public';
        """)
        
        tables = cursor.fetchall()
        
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")
            
        print("\nContents of the 'metadata' table:")
        cursor.execute("SELECT * FROM metadata;")
        metadata_rows = cursor.fetchall()
        for row in metadata_rows:
            print(row)

        print("\nContents of the 'chunks' table:")
        cursor.execute("SELECT * FROM chunks;")
        chunks_rows = cursor.fetchall()
        for row in chunks_rows:
            print(row)
        
        cursor.close()
        connection.close()
              
        
    except Exception as error:
        print(f"Error: Could not connect to the PostgreSQL database: {error}")
        
        

connect_to_db()
