import { useEffect } from "react"
import { thunkAllRestaurants } from "../../store/restaurant"
import { useDispatch, useSelector } from "react-redux"
import { Link } from "react-router-dom"


const Home = () => {
    const dispatch = useDispatch()
    const allRestaurantsObj = useSelector(state => state.restaurant.allRestaurants)
    console.log("this is all HOME =====> ", allRestaurantsObj)

    useEffect(() => {
        dispatch(thunkAllRestaurants())
    }, [dispatch])


    return (
        <div>
            <div id="cuisine_types">
                <div>
                    <i class="fa-solid fa-burger"></i>
                </div>
                <div>
                    <p>American</p>
                </div>
            </div>
            <div id="cuisine_types">
                <div>
                    <i class="fa-solid fa-burger"></i>
                </div>
                <div>
                    <p>Filipino</p>
                </div>
            </div>
            <div id="cuisine_types">
                <div>
                    <i class="fa-solid fa-burger"></i>
                </div>
                <div>
                    <p>Chinese</p>
                </div>
            </div>
            <div id="cuisine_types">
                <div>
                    <i class="fa-solid fa-burger"></i>
                </div>
                <div>
                    <p>Italian</p>
                </div>
            </div>
            <div id="cuisine_types">
                <div>
                    <i class="fa-solid fa-burger"></i>
                </div>
                <div>
                    <p>Korean</p>
                </div>
            </div>
            <div id="cuisine_types">
                <div>
                    <i class="fa-solid fa-burger"></i>
                </div>
                <div>
                    <p>Mediterranean</p>
                </div>
            </div>
            <div id="cuisine_types">
                <div>
                    <i class="fa-solid fa-burger"></i>
                </div>
                <div>
                    <p>Vietnamese</p>
                </div>
            </div>
            <div id="cuisine_types">
                <div>
                    <i class="fa-solid fa-burger"></i>
                </div>
                <div>
                    <p>Peruvian</p>
                </div>
            </div>
            <div id="cuisine_types">
                <div>
                    <i class="fa-solid fa-burger"></i>
                </div>
                <div>
                    <p>Nepalese</p>
                </div>
            </div>
            <div id="cuisine_types">
                <div>
                    <i class="fa-solid fa-burger"></i>
                </div>
                <div>
                    <p>Indian</p>
                </div>
            </div>
        </div>

    )
}

export default Home
