import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://zifcppbxexzolo:e3010b16e511b7eaa5ecf81c2f52b8e07582f937c8d50745d8a07054066f5a10@ec2-23-21-106-241.compute-1.amazonaws.com:5432/d72n20v43tptqd")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    first=True
    try:
        query = ""
        for isbn, title, author, year in reader:
            if first:
                first = False
            else:
                title = title.replace("'", "''")
                author = author.replace("'", "''")
                query = f"INSERT INTO books (isbn, title, author, year) VALUES ('{isbn}', '{title}', '{author}', {year})"
                db.execute(query)
                print(f"Added book isbn: {isbn}, title: {title}, author: {author}, year: {year}.")
        db.commit()
    except:
        print(f"error in query: {query}")

if __name__ == "__main__":
    main()
