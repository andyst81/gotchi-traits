import WalletForm from '../src/components/WalletForm.js'

export default function Home() {
  return (
    <div className='container mx-auto py-4'>
      <h1 className='text-center text-3xl font-press-start'>
        Aavegotchi Traits Analyser
      </h1>
      <WalletForm />
    </div>
  )
}