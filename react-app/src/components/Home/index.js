import { useEffect, useState } from "react"
import { thunkAllRestaurants } from "../../store/restaurant"
import { thunkAllReviews } from "../../store/review"
import { useDispatch, useSelector } from "react-redux"
import { Link } from "react-router-dom"
import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';
import "./index.css"

import Boba from "../../imgs/cuisine_imgs/boba.png"
import Burgers from "../../imgs/cuisine_imgs/burgers.png"
import Chicken from "../../imgs/cuisine_imgs/chicken.png"
import Chinese from "../../imgs/cuisine_imgs/chinese.png"
import Coffee from "../../imgs/cuisine_imgs/coffee.png"
import Filipino from "../../imgs/cuisine_imgs/filipino.png"
import Mediterranean from "../../imgs/cuisine_imgs/mediterranean.png"
import Pizza from "../../imgs/cuisine_imgs/pizza.png"
import Sushi from "../../imgs/cuisine_imgs/sushi.png"
import Top from "../../imgs/cuisine_imgs/top.png"
import Vietnamese from "../../imgs/cuisine_imgs/vietnamese.png"
import Korean from "../../imgs/cuisine_imgs/korean.png"

const cuisineTypeArr = ["Top", "Burgers", "Boba", "Chicken", "Chinese", "Coffee", "Filipino", "Korean", "Mediterranean", "Pizza", "Sushi", "Vietnamese"]

const cuisineImgs = {
    Boba, Burgers, Chicken, Chinese, Coffee, Filipino, Mediterranean, Pizza, Sushi, Top, Vietnamese, Korean
}

const Home = () => {
    const dispatch = useDispatch()
    const allRestaurantsObj = useSelector(state => state.restaurant.allRestaurants)
    const allRestaurants = Object.values(allRestaurantsObj)
    const allReviewsObj = useSelector(state => state.review.allReviews)
    const allReviews = Object.values(allReviewsObj)

    const topRatedArr = []

    allRestaurants.forEach(restaurant => {
        let sum = 0
        const restaurantReviews = allReviews.filter(review => (review.restaurant_id === restaurant.id))
        restaurantReviews.forEach(review => {
            sum += review.rating
        })
        const averageRating = sum / restaurantReviews.length
        restaurant["averageRating"] = averageRating
        restaurant["reviewCount"] = restaurantReviews.length
        if (averageRating >= 4) {
            topRatedArr.push(restaurant)
        }
    })


    const [cuisine, setCuisine] = useState("Top")
    const filteredRestaurants = cuisine
        ? allRestaurants.filter(restaurant => restaurant.cuisine_type === cuisine)
        : allRestaurants


    useEffect(() => {
        dispatch(thunkAllRestaurants())
        dispatch(thunkAllReviews())
    }, [dispatch])


    return (
        <div id="home-center">
            <div id="home-container">
                <div id="cuisine-container-col">

                    <div id="cuisine-container">

                        {cuisineTypeArr.map(cuisineType => (
                            <div id="cuisine-types"
                            key={cuisineType}
                            onClick={() => setCuisine(cuisineType)}>
                                <div className="icon">
                                    {/* <i class="fa-solid fa-burger"></i> */}
                                    <img className="clickable-img"
                                    src={cuisineImgs[cuisineType]}/>
                                </div>
                                <div className="cuisine-text">
                                    <span>{cuisineType}</span>
                                </div>
                            </div>
                        ))}
                    </div>

                    {cuisine === "Top"
                        ? null : (<div id="promo-container">
                            <div className="promo-header">
                                <h2>{cuisine}</h2>
                            </div>
                            <p>
                                {filteredRestaurants.length === 1
                                    ? `${filteredRestaurants.length} result`
                                    : `${filteredRestaurants.length} results`}
                            </p>
                            <div className="promo-featured-container">

                                {filteredRestaurants.map(restaurant => (
                                    <div className="top-restaurant-container">
                                        <Link to={`/restaurants/${restaurant.id}`}>
                                            <div className="top-restaurant-pic">
                                                <img src={restaurant.header_image}
                                                onError={e => { e.currentTarget.src = "https://cdn.discordapp.com/attachments/1119886170579550301/1119886247956054026/image-coming-soon.png"; }}/>
                                            </div>
                                            <div className="top-restaurant-name-rating">
                                                <strong>{restaurant.name}</strong>
                                                <p className="grey-text">{isNaN(restaurant.averageRating) ? null : restaurant.averageRating.toFixed(1)} <i class="fa-solid fa-star" />  ({restaurant.reviewCount}+ reviews)</p>
                                            </div>
                                        </Link>
                                    </div>
                                ))}

                            </div>

                        </div>)}


                </div>

                <div id="promo-container">
                    <div className="promo-header">
                        <h2>Top Rated Restaurants</h2>
                    </div>


                    <div className="promo-featured-container">
                        {topRatedArr.map(restaurant => (
                            <div className="top-restaurant-container">
                                <Link to={`/restaurants/${restaurant.id}`}>
                                    <div className="top-restaurant-pic">
                                        <img src={restaurant.header_image}
                                                onError={e => { e.currentTarget.src = "https://cdn.discordapp.com/attachments/1119886170579550301/1119886247956054026/image-coming-soon.png"; }}/>
                                                </div>
                                    <div className="top-restaurant-name-rating">
                                        <strong>{restaurant.name}</strong>
                                        <p className="grey-text">{isNaN(restaurant.averageRating) ? null : restaurant.averageRating.toFixed(1)} <i class="fa-solid fa-star" />  ({restaurant.reviewCount}+ reviews)</p>
                                    </div>
                                </Link>
                            </div>
                        ))}

                    </div>

                </div>

                <div id="promo-container">
                    <div className="promo-header">
                        <h2>All Restaurants</h2>
                    </div>


                    <div className="promo-featured-container">
                        {allRestaurants.map(restaurant => (
                            <div className="top-restaurant-container">
                                <Link to={`/restaurants/${restaurant.id}`}>
                                    <div className="top-restaurant-pic">
                                        <img src={restaurant.header_image}
                                                onError={e => { e.currentTarget.src = "https://cdn.discordapp.com/attachments/1119886170579550301/1119886247956054026/image-coming-soon.png"; }}/>
                                    </div>
                                    <div className="top-restaurant-name-rating">
                                        <strong>{restaurant.name}</strong>
                                        <p className="grey-text">{isNaN(restaurant.averageRating) ? null : restaurant.averageRating.toFixed(1)} <i class="fa-solid fa-star" />  ({restaurant.reviewCount}+ reviews)</p>
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
