--
-- File generated with SQLiteStudio v3.4.3 on Sun Mar 12 21:22:25 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Documents
CREATE TABLE IF NOT EXISTS Documents (DocumentID INTEGER PRIMARY KEY AUTOINCREMENT, UserID INTEGER REFERENCES Users (UserID) ON UPDATE SET DEFAULT, DocType TEXT,DocName TEXT, Summary TEXT, PagesNum INTEGER, StanzaNum INTEGER);

-- Table: Keywords
CREATE TABLE IF NOT EXISTS Keywords (keywordID INTEGER PRIMARY KEY AUTOINCREMENT, ParaID INTEGER REFERENCES Paragraphs (ParaID), Keyword TEXT);

-- Table: Paragraphs
CREATE TABLE IF NOT EXISTS Paragraphs (ParaID INTEGER PRIMARY KEY AUTOINCREMENT, DocID INTEGER REFERENCES Documents (DocID), SentenceNum INTEGER, SentimentScore REAL, ParaText TEXT);

-- Table: Users
CREATE TABLE IF NOT EXISTS Users (UserID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Email TEXT, DocNum NUMERIC);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
