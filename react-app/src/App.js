import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import Home from "./components/Home"
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import OrderHistory from "./components/Orders/OrderHistory";
import UserReviews from "./components/Reviews/UserReviews"
import CreateReview from "./components/Reviews/CreateReview";
import OneRestaurant from "./components/Restaurants/OneRestaurant";
import UserRestaurants from "./components/Restaurants/UserRestaurants";
import RestaurantForm from "./components/Restaurants/RestaurantForm"
import DishForm from "./components/Dishes/DishForm";
import CreateRestaurant from "./components/Restaurants/CreateRestaurant"
import Navigation from "./components/Navigation";
import Footer from "./components/Footer";
import Cart from "./components/Cart";

import { authenticate, signUp } from "./store/session";
import SearchResults from "./components/SearchResults/SearchResults";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/login" component={LoginFormPage} />
          <Route exact path="/signup" component={SignupFormPage} />
          <Route exact path="/orders" component={OrderHistory} />
          <Route exact path="/reviews" component={UserReviews} />
          <Route exact path="/restaurants/user" component={UserRestaurants} />
          <Route exact path="/restaurants/new" component={CreateRestaurant} />
          <Route exact path="/restaurants/results" component={SearchResults} />

          {/* <Route exact path="/restaurants/1/dishes/new" component={DishForm} /> */}

          <Route exact path="/restaurants/:restaurantId" component={OneRestaurant} />
          <Route exact path="/cart" component={Cart} />


        </Switch>
      )}
      <Footer isLoaded={isLoaded} />

    </>
  );
}

export default App;
