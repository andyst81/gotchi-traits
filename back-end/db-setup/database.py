import sqlite3
import os
from pop_database import get_data

if os.path.exists('8ggdb.db'):
        os.remove('8ggdb.db')
        print('Old DB removed')
else:
        print('No DB file found')

if __name__ == '__main__':
  conn = sqlite3.connect('8ggdb.db')
  print("Opened database successfully")

  conn.execute('''CREATE TABLE IF NOT EXISTS GOTCHIS
          (ID          TEXT  PRIMARYKEY NOT NULL,
          NAME         TEXT  NOT NULL,
          HAUNTID      TEXT  NOT NULL,
          KIN          TEXT  NOT NULL,
          XP           TEXT  NOT NULL,
          OWNER        TEXT  NOT NULL,
          BRS          TEXT  NOT NULL,
          MBRS         TEXT  NOT NULL,
          SBRS         TEXT  NOT NULL,
          COLLATERAL   TEXT  NOT NULL,
          NRG          INT   NOT NULL,
          AGG          INT   NOT NULL,
          SPK          INT   NOT NULL,
          BRN          INT   NOT NULL,
          EYEC         INT   NOT NULL,
          EYES         INT   NOT NULL,
          NRGT         TEXT  NOT NULL,
          AGGT         TEXT  NOT NULL,
          SPKT         TEXT  NOT NULL,
          BRNT         TEXT  NOT NULL,
          EYECT        TEXT NOT NULL,
          EYEST        TEXT NOT NULL,
          MNRG         INT   NOT NULL,
          MAGG         INT   NOT NULL,
          MSPK         INT   NOT NULL,
          MBRN         INT   NOT NULL,
          MEYEC        INT   NOT NULL,
          MEYES        INT   NOT NULL,
          MNRGT        TEXT  NOT NULL,
          MAGGT        TEXT  NOT NULL,
          MSPKT        TEXT  NOT NULL,
          MBRNT        TEXT  NOT NULL,
          MEYECT       TEXT  NOT NULL,
          MEYEST       TEXT  NOT NULL,
          SNRG         INT   NOT NULL,
          SAGG         INT   NOT NULL,
          SSPK         INT   NOT NULL,
          SBRN         INT   NOT NULL,
          SEYEC        INT   NOT NULL,
          SEYES        INT   NOT NULL,
          SNRGT        TEXT  NOT NULL,
          SAGGT        TEXT  NOT NULL,
          SSPKT        TEXT  NOT NULL,
          SBRNT        TEXT  NOT NULL,
          SEYECT       TEXT  NOT NULL,
          SEYEST       TEXT  NOT NULL
          );''')
  print("Main gotchi table created successfully")

  conn.close()

  get_data()