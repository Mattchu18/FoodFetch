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
            <div>
                {restaurantResults.map(restaurant => (
                    <Link to={`/restaurants/${restaurant.id}`}>
                        <div>
                            <div>
                                <h3>{restaurant.name}</h3>
                            </div>
                        </div>
                    </Link>
                ))}
            </div>

        </div>
    )
}

export default SearchResults
