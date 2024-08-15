import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  // Initialize state to store products
  const [products, setProducts] = useState([]);

  // Function to fetch products from the backend
  const fetchProducts = async () => {
    try {
      const response = await axios.get('http://localhost:5555/product'); // Replace with your backend URL
      setProducts(response.data); // Update state with fetched products
    } catch (error) {
      console.error('Error fetching products:', error.response ? error.response.data : error.message);
    }
  };

  // Use useEffect to fetch products when the component mounts
  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <>
      <h1>Products</h1>
      <div className="card">
        {products.length > 0 ? (
          products.map((product) => (
            <div key={product.id} className="product">
              <h2>{product.title}</h2>
              <p>Price: ${product.price}</p>
              {product.image_url && <img src={product.image_url} alt={product.title} />}
            </div>
          ))
        ) : (
          <p>No products available</p>
        )}
        <p>Get all you require with a call</p>
      </div>
      <p className="read-the-docs">Trusted retailer</p>
    </>
  );
}

export default App;
