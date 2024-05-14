import React, {useState, useEffect} from 'react'

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {

    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
      <div>
        {Object.keys(data).length === 0 ? (
          <p>Loading....</p>
        ) : (
          <div>
            <p>Item Name: {data['item-name']}</p>
            <p>Item Price: {data['item-price']}</p>
          </div>
        )}

      </div>
  )
}

export default App