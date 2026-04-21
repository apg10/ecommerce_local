import { render, screen } from '@testing-library/react';
import ProductList from '../pages/ProductList';
import { CartProvider } from '../context/CartContext';
import { BrowserRouter } from 'react-router-dom';

test('renders product list', async () => {
  render(
    <BrowserRouter>
      <CartProvider>
        <ProductList />
      </CartProvider>
    </BrowserRouter>
  );
  expect(await screen.findByText(/Products/i)).toBeInTheDocument();
});
