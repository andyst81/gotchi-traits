import { useEffect, useState } from 'react';
import axios from 'axios';


const Gotchis = (props) => {
  const [gotchis, setGotchis] = useState([]);
  const [error, setError] = useState(false);
  const fetchData = async () => {
    await axios.get(`http://23.234.216.147:8080/api/users/${props.address}`)
      .then(res => {
        setError(false);
        setGotchis(prevState => [...prevState, ...res.data]);
      })
      .catch(() => {
        setError(true);
      })
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>

      <h2 className='text-2xl text-center mb-2'>List of Gotchis</h2>
      {error && <div>There was an error.</div>}
      {!error && gotchis && (
        <div>
        {gotchis.map((gotchi, key) => (
          <div key={key}>
              <div className="grid sm:grid-cols-1 md:grid-cols-2 border">
                <div>
                  <p>Name: {gotchi.Name}</p>
                  <p>ID: {gotchi.info.ID}</p>
                  <p>Haunt: {gotchi.info.Haunt}</p>
                  <p>Experience: {gotchi.info.XP}</p>
                  <p>Kinship: {gotchi.info.Kinship}</p>
                  <p>Rarity Score: { props.traits === 'baseStats' ? 
                  gotchi.info.baseStats.baseRarityScore :
                  props.traits === 'modifiedStats' ? gotchi.info.modifiedStats.modifiedRarityScore :
                  gotchi.info.withSetStats.withSetsRarityScore }
                  </p>
                </div>
                <div>
                  <p>Energy: { props.traits === 'baseStats' ? (gotchi.info.baseStats.Nrg, gotchi.info.baseStats.NrgMapped) :
                  props.traits === 'modifiedStats' ? (gotchi.info.modifiedStats.Nrg, gotchi.info.modifiedStats.NrgMapped) :
                  (gotchi.info.withSetStats.Nrg, gotchi.info.withSetStats.NrgMapped) }</p>
                  <p>Aggression: { props.traits === 'baseStats' ? (gotchi.info.baseStats.Agg, gotchi.info.baseStats.AggMapped) :
                  props.traits === 'modifiedStats' ? (gotchi.info.modifiedStats.Agg, gotchi.info.modifiedStats.AggMapped) :
                  (gotchi.info.withSetStats.Agg, gotchi.info.withSetStats.AggMapped) }</p>
                  <p>Brain Size:  { props.traits === 'baseStats' ? (gotchi.info.baseStats.Brn, gotchi.info.baseStats.BrnMapped) :
                  props.traits === 'modifiedStats' ? (gotchi.info.modifiedStats.Brn, gotchi.info.modifiedStats.BrnMapped) :
                  (gotchi.info.withSetStats.Brn, gotchi.info.withSetStats.BrnMapped) }</p>
                  <p>Spookiness:  { props.traits === 'baseStats' ? (gotchi.info.baseStats.Spk, gotchi.info.baseStats.SpkMapped) :
                  props.traits === 'modifiedStats' ? (gotchi.info.modifiedStats.Spk, gotchi.info.modifiedStats.SpkMapped) :
                  (gotchi.info.withSetStats.Spk, gotchi.info.withSetStats.SpkMapped) }</p>
                  <p>Eye Shape: { props.traits === 'baseStats' ? (gotchi.info.baseStats.EyeShape, gotchi.info.baseStats.EyeShapeMapped) :
                  props.traits === 'modifiedStats' ? (gotchi.info.modifiedStats.EyeShape, gotchi.info.modifiedStats.EyeShapeMapped) :
                  (gotchi.info.withSetStats.EyeShape, gotchi.info.withSetStats.EyeShapeMapped) }</p>
                  <p>Eye Color: { props.traits === 'baseStats' ? (gotchi.info.baseStats.EyeColor, gotchi.info.baseStats.EyeColorMapped) :
                  props.traits === 'modifiedStats' ? (gotchi.info.modifiedStats.EyeColor, gotchi.info.modifiedStats.EyeColorMapped) :
                  (gotchi.info.withSetStats.EyeColor, gotchi.info.withSetStats.EyeColorMapped) }</p>
                </div>
              </div>
          </div>
        ))}
      </div>
      )}
    </div>
  );
};

export default Gotchis;