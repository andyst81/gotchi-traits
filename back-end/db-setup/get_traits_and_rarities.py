def get_traits(traits):
  n = traits
  NRG = n[0]
  AGG = n[1]
  SPK = n[2]
  BRN = n[3]
  EYES = n[4]
  EYEC = n[5]

  return NRG, AGG, SPK, BRN, EYES, EYEC
    
def get_NRG(NRG):   
  if NRG <= 49:
    NRGT = 'CARRYING CAPACITY'
  elif NRG >= 50:
    NRGT = 'MOVEMENT SPEED'
  else:
    NRGT = ''
  NRGR = get_trait_rarity(NRG)
  return NRGR + " " + NRGT

def get_AGG(AGG):
  if AGG <= 49:
    AGGT = 'ARMOR'
  elif AGG >= 50:
    AGGT = 'MELEE DAMAGE'
  else:
    AGGT = ''
  AGGR = get_trait_rarity(AGG)
  return AGGR + " " + AGGT

def get_SPK(SPK):   
  if SPK <= 49:
    SPKT = 'HEALTH REGEN SPEED'
  elif SPK >= 50:
    SPKT = 'ETHEREALITY'
  else:
    SPKT = ''
  SPKR = get_trait_rarity(SPK)
  return SPKR + " " + SPKT

def get_BRN(BRN):
  if BRN <= 49:
    BRNT = 'ATTACK SPEED'
  elif BRN >= 50:
    BRNT = 'RANGED DAMAGE'
  else:
    BRNT = ''
  BRNR = get_trait_rarity(BRN)
  return BRNR + " " + BRNT

def get_EYEC(EYEC):
  if EYEC <= 49:
    EYECT = 'VISION RANGE'
  elif EYEC >= 50:
    EYECT = 'HANDLING'
  else:
    EYECT = ''
  EYECR = get_trait_rarity(EYEC)
  return EYECR + " " + EYECT

def get_EYES(EYES, haunt, collateral):
  if EYES == 0 and haunt == 1:
    EYEST = 'MORE MELEE ARMOR'
  elif EYES == 0 and haunt == 2:
    EYEST = 'MORE LIQUIDATOR DAMAGE'
  elif EYES == 1 and haunt == 1:
    EYEST = 'MORE MELEE DAMAGE'
  elif EYES == 1 and haunt == 2:
    EYEST = 'MORE EVASION'
  elif EYES >=2 and EYES <=4:
    EYEST = 'rare low 1 FASTER HEALTH REGEN'
  elif EYES>=5 and EYES <= 6:
    EYEST = 'rare low 2 SLOWER STAMINA USAGE'
  elif EYES >=7 and EYES <=9:
    EYEST = 'rare low 3 FASTER HEALTH REGEN and SLOWER STAMINA USAGE'
  elif EYES >=10 and EYES <=15:
    EYEST = 'uncommon low 1 MORE MELEE EVASION'
  elif EYES >=15 and EYES <= 19:
    EYEST = 'uncommon low 2 MORE RANGED EVASION'
  elif EYES >= 20 and EYES <=24:
    EYEST = 'uncommon low 3 MORE EVASION'
  elif EYES >= 25 and EYES <= 41:
    EYEST = 'common 1 MORE BASE DAMAGE'
  elif EYES >= 42 and EYES <= 57:
    EYEST = 'common 2 MORE BASE and MORE ATTACK DAMAGE'
  elif EYES >= 58 and EYES <= 74:
    EYEST = 'common 3 MORE MAX DAMAGE'
  elif EYES >= 75 and EYES <= 79:
    EYEST = 'uncommon high 1 MORE MELEE ATTACK SPEED'
  elif EYES >=80 and EYES <= 84:
    EYEST = 'uncommon high 2 MORE RANGED ATTACK SPEED'
  elif EYES >= 85 and EYES <= 89:
    EYEST = 'uncommon high 3 MORE ATTACK SPEED'
  elif EYES >= 90 and EYES <= 92:
    EYEST = 'rare high 1 MORE ROAD SPEED'
  elif EYES >= 93 and EYES <= 94:
    EYEST = 'rare high 2 MORE ALHEMICA SPEED'
  elif EYES >= 95 and EYES <= 97: 
    EYEST = 'rare high 3 MORE SPEED'
  elif EYES >= 98 and (collateral == 'maDAI' or collateral == 'amDAI'):
    EYEST = 'mythical MORE BASE DAMAGE'
  elif EYES >= 98 and (collateral == 'maAAVE' or collateral == 'amAAVE'):
    EYEST = 'mythical MORE RANGED EVASION'
  elif EYES >= 98 and collateral == 'maWETH':
    EYEST = 'mythical MORE VISION RANGE'
  elif EYES >= 98 and collateral == 'maLINK' :
    EYEST = 'mythical MORE ATTACK EVASION'
  elif EYES >= 98 and (collateral == 'maUSDC' or collateral == 'amUSDC'):
    EYEST = 'mythical MORE RANGED ARMOR'
  elif EYES >= 98 and collateral == 'maYFI':
    EYEST = 'mythical MORE ALCHEMICA SPEED'
  elif EYES >= 98 and collateral == 'maUNI':
    EYEST = 'mythical FASTER HEALTH REGEN'
  elif EYES >= 98 and collateral == 'maTUSD':
    EYEST = 'mythical MORE MAX DAMAGE'
  elif EYES >= 98 and collateral == 'amUSDT':
    EYEST = 'mythical MORE BASE + MAX DAMAGE'
  elif EYES >= 98 and collateral == 'amWETH':
    EYEST = 'mythical SLOWER STAMINA USAGE'
  elif EYES >= 98 and collateral == 'amWBTC':
    EYEST = 'mythical MORE MELEE EVASION'
  elif EYES >= 98 and collateral == 'amWMATIC':
    EYEST = 'mythical MORE ATTACK SPEED'
  else:
    EYEST = ':poop: THERE SEEMS TO HAVE BEEN AN ERROR :poop:'
  return EYEST

def get_trait_rarity(n):
  if n < 0 or n > 99:
    return 'godlike'
  elif n == 0 or n == 1 or n == 98 or n == 99:
    return 'mythical'
  elif (n >= 2 and n <= 9) or (n >= 91 and n <= 97):
    return "rare"
  elif (n >= 10 and n <= 24) or (n >= 75 and n <= 90):
    return 'uncommon'
  else:
    return 'common'