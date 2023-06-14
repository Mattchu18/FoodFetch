import { thunkOneRestaurant } from "../../store/restaurant";
import { useDispatch, useSelector } from "react-redux"
import { useEffect } from "react"
import { useParams } from "react-router-dom"

const OneRestaurant = () => {
    const dispatch= useDispatch()
    const { restaurantId } = useParams()
    const restaurant = useSelector(state => state)
    console.log("THIS IS ONE RESTAURANT=======>", restaurant)

    useEffect(() => {
        dispatch(thunkOneRestaurant(restaurantId))
    }, [dispatch])

    return (
        null



    )
}

export default OneRestaurant
