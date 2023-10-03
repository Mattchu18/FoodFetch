import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { thunkAllRestaurants } from "../../store/restaurant"
import { Link } from "react-router-dom"

const SearchResults = () => {
    const dispatch = useDispatch()
    const restaurantResultsObj = useSelector(state => state.restaurant.searchRestaurants)
    const restaurantResults = Object.values(restaurantResultsObj)


    useEffect(() => {
        dispatch(thunkAllRestaurants())
    }, [dispatch])

    return (
        <div>
            <div className="search-results-container">
                {!restaurantResults?.length && (<h3>No results found</h3>)}
                {restaurantResults.map(restaurant => (
                    <Link to={`/restaurants/${restaurant.id}`}>
                        <div className="search-results-mapped">
                            <div>
                                <img src={restaurant.image}/>
                                <h3>{restaurant.name}</h3>
                                <span>{restaurant.cuisine_type}</span>
                            </div>
                        </div>
                    </Link>
                ))}
            </div>

        </div>
    )
}

export default SearchResults
