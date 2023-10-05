import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams, useHistory } from "react-router-dom"
import { thunkUserFavorites } from "../../store/favorite";
import { thunkAllRestaurants } from "../../store/restaurant";
import { Link } from "react-router-dom/cjs/react-router-dom.min";
import OpenModalButton from "../OpenModalButton";
import FavoriteButton from "./FavoriteButton";

const FavoritePage = () => {
    const history = useHistory()
        const dispatch = useDispatch()
    const currUser = useSelector(state => state.session.user)
    const userFavoritesObj = useSelector(state => state.favorite.userFavorites)
    const userFavorites = Object.values(userFavoritesObj)
    const restaurantsObj = useSelector(state => state.restaurant.allRestaurants)
    const restaurants = Object.values(restaurantsObj)
    // const favoriteRestaurants = restaurants.filter(restaurant => userFavorites.some(favorites => favorites.restaurant_id === restaurant.id))

    // Convert userFavorites into a hash map
    const favoritesMap = userFavorites.reduce((acc, favorite) => {
        acc[favorite.restaurant_id] = favorite;
        return acc;
    }, {});

    const favoriteRestaurants = restaurants
        .filter(restaurant => favoritesMap[restaurant.id])
        .map(restaurant => ({
            ...restaurant,
            favoriteId: favoritesMap[restaurant.id].id
        }));


    useEffect(() => {
        dispatch(thunkUserFavorites(currUser.id))
        dispatch(thunkAllRestaurants())

    }, [dispatch, currUser])

    console.log("this is userFavorites====> ", userFavorites)
    console.log("this is restaurants====> ", restaurants)
    console.log("this is favoriteRestaurants====> ", favoriteRestaurants)



    return (
        <div>
            {favoriteRestaurants.map(restaurant => (
                <>
                    <Link to={`/restaurants/${restaurant.id}`}>
                        <h2>
                            {restaurant.name}
                        </h2>
                    </Link>

                    {/* make a modal that will confirm unfavorite! */}



                    <FavoriteButton
                        favoriteId={restaurant.favoriteId}
                        restaurantId={restaurant.id}
                        filled={true}
                        currUser={currUser}
                    />
                </>

            ))}

        </div>
    )
}


export default FavoritePage
