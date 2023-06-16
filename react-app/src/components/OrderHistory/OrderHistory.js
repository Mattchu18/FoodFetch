import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"

import { thunkUserRestaurants } from "../../store/restaurant"
import { thunkUserReviews } from "../../store/review"
import { Link } from "react-router-dom"

const OrderHistory = () => {
    const dispatch = useDispatch()
    const allUserRestaurantsObj = useSelector(state => state.restaurant.allUserRestaurantsObj)


    useEffect(() => {
        dispatch(thunkUserRestaurants())
        dispatch(thunkUserReviews())
    }, [dispatch])

    return (
        <div>
            <h1>
                Order History
            </h1>
        </div>

    )
}

export default OrderHistory
