import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session'
import reviewsReducer from './review';
import restaurantReducer from './restaurant'
import dishReducer from './dish';
import orderReducer from './order'
import orderDishReducer from './order_dish';


const rootReducer = combineReducers({
  session,
  review: reviewsReducer,
  restaurant: restaurantReducer,
  dish: dishReducer,
  order: orderReducer,
  orderDish: orderDishReducer
});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
