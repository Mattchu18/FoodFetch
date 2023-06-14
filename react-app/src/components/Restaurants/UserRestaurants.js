import { thunkUserRestaurants } from "../../store/restaurant";
import { thunkAllReviews } from "../../store/review";
import { useDispatch, useSelector } from "react-redux"
import { useEffect } from "react"
import { useParams } from "react-router-dom"
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";

const UserRestaurants = () => {
    const dispatch = useDispatch()
    const userRestaurantsObj = useSelector(state => state.restaurant.currentUserRestaurants)
    const userRestaurants = Object.values(userRestaurantsObj)
    // console.log("This is in UserRestaurants======>", userRestaurants)

    useEffect(() => {
        dispatch(thunkUserRestaurants())
        dispatch(thunkAllReviews())
    }, [dispatch])

    return (
        <div>
            <div>
                <h1>Your Restaurants</h1>
            </div>
            <div>
                {userRestaurants?.length ? (<>
                    {userRestaurants.map(restaurant => (
                        <div>
                            <div>
                                <h2>{restaurant.name}</h2>
                            </div>
                            <div>
                                <p>Hours of operation</p>
                                <p>{restaurant.opening_time} - {restaurant.closing_time}</p>
                            </div>
                            <div>
                                <p>Cuisine Type</p>
                                <p>{restaurant.cuisine_type}</p>
                            </div>
                            <div>
                                <p>Phone number</p>
                                <p>{restaurant.phone_number}</p>
                            </div>

                            <div>
                                {/* edit button */}
                                {/* delete button */}
                            </div>
                        </div>
                    ))}</>
                ) : null}
            </div>



        </div>
    )
}

export default UserRestaurants
