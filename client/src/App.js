import React, { useState, useEffect } from 'react';
import './App.css'

function App() {
  const [data, setData] = useState([]);
  const [previousProducts, setPreviousProducts] = useState([]);

  const sendNotification = (newProducts) => {
    if (Notification.permission === 'granted') {
      newProducts.forEach(product => {
        new Notification(`New Product Added: ${product.title}`);
      });
    } else {
      console.warn('Notifications not allowed!')
    }
  }

  useEffect(() => {
    const checkForNewProducts = (currentProducts) => {
      if (previousProducts.length === 0) {
        setPreviousProducts(currentProducts);
      } else {
        const newProducts = currentProducts.filter(product => !previousProducts.some(prev => prev.title === product.title));
  
        if (newProducts.length > 0){
          sendNotification(newProducts);
        }
        setPreviousProducts(currentProducts);
      }
    }

    fetch("/members")
      .then(res => res.json())
      .then(data => {
        setData(data.product);
        checkForNewProducts(data.product);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, [previousProducts]);

  return (
    <div className="App">
      <h1>Product List</h1>
      <ul>
        {data.map((product, index) => (
          <li class="productList" key={index}>
            <h2>{product.title}</h2>
            <p>Price: ${product.price}</p>
            <p>Discount: {product.discount}</p>
            <p>Link: <a href={product.source}>{product.source}</a></p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
