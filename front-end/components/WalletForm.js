import React from 'react'
import Gotchis from '../components/PullGotchis.js'
import { useState } from 'react';


export function WalletForm() {
  const [address, setAddress] = useState("")
  const [traits, setTraits] = useState('baseStats')


  return (
    <div>
      <form className="w-full max-w-md py-6">
      <div className="flex items-center border-b border-blue-700 min-w-full">
        <input className="appearance-none bg-transparent border-none min-w-full text-blue-700" 
          type="text" 
          placeholder="Wallet Address" 
          ariaLabel="Wallet Address"
          value={address}
          onChange={e => setAddress(e.target.value)}
        />
      </div>
    </form>
    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mx-2 rounded-full"
      onClick={() => setTraits('baseStats')}>
        Base Stats
      </button>
      <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mx-2 rounded-full"
      onClick={() => setTraits('modifiedStats')}>
        With Wearables
      </button>
      <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mx-2 rounded-full"
      onClick={() => setTraits('withSetStats')}>
        With Bonuses
      </button>
    { address ? <Gotchis address={address} traits={traits}/> : null }

  </div>
  );
}


export default WalletForm