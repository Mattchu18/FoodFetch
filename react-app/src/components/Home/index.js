import { useEffect } from "react"
import { thunkAllRestaurants } from "../../store/restaurant"
import { thunkAllReviews } from "../../store/review"
import { useDispatch, useSelector } from "react-redux"
import { Link } from "react-router-dom"
import "./index.css"

const cuisineTypeArr = ["American", "Filipino", "Chinese", "Italian", "Korean", "Mediterranean", "Vietnamese", "Peruvian", "Nepalese", "Indian"]

const Home = () => {
    const dispatch = useDispatch()
    const allRestaurantsObj = useSelector(state => state.restaurant.allRestaurants)
    const allRestaurants = Object.values(allRestaurantsObj)
    const allReviewsObj = useSelector(state => state.review.allReviews)
    const allReviews = Object.values(allReviewsObj)
    console.log("this is all restaurants =====> ", allRestaurantsObj)
    console.log("this is all reviews =====> ", allReviewsObj)
    const topRatedArr = []

    allRestaurants.forEach(restaurant => {
        let sum = 0
        const restaurantReviews = allReviews.filter(review => (review.restaurant_id === restaurant.id))
        restaurantReviews.forEach(review => {
            sum += review.rating
            console.log("This is sum=====>", sum)
        })
        const averageRating = sum / restaurantReviews.length
        if (averageRating >= 2) {
            restaurant["averageRating"] = averageRating
            restaurant["reviewCount"] = restaurantReviews.length
            topRatedArr.push(restaurant)
        }
        // console.log("This is sum2222=====>", sum / restaurantReviews.length)
    })


    console.log("this is topratedarr ===========>", topRatedArr)
    useEffect(() => {
        dispatch(thunkAllRestaurants())
        dispatch(thunkAllReviews())
    }, [dispatch])


    return (
        <div id="home-center">
            <div id="home-container">
                <div id="cuisine-container">
                    {cuisineTypeArr.map(cuisine => (
                        <div id="cuisine-types">
                            <div className="icon">
                                <i class="fa-solid fa-burger"></i>
                            </div>
                            <div className="cuisine-text">
                                <span>{cuisine}</span>
                            </div>
                        </div>
                    ))}

                </div>
                <div id="promo-container">
                    <div className="promo-header">
                        <h2>Top Rated Restaurants</h2>
                        <span> arrows</span>
                    </div>


                    <div className="promo-featured-container">
                        {topRatedArr.map(restaurant => (
                            <div className="top-restaurant-container">
                                <Link to={`/restaurants/${restaurant.id}`}>
                                    <div className="top-restaurant-pic">
                                        PIC
                                    </div>
                                    <div className="top-restaurant-name-rating">
                                        <span>{restaurant.name}</span>
                                        <br/>
                                        <span>{restaurant.averageRating} <i class="fa-solid fa-star"></i> ({restaurant.reviewCount})</span>
                                    </div>
                                </Link>
                            </div>
                        ))}

                    </div>

                </div>
            </div>
        </div>

    )
}

export default Home
