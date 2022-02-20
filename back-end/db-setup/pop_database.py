from collaterals import colls
import requests
import sqlite3

from get_traits_and_rarities import get_traits, get_NRG, get_AGG, get_SPK, get_BRN, get_EYES, get_EYEC

def set_functions():
  base_url = 'https://api.thegraph.com/subgraphs/name/aavegotchi/aavegotchi-core-matic'
  conn = sqlite3.connect('8ggdb.db')

  return base_url, conn

def get_top_brs():
  base_url, conn = set_functions()

  query = """
  {
    aavegotchis (first: 1, orderBy: baseRarityScore, orderDirection: desc, where:{baseRarityScore_not: 0})
    {
      baseRarityScore
    }
  } 
  """

  response = requests.post(base_url, json={'query': query})
  raw_data = response.json()
  top_brs = raw_data['data']['aavegotchis'][0]['baseRarityScore']
  
  return top_brs

def get_bottom_brs():
  base_url, conn = set_functions()

  query = """
  {
    aavegotchis (first: 1, orderBy: baseRarityScore, orderDirection: asc, where:{baseRarityScore_not: 0})
    {
      baseRarityScore
    }
  } 
  """

  response = requests.post(base_url, json={'query': query})
  raw_data = response.json()
  bottom_brs = raw_data['data']['aavegotchis'][0]['baseRarityScore']
  
  return bottom_brs


def get_data():
  base_url, conn = set_functions()
  bottom_brs = get_bottom_brs()
  top_brs = get_top_brs()

  #set query for The Graph quary
  query = """ 
  query getGotchis($bottom_brs: Int, $top_brs: Int, $skip: Int)
    {
      aavegotchis (
        first:1000, 
        skip: $skip, 
        orderBy: baseRarityScore,
        orderDirection: asc
        where: {
          baseRarityScore_gte: $bottom_brs, 
          baseRarityScore_lte: $top_brs
        })
      {
        id
        owner {
          id
        }
        name
        collateral
        hauntId
        kinship
        experience
        baseRarityScore
        modifiedRarityScore
        withSetsRarityScore
        numericTraits
        modifiedNumericTraits
        withSetsNumericTraits
      }
    }
  """

  while int(bottom_brs) < int(top_brs):

    variables = {'bottom_brs': int(bottom_brs), 'top_brs': int(top_brs), 'skip': 0}  ##### brs_gte highest brs of last pull

    #pull data from The Graph
    response = requests.post(base_url, json={'query': query, 'variables': variables})
    raw_data = response.json()
    # print(raw_data)
    if raw_data['data']['aavegotchis']:
      data = raw_data['data']['aavegotchis']
      #print(data)
      for d in data:
        id = d['id']
        owner = d['owner']['id']
        name = d['name']
        hauntId = d['hauntId']
        kin = d['kinship']
        xp = d['experience']
        brs = d['baseRarityScore']
        mbrs = d['modifiedRarityScore']
        sbrs = d['withSetsRarityScore']
        
        collateral = colls.get(d['collateral'])
        nrg, agg, spk, brn, eyes, eyec = get_traits(d['numericTraits'])
        mnrg, magg, mspk, mbrn, meyes, meyec = get_traits(d['modifiedNumericTraits'])
        snrg, sagg, sspk, sbrn, seyes, seyec = get_traits(d['withSetsNumericTraits'])

        nrgt = get_NRG(nrg)
        aggt = get_AGG(agg)
        spkt = get_SPK(spk)
        brnt = get_BRN(brn)
        eyest = get_EYES(eyes, hauntId, collateral)
        eyect = get_EYEC(eyec)

        mnrgt = get_NRG(mnrg)
        maggt = get_AGG(magg)
        mspkt = get_SPK(mspk)
        mbrnt = get_BRN(mbrn)
        meyest = get_EYES(meyes, hauntId, collateral)
        meyect = get_EYEC(meyec)

        snrgt = get_NRG(snrg)
        saggt = get_AGG(sagg)
        sspkt = get_SPK(sspk)
        sbrnt = get_BRN(sbrn)
        seyest = get_EYES(seyes, hauntId, collateral)
        seyect = get_EYEC(seyec)

        if collateral != None:
          conn.execute("INSERT OR REPLACE INTO GOTCHIS (ID, OWNER, NAME, HAUNTID, KIN, XP, BRS, MBRS, SBRS, \
            COLLATERAL, NRG, AGG, SPK, BRN, EYEC, EYES, NRGT, AGGT, SPKT, BRNT, EYECT, EYEST, \
            MNRG, MAGG, MSPK, MBRN, MEYEC, MEYES, MNRGT, MAGGT, MSPKT, MBRNT, MEYECT, MEYEST, \
            SNRG, SAGG, SSPK, SBRN, SEYEC, SEYES, SNRGT, SAGGT, SSPKT, SBRNT, SEYECT, SEYEST ) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
            (id, owner, name, hauntId, kin, xp, brs, mbrs, sbrs, collateral,  \
            nrg, agg, spk, brn, eyec, eyes, nrgt, aggt, spkt, brnt, eyect, eyest, \
            mnrg, magg, mspk, mbrn, meyec, meyes, mnrgt, maggt, mspkt, mbrnt, meyect, meyest,\
            snrg, sagg, sspk, sbrn, seyec, seyes, snrgt, saggt, sspkt, sbrnt, seyect, seyest))
          conn.commit()
          print (brs, id)
    
    cursor = conn.execute("SELECT BRS FROM GOTCHIS ORDER BY BRS DESC LIMIT 1")
    for row in cursor:
      bottom_brs = row[0]
    print(bottom_brs)
  conn.close()






if __name__ == '__main__':
  get_data()