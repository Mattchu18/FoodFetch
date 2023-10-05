import { thunkCreateFavorite, thunkDeleteFavorite, thunkRestaurantFavorites, thunkUserFavorites } from "../../store/favorite"
import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from "react-redux"
import "./FavoriteButton.css"

const FavoriteButton = ({favoriteId, restaurantId, filled, currUser}) => {
    const dispatch = useDispatch()
    // const [favorited, setFavorited] = useState('')

    const handleClick = async () => {
        if (filled) {
            await dispatch(thunkDeleteFavorite(favoriteId))
            await dispatch(thunkRestaurantFavorites(restaurantId))
            // setFavorited(false)
        } else {
            await dispatch(thunkCreateFavorite(restaurantId))
            await dispatch(thunkRestaurantFavorites(restaurantId))
            // setFavorited(true)
        }
    }


    // useEffect(() => {
    //     dispatch(thunkRestaurantFavorites(restaurantId))

    // }, [dispatch, favoriteId, restaurantId, filled])

    return (
        currUser ?
            (<button className="favorite-heart-button" onClick={handleClick}>
            {filled ?
                (<i className="fa fa-heart filled" />)
                :
                (<i className="fa fa-heart empty" />)
            }
            </button>)
            :
            (null)

    )
}

export default FavoriteButton
