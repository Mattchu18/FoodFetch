import { thunkOneRestaurant } from "../../store/restaurant";
import { useDispatch, useSelector } from "react-redux"
import { useEffect } from "react"
import { useParams } from "react-router-dom"
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { thunkAllRestaurantDishes } from "../../store/dish";
import { thunkAllReviews, thunkUserReviews } from "../../store/review";
import OneDish from "../Dishes/OneDish";
import OpenModalButton from "../OpenModalButton";
import CreateReview from "../Reviews/CreateReview";
import DeleteReview from "../Reviews/DeleteReview"
import EditReview from "../Reviews/EditReview"
import "./OneRestaurant.css"


const OneRestaurant = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const { restaurantId } = useParams()
    const restaurant = useSelector(state => state.restaurant.singleRestaurant[restaurantId])
    const reviewsObj = useSelector(state => state.review.allReviews)
    const reviews = Object.values(reviewsObj)
    const currUser = useSelector(state => state.session.user)
    const restaurantReviews = reviews.filter(review => review.restaurant_id === parseInt(restaurantId))
    const restaurantDishesObj = useSelector(state => state.dish.allRestaurantDishes)
    const restaurantDishes = Object.values(restaurantDishesObj)

    console.log("THIS IS RESTAURANTOBJ====>", restaurantDishesObj)

    let sum = 0
    restaurantReviews.forEach(review => {
        sum += review.rating
    })
    const averageRating = parseInt((sum / restaurantReviews.length).toFixed(1))

    const reviewed = restaurantReviews.find(review => review.user_id === currUser?.id)
    /*
    //maybe push to a 404 page in the future
    if (!restaurant) {
        history.push("/")
    }
    */
    useEffect(() => {
        dispatch(thunkOneRestaurant(restaurantId))
        dispatch(thunkAllRestaurantDishes(restaurantId))
        dispatch(thunkAllReviews())
        dispatch(thunkUserReviews())
    }, [dispatch])


    if (!restaurant) return null
    if (!restaurantDishes) return null
    return (
        <div id="restaurant-container">
            <div id="restaurant-img-header"
                style={{
                    backgroundImage: ` url(${restaurant?.header_image})`,
                    backgroundSize: "cover",
                    backgroundPosition: "center",
                    color: "white",
                    // padding: "20px"
                }}>
                <div className="restaurant-image">
                    <img src={restaurant.image} />
                </div>
            </div>
            <div className="restaurant-details">
                <div>
                    <h1>{restaurant.name}</h1>
                    {Number.isInteger(averageRating) ? (
                        <h5>{restaurant.cuisine_type} • {averageRating} <i class="fa-solid fa-star"></i>  {restaurantReviews.length}+ ratings</h5>) : (<p>Be the first to review!</p>)}

                </div>
                <div>
                    <h5>  <i class="fa-regular fa-clock"></i> {restaurant.opening_time} - {restaurant.closing_time}</h5>
                </div>
            </div>

            <div id="featured-items">
                <div className="featured-header">
                    <h3>Featured Items</h3>
                    <span>arrows</span>
                </div>
                <div id="featured-items-carousel">
                    {restaurantDishes.length > 0 ?
                        restaurantDishes.map(dish => (

                            // open a modal that leads to one dish showing
                            //pass in dish as prop to that component
                            <div className="featured-dish">
                                <div className="featured-dish-img">
                                    PIC
                                </div>

                                <OpenModalButton
                                    buttonText="Add"
                                    modalComponent={<OneDish dish={dish} restaurantId={restaurantId} />}

                                />
                                <div className="featured-dish-name-price">

                                    <h4>{dish.name}</h4>
                                    <span>${dish.price}</span>
                                </div>
                            </div>
                            //pass in dish as prop to that component
                            // open a modal that leads to one dish showing



                        )) : <span>Dishes coming soon!</span>}
                    {/* dishes display here */}
                </div>
            </div>


            <div id="restaurant-reviews">
                <div>
                    <h3>What people are saying</h3>
                </div>
                <div>
                    {Number.isInteger(averageRating) ? (
                        <div>
                            <strong>{averageRating} <i class="fa-solid fa-star"></i></strong> <span>{restaurantReviews.length}+ ratings</span>
                        </div>) : (<h4>Be the first to review!</h4>)}
                </div>

                {!reviewed && currUser ? (<div>
                    <OpenModalButton
                        buttonText={"Submit a review!"}
                        modalComponent={<CreateReview restaurantId={restaurantId} />} />
                </div>) : null}



                <div className="review-container">
                    {restaurantReviews.length ? (
                        restaurantReviews.map(review => (
                            <div className="review--container">
                                <div className="review-user-details">
                                    <p>{review.username}</p>
                                    <div className="review-rating-created">
                                        {review.rating == 5 ? (<span>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-solid fa-star"></i>
                                        </span>) : null}

                                        {review.rating == 4 ? (<span>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-regular fa-star"></i>
                                        </span>) : null}

                                        {review.rating == 3 ? (<span>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-regular fa-star"></i>
                                            <i class="fa-regular fa-star"></i>

                                        </span>) : null}

                                        {review.rating == 2 ? (<span>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-regular fa-star"></i>
                                            <i class="fa-regular fa-star"></i>
                                            <i class="fa-regular fa-star"></i>

                                        </span>) : null}

                                        {review.rating == 1 ? (<span>
                                            <i class="fa-solid fa-star"></i>
                                            <i class="fa-regular fa-star"></i>
                                            <i class="fa-regular fa-star"></i>
                                            <i class="fa-regular fa-star"></i>
                                            <i class="fa-regular fa-star"></i>

                                        </span>) : null}

                                        <p>{review.created_at}</p>
                                    </div>
                                </div>
                                <div className="review_text">
                                    <p>{review.review_text}</p>
                                </div>
                                <div className="review-btns-container">
                                    {review.user_id === currUser?.id ?
                                        (<div className="user-review-btn">
                                            <OpenModalButton buttonText="Delete Review" modalComponent={<DeleteReview review={review} />} />
                                        </div>
                                        ) : null}
                                    {review.user_id === currUser?.id ?
                                        (<div className="user-review-btn">
                                            <OpenModalButton buttonText="Edit Review" modalComponent={<EditReview review={review} />} />
                                        </div>) : null}
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
