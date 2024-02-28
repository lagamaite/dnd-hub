// Filename - Map.js

import React, {useState} from 'react'
import "./Maps.css"


const Maps = () => {
  const [selectedImage, setSelectedImage] = useState('Black_Desert.png');

  const handleImageChange = (event) => {
    setSelectedImage(event.target.value);
  };

  return (
    <div className='Map'>
        <header className='Map-Header'>

        <h1>Maps</h1>
        <div>
          <label htmlFor="imageDropdown">Select Map: </label>
          <select id="imageDropdown" value={selectedImage} onChange={handleImageChange}>
            <option value="Black_Desert.png">Black Desert</option>
            <option value="Ivory_Desert.png">Ivory Desert</option>
          </select>
        </div>
        <picture>
          <img className='Map-Image' src={require(`../Images/${selectedImage}`)} alt="" />
        </picture>
        </header>
    </div>
  )
}

export default Maps