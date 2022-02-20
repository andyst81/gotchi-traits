import sqlite3

def get_gotchis_by_address(address):
  gotchis = []
  try:
    conn = sqlite3.connect('8ggdb.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM GOTCHIS where OWNER = '{address}' order by BRS DESC;")
    rows = cursor.fetchall()
    # convert row objects to dictionary
    for i in rows:
      gotchi = {}
      base = {}
      modified = {}
      sets = {}
      info = {}
      info['ID'] = i['ID']
      info['Owner'] = i['OWNER']
      gotchi['Name'] = i['NAME']
      info['XP'] = i['XP']
      info['Kinship'] = i['KIN']
      info['Haunt'] = i['HAUNTID']
      base['baseRarityScore'] = i['BRS']
      modified['modifiedRarityScore'] = i['MBRS']
      sets['withSetsRarityScore'] = i['SBRS']
      info['Collateral'] = i['COLLATERAL']
      base['Nrg'] = i['NRG']
      base['Agg'] = i['AGG']
      base['Spk'] = i['SPK']
      base['Brn'] = i['BRN']
      base['EyeColor'] = i['EYEC']
      base['EyeShape'] = i['EYES']
      base['NrgMapped'] = i['NRGT']
      base['AggMapped'] = i['AGGT']
      base['SpkMapped'] = i['SPKT']
      base['BrnMapped'] = i['BRNT']
      base['EyeColorMapped'] = i['EYECT']
      base['EyeShapeMapped'] = i['EYEST']
      modified['Nrg'] = i['MNRG']
      modified['Agg'] = i['MAGG']
      modified['Spk'] = i['MSPK']
      modified['Brn'] = i['MBRN']
      modified['EyeColor'] = i['MEYEC']
      modified['EyeShape'] = i['MEYES']
      modified['NrgMapped'] = i['MNRGT']
      modified['AggMapped'] = i['MAGGT']
      modified['SpkMapped'] = i['MSPKT']
      modified['BrnMapped'] = i['MBRNT']
      modified['EyeColorMapped'] = i['MEYECT']
      modified['EyeShapeMapped'] = i['MEYEST']
      sets['Nrg'] = i['SNRG']
      sets['Agg'] = i['SAGG']
      sets['Spk'] = i['SSPK']
      sets['Brn'] = i['SBRN']
      sets['EyeColor'] = i['SEYEC']
      sets['EyeShape'] = i['SEYES']
      sets['NrgMapped'] = i['SNRGT']
      sets['AggMapped'] = i['SAGGT']
      sets['SpkMapped'] = i['SSPKT']
      sets['BrnMapped'] = i['SBRNT']
      sets['EyeColorMapped'] = i['SEYECT']
      sets['EyeShapeMapped']  = i['SEYEST']
      
      info['baseStats'] = base
      info['modifiedStats'] = modified
      info['withSetStats'] = sets
      gotchi['info'] = info
      gotchis.append(gotchi)
  except Exception as e:
    print(e)

  return gotchis


def get_gotchi_by_id(gotchi_id):
  gotchi = {}
  try:
    conn = sqlite3.connect('8ggdb.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM GOTCHIS WHERE ID = {gotchi_id};")
    row = cursor.fetchone()
    gotchi = {}
    gotchi['ID'] = row['ID']
    gotchi['OWNER'] = row['OWNER']
    gotchi['NAME'] = row['NAME']
    gotchi['HAUNTID'] = row['HAUNTID']
    gotchi['BRS'] = row['BRS']
    gotchi['MBRS'] = row['MBRS']
    gotchi['SBRS'] = row['SBRS']
    gotchi['COLLATERAL'] = row['COLLATERAL']
    gotchi['NRG'] = row['NRG']
    gotchi['AGG'] = row['AGG']
    gotchi['SPK'] = row['SPK']
    gotchi['BRN'] = row['BRN']
    gotchi['EYEC'] = row['EYEC']
    gotchi['EYES'] = row['EYES']
    gotchi['NRGT'] = row['NRGT']
    gotchi['AGGT'] = row['AGGT']
    gotchi['SPKT'] = row['SPKT']
    gotchi['BRNT'] = row['BRNT']
    gotchi['EYECT'] = row['EYECT']
    gotchi['EYEST'] = row['EYEST']
    gotchi['MNRG'] = row['MNRG']
    gotchi['MAGG'] = row['MAGG']
    gotchi['MSPK'] = row['MSPK']
    gotchi['MBRN'] = row['MBRN']
    gotchi['MEYEC'] = row['MEYEC']
    gotchi['MEYES'] = row['MEYES']
    gotchi['MNRGT'] = row['MNRGT']
    gotchi['MAGGT'] = row['MAGGT']
    gotchi['MSPKT'] = row['MSPKT']
    gotchi['MBRNT'] = row['MBRNT']
    gotchi['MEYECT'] = row['MEYECT']
    gotchi['MEYEST'] = row['MEYEST']
    gotchi['SNRG'] = row['SNRG']
    gotchi['SAGG'] = row['SAGG']
    gotchi['SSPK'] = row['SSPK']
    gotchi['SBRN'] = row['SBRN']
    gotchi['SEYEC'] = row['SEYEC']
    gotchi['SEYES'] = row['SEYES']
    gotchi['SNRGT'] = row['SNRGT']
    gotchi['SAGGT'] = row['SAGGT']
    gotchi['SSPKT'] = row['SSPKT']
    gotchi['SBRNT'] = row['SBRNT']
    gotchi['SEYECT'] = row['SEYECT']
    gotchi['SEYEST']  = row['SEYEST'] 
  except:
    gotchi = {}

  return gotchi