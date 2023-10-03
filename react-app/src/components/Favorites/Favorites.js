import { thunkCreateFavorite, thunkDeleteFavorite, thunkRestaurantFavorites, thunkUserFavorites } from "../../store/favorite"
import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from "react-redux"

const FavoriteButton = ({favoriteId, restaurantId, filled}) => {
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
        <button onClick={handleClick}>
            {filled ?
                (<i className="fa fa-heart filled" />)
                :
                (<i className="fa fa-heart empty" />)
            }
        </button>
    )
}

export default FavoriteButton
