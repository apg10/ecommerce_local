import { renderHook, act } from '@testing-library/react';
import { CartProvider, useCart } from '../context/CartContext';

const wrapper = ({ children }) => (
  <CartProvider>{children}</CartProvider>
);

test('adds and removes items', () => {
  const { result } = renderHook(() => useCart(), { wrapper });
  act(() => result.current.addItem({ id: 1, name: "Test", price: 10 }));
  expect(result.current.items).toHaveLength(1);
  act(() => result.current.removeItem(1));
  expect(result.current.items).toHaveLength(0);
});
