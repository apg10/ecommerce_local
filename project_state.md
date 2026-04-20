# Backend Development Plan
## 1. Authentication & Permissions
- Add Django Rest Framework SimpleJWT.
- Configure settings.py (add REST_FRAMEWORK & SIMPLE_JWT).
- Create login, refresh endpoints.
- Secure all endpoints except public listings.

## 2. Cart & Checkout Flow
- Model: Cart (one per user session), CartItem linked to Variant.
- API: CartViewSet (retrieve, add, update, delete items).
- Checkout endpoint: create Order from Cart, calculate totals.
- Order status workflow (created → paid → shipped).

## 3. Payment Integration
- Service layer for PayU SDK.
- Create webhook endpoint to receive payment status.
- Update Order & Payment models accordingly.
- Validation of provider/reference.

## 4. API Enhancements
- Expand Product API to include variants, inventory.
- Add filtering, pagination, search.
- Implement order creation validation, stock reservation.

## 5. Admin Customization
- Register models with Django admin.
- List filters, search fields, inline editing for Order Items.

## 6. Testing & Quality
- Write unit tests for models, serializers, views.
- Test payment webhook flow.
- Lint with flake8, format with black.

## 7. Deployment & CI
- Update Dockerfile to include Celery worker.
- Add docker-compose services for Celery & Redis.
- Create CI workflow to run tests and lint.

# Frontend Development Plan
## 1. Project Setup
- Initialize Vite/React or Next.js project in frontend/.
- Configure TypeScript, ESLint, Prettier.
- Install axios, react-router-dom.

## 2. UI Components
- Product list, product detail, cart sidebar.
- Checkout form (guest checkout).
- Payment confirmation page.
- Admin panel placeholder (later, maybe VueAdmin).

## 3. API Integration
- Create service layer for API calls (auth, products, cart, orders).
- Implement authentication token storage (localStorage).
- Handle API errors globally.

## 4. State Management
- Use React Context or Zustand for cart state.
- Persist cart to localStorage for guest users.

## 5. Routing & Navigation
- Routes: /, /products, /product/:id, /cart, /checkout, /login.
- Protected routes for user account (future).

## 6. Styling & Responsiveness
- Use Tailwind CSS.
- Mobile‑first layout.
- Ensure accessibility (ARIA labels).

## 7. Testing & Quality
- Unit tests with Jest + React Testing Library.
- E2E tests with Cypress.
- Lint with ESLint, format with Prettier.

## 8. Deployment
- Dockerfile for frontend.
- Update docker-compose to build and run frontend.
- CI workflow for lint, tests, build.