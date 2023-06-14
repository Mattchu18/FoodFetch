import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import UserReviews from "./components/Reviews/UserReviews"
import CreateReview from "./components/Reviews/CreateReview";
import OneRestaurant from "./components/Restaurants/OneRestaurant";


import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";

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
          <Route exact path="/login" >
            <LoginFormPage />
          </Route>
          <Route exact path="/signup">
            <SignupFormPage />
          </Route>
          <Route exact path="/reviews" component={UserReviews}/>
          <Route exact path="/restaurants/:restaurantId" component={OneRestaurant}/>

          {/* <Route exact path="/restaurants/:restaurantId" component={}/> */}
          {/* <Route exact path="/restaurants/:restaurantId/reviews/new" component={CreateReview}/> */}
        </Switch>
      )}
    </>
  );
}

export default App;
