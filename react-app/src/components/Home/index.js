import { useEffect } from "react"
import { thunkAllRestaurants } from "../../store/restaurant"
import { useDispatch, useSelector } from "react-redux"
import { Link } from "react-router-dom"
import "./index.css"

const cuisineTypeArr = ["American", "Filipino", "Chinese", "Italian", "Korean", "Mediterranean", "Vietnamese", "Peruvian", "Nepalese", "Indian"]

const Home = () => {
    const dispatch = useDispatch()
    const allRestaurantsObj = useSelector(state => state.restaurant.allRestaurants)
    console.log("this is all HOME =====> ", allRestaurantsObj)

    useEffect(() => {
        dispatch(thunkAllRestaurants())
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
                        <h2>Under $5 dishes</h2>
                        <span> arrows</span>
                    </div>
                    <div className="promo-featured-container">
                        <span>Dishes coming soon</span>
                    </div>
                </div>
            </div>
        </div>

    )
}

export default Home
