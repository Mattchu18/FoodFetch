import { thunkOneRestaurant } from "../../store/restaurant";
import { useDispatch, useSelector } from "react-redux"
import { useEffect } from "react"
import { useParams } from "react-router-dom"
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { thunkAllReviews } from "../../store/review";

const OneRestaurant = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const { restaurantId } = useParams()
    const restaurant = useSelector(state => state.restaurant.singleRestaurant[restaurantId])
    const reviewsObj = useSelector(state => state.review.allReviews)
    const reviews = Object.values(reviewsObj)
    const restaurantReviews = reviews.filter(review => review.restaurant_id === parseInt(restaurantId))
    let sum = 0
    restaurantReviews.forEach(review => {
        sum += review.rating
    })
    const averageRating = parseInt((sum / restaurantReviews.length).toFixed(1))
    console.log("this is average rating====>", restaurantReviews)
    /*
    //maybe push to a 404 page in the future
    if (!restaurant) {
        history.push("/")
    }
    */
    useEffect(() => {
        dispatch(thunkOneRestaurant(restaurantId))
        dispatch(thunkAllReviews())
    }, [dispatch])


    if (!restaurant) return null

    return (
        <div>
            <div id="restaurant-details">
                <div>
                    <h1>{restaurant.name}</h1>
                    {Number.isInteger(averageRating) ? (<p>{averageRating} Stars and {restaurantReviews.length} ratings</p>) : (<p>Be the first to review!</p>)}
                </div>
                <div>
                    <p> Today's hours: {restaurant.opening_time} - {restaurant.closing_time}</p>
                </div>
            </div>

            <div id="featured-items">
                <div>
                    <h2>Featured Items</h2>
                </div>
                <div>
                    {/* dishes display here */}
                </div>
            </div>

            <br />

            <div id="restaurant-reviews">
                <div>
                    <h2>What people are saying</h2>
                </div>
                <div>
                    {Number.isInteger(averageRating) ? (<p>{averageRating} Stars and {restaurantReviews.length} ratings</p>) : (<p>Be the first to review!</p>)}
                </div>
                <div>
                    {restaurantReviews.length ? (
                        restaurantReviews.map(review => (
                            <div className="review-container">
                                <div>
                                    <p>{review.username}</p>
                                </div>
                                <div>
                                    <p>{review.rating} stars</p>
                                    <p>{review.created_at}</p>
                                    <p>{review.review_text}</p>
                                </div>
                            </div>
                        ))
                    ) : null}
                </div>
            </div>
        </div>
    )
}

export default OneRestaurant
